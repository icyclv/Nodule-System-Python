import io
import math

import numpy as np
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from datetime import datetime
from dateutil.relativedelta import relativedelta
import sys

from addPatientWindow import AddPatientWindow
from addScanDialog import AddScanDialog
from ui.addPatientWindowUI import AddPatientWindowUI
from ui.component.LoadingDialog import LoadingDialog
from ui.CadWindowUI import CadWindowUI
from utils.util import get_type_name
from utils.MyThread import  RequestThread

from DisplayDialog import  DisplayDialog
import qdarkstyle
import json
from faker import Faker
from functools import partial

from utils.SingletionUtils import urlConstants


class NoduleCADx(CadWindowUI):

    def __init__(self):
        super().__init__()

        self.display_dialog = None
        self.preferences_dialog = None
        self.patient_data =None
        self.scan_data = None
        self.display_data = None

        self.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.treeWidgetItem_fun)

        self.noduletreeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.noduletreeWidget.customContextMenuRequested.connect(self.noduletreeWidgetItem_fun)


        self.treeWidget.itemDoubleClicked.connect(self.changePatientInfo)
        # self.refresh_patient_list()
        self.current_search = ""

        self.pageInfo = {
            "current": 1,
            "total": 0,
            "size": 10
        }

        self.currentPageEdit.setText("1")


        self.get_patient_data_pre(1, self.current_search)
        self.prePageButton.clicked.connect(self.prePage)
        self.nextPageButton.clicked.connect(self.nextPage)
        # 按回车键跳转到指定页
        self.currentPageEdit.returnPressed.connect(self.jumpPage)
        self.searchButton.clicked.connect(self.search)
        self.searchEdit.returnPressed.connect(self.search)



    def prePage(self):
        if self.pageInfo["current"] == 1:
            return
        self.get_patient_data_pre(self.pageInfo["current"]-1, self.current_search)


    def nextPage(self):
        if self.pageInfo["current"] == self.pageInfo["total"]:
            return
        self.get_patient_data_pre(self.pageInfo["current"]+1, self.current_search)


    def jumpPage(self):
        page = int(self.currentPageEdit.text())
        if page < 1:
            page = 1
        if page > math.ceil(self.pageInfo["total"] / self.pageInfo["size"]):
            page =  math.ceil(self.pageInfo["total"] / self.pageInfo["size"])
        self.get_patient_data_pre(page, self.current_search)

    def search(self):
        self.current_search = self.searchEdit.text()
        self.get_patient_data_pre(1, self.current_search)



    def treeWidgetItem_fun(self, pos):
        item = self.treeWidget.currentItem()
        if item is not None :
            menu = QMenu()
            item1 = menu.addAction(u"添加扫描")
            item2 = menu.addAction(u"修改患者")
            item3 = menu.addAction(u"删除患者")
            action = menu.exec_(self.treeWidget.mapToGlobal(pos))
            if action == item1:
                self.on_loadDicomButton_clicked()
            elif action == item2:
                self.changePatientInfo()
            elif action == item3:
                self.delete_patient()

    def noduletreeWidgetItem_fun(self, pos):
        item = self.noduletreeWidget.currentItem()
        if item is not None :
            menu = QMenu()
            item2 = menu.addAction(u"查看影像")
            item1 = menu.addAction(u"删除影像")
            action = menu.exec_(self.noduletreeWidget.mapToGlobal(pos))
            if action == item1:
                self.on_displayButton_clicked()
            elif action == item2:
                self.delete_scan()

    def delete_scan(self):
        # 提问是否删除
        reply = QMessageBox.question(self, '删除', "确定删除该影像吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # 否
        if reply == QMessageBox.No:
            return
        if self.noduletreeWidget.selectedItems()[0].parent():
           #获取父节点的第八列的值，也就是id
            id = self.noduletreeWidget.selectedItems()[0].parent().text(7)
        else:
            id = self.noduletreeWidget.selectedItems()[0].text(7)

        url = urlConstants.SCAN_URL + "?id=" + str(id)
        self.request_thread = RequestThread("delete", url)
        self.request_thread.finishSignal.connect(self.delete_scan_post)
        self.request_thread.start()

    def delete_scan_post(self,response):
        if response.status_code == 200:
            res = response.content.decode("utf-8")
            res = json.loads(res)
            if res['success'] == True:
                self.on_treeWidget_itemClicked()
            else:
                if "errorMsg" in res:
                    QMessageBox.information(self, "删除", res['errorMsg'])
        else:
            QMessageBox.information(self, "删除", "删除失败;状态码：" + str(response.status_code))


    def delete_patient(self):
        #提问是否删除
        reply = QMessageBox.question(self, '删除', "确定删除该患者吗？", QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        #否
        if reply == QMessageBox.No:
            return

        index_member = self.treeWidget.currentIndex().row()
        id = self.patient_data[index_member]['id']
        url = urlConstants.PATIENT_URL + "?id=" + str(id)
        self.request_thread = RequestThread("delete", url)
        self.request_thread.finishSignal.connect(self.delete_patient_post)
        self.request_thread.start()

    def delete_patient_post(self,response):
        if response.status_code == 200:
            res = response.content.decode("utf-8")
            res = json.loads(res)
            if res['success'] == True:
                self.get_patient_data_pre(self.pageInfo["current"], self.current_search)
            else:
                if "errorMsg" in res:
                    QtWidgets.QMessageBox.information(self, "删除", res['errorMsg'])
        else:
            QtWidgets.QMessageBox.information(self, "删除", "删除失败;状态码：" + str(response.status_code))



    def refresh_patient_list(self):
        """
        refresh patient list (upper block of main window).
        """
        self.treeWidget.clear()
        self.noduletreeWidget.clear()
        for m in self.patient_data:
            scan_item = QTreeWidgetItem(self.treeWidget,
                                        [m['name'] ,"女" if m['gender'] else "男", m['birthday'],m["phone"],m["backup"]])
            for i in range(scan_item.columnCount()):
                scan_item.setTextAlignment(i, Qt.AlignHCenter)



    def get_patient_data_pre(self,page=1,search=""):

        url = urlConstants.PATIENT_GET_PAGE_URL+"?page="+str(page)+"&search="+search

        self.request_thread = RequestThread("get", url)
        self.request_thread.finishSignal.connect(self.get_patient_data_post)
        self.request_thread.start()

    def get_patient_data_post(self,response):
        if response.status_code == 200:
            res = response.content.decode("utf-8")
            res = json.loads(res)
            if res['success'] == True:
               self.patient_data = res['data']['data']
               self.pageInfo = {
                     "total": res['data']['total'],
                     "size": res['data']['size'],
                     "current": res['data']['current'],
               }
               self.update_page_info()
               self.refresh_patient_list()
            else:
                message = res['message'] if "message" in res else "请求失败"
                QMessageBox.warning(self, "提示", message, QMessageBox.Yes)
        else:
            message = "请求失败"
            QMessageBox.warning(self, "提示", message, QMessageBox.Yes)



    def update_page_info(self):
        self.currentPageEdit.setText(str(self.pageInfo["current"]))

        self.currentPageEdit.setValidator(QIntValidator(1,  math.ceil(self.pageInfo["total"] / self.pageInfo["size"])))
        self.totalPageLabel.setText("第"+str(self.pageInfo["current"])+"页/共"+str(self.pageInfo["total"])+"条")
        if self.pageInfo["current"] == 1:
            self.prePageButton.setEnabled(False)
        else:
            self.prePageButton.setEnabled(True)
        #根据当前页、每页size和总条数数判断是否可以点击下一页
        if self.pageInfo["current"] * self.pageInfo["size"] >= self.pageInfo["total"]:
            self.nextPageButton.setEnabled(False)
        else:
            self.nextPageButton.setEnabled(True)

    def get_scan_data_pre(self,id):
        url = urlConstants.SCAN_GET_BY_PatientID_URL

        self.request_thread = RequestThread("get", url+"?id="+str(id))
        self.request_thread.finishSignal.connect(self.get_scan_data_post)
        self.request_thread.start()


    def get_scan_data_post(self,response):
        if response.status_code == 200:
            res = response.content.decode("utf-8")
            res = json.loads(res)
            if res['success'] == True:
                self.scan_data = res['data']
                self.refresh_scan_list()
            else:
                message = res['message'] if "message" in res else "请求失败"
                QMessageBox.warning(self, "提示", message, QMessageBox.Yes)
        else:
            message = "请求失败;"
            QMessageBox.information(self, "提示", "提交失败;状态码：" + str(response.status_code))

    @pyqtSlot()
    def on_addUserButton_clicked(self):
        self.addPatientWindow = AddPatientWindow()
        self.addPatientWindow.finishSignal.connect(partial(self.get_patient_data_pre,self.pageInfo["current"], self.current_search))
        self.addPatientWindow.show()


    def refresh_scan_list(self):
        """
        refresh scan and nodule list (lower block of main window).
        """
        self.noduletreeWidget.clear()
        for scan in self.scan_data:
            if scan['status'] == 0:
                status = "已排队"
            elif scan['status'] == 1:
                status = "已推理"
            else:
                status = "推理失败"

            p = QTreeWidgetItem(self.noduletreeWidget,[status, scan['time'],str(scan['age']),"","","","",str(scan['id'])])

            for nodule in scan["noduleList"]:
                type_name =get_type_name(nodule['type'])
                n_item = QTreeWidgetItem(p, ['', '', '', str(nodule['confidence']), str(nodule['diameter']),
                                             type_name, str(nodule['classificationProbability']),str(scan['id'])])
                for i in range(n_item.columnCount()):
                    n_item.setTextAlignment(i, Qt.AlignHCenter)
            for i in range(p.columnCount()):
                p.setTextAlignment(i, Qt.AlignHCenter)
        self.noduletreeWidget.expandAll()





    def on_treeWidget_itemClicked(self):
        index_member = self.treeWidget.currentIndex().row()
        self.get_scan_data_pre(self.patient_data[index_member]['id'])

    def changePatientInfo(self):
        index_member = self.treeWidget.currentIndex().row()
        self.addPatientWindow = AddPatientWindow(self.patient_data[index_member]['id'])
        self.addPatientWindow.finishSignal.connect(partial(self.get_patient_data_pre,self.pageInfo["current"], self.current_search))
        self.addPatientWindow.show()


    @pyqtSlot()
    def on_loadDicomButton_clicked(self):
        if self.treeWidget.currentIndex().row() == -1:
            QMessageBox.warning(self, "提示", "请先选择患者", QMessageBox.Yes)
            return
        self.addSacnDialog = AddScanDialog(self.patient_data[self.treeWidget.currentIndex().row()]['id'])
        self.addSacnDialog.finishSignal.connect(partial(self.get_scan_data_pre,self.patient_data[self.treeWidget.currentIndex().row()]['id']))
        self.addSacnDialog.show()



    @pyqtSlot()
    def on_displayButton_clicked(self):
        # 如果是叶子节点，获取父节点的路径
        item = self.noduletreeWidget.currentItem()
        if item is  None:
            QMessageBox.warning(self, "提示", "请先选择影像", QMessageBox.Yes)
            return

        if self.noduletreeWidget.selectedItems()[0].parent():
           #获取父节点的第八列的值，也就是id
            id = self.noduletreeWidget.selectedItems()[0].parent().text(7)
        else:
            id = self.noduletreeWidget.selectedItems()[0].text(7)




        self.loading_dialog = LoadingDialog(self,"下载影像中...")
        self.loading_dialog.show()
        self.request_thread = RequestThread("get", urlConstants.SCAN_INFO_WITH_URL_URL + "?id=" + str(id))
        self.request_thread.finishSignal.connect(self.get_scan_data_step1)
        self.request_thread.start()

    def get_scan_data_step1(self,response):
        if response.status_code == 200:
            res = response.content.decode("utf-8")
            res = json.loads(res)
            if res['success'] == True:
                res = res['data']
                self.display_data = res['scan']
                self.get_scan_data_step2_pre(res['url'])
            else:
                message = res['message'] if "message" in res else "请求失败"
                self.loading_dialog.close()
                QMessageBox.warning(self, "提示", message, QMessageBox.Yes)
        else:

            self.loading_dialog.close()
            QMessageBox.information(self, "提示", "提交失败;状态码：" + str(response.status_code))



    def get_scan_data_step2_pre(self,url):
        self.request_thread = RequestThread("get", url)
        self.request_thread.finishSignal.connect(self.get_scan_data_step2)
        self.request_thread.start()

    def get_scan_data_step2(self,response):
        if response.status_code == 200:
            file = np.load(io.BytesIO(response.content),allow_pickle=True)


            if self.treeWidget.currentItem() is None:
                QMessageBox.warning(self, "提示", "请先选择患者", QMessageBox.Yes)
                return


            self.loading_dialog.close()
            self.display_dialog = DisplayDialog()
            self.display_dialog.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
            self.display_dialog.finishSignal.connect(
                partial(self.get_scan_data_pre, self.patient_data[self.treeWidget.currentIndex().row()]['id']))
            self.display_dialog.w = self.display_dialog.imgLabel_1.width()
            self.display_dialog.h = self.display_dialog.imgLabel_1.height()

            index_member = self.treeWidget.currentIndex().row()

            self.display_dialog.load_dicomfile(self.patient_data[index_member],self.display_data,file['ct'],file['reconstruction'],file['crop_boxes'],file['mask_probs'])
            self.display_dialog.show()
            self.display_dialog.w = self.display_dialog.imgLabel_1.width()
            self.display_dialog.h = self.display_dialog.imgLabel_1.height()
            self.display_dialog.update_shape()
            if self.display_dialog.v.count()>0:
                self.display_dialog.v.itemAt(0).widget().imgLabel.mousePressEvent(event=None)
        else:

            self.loading_dialog.close()
            QMessageBox.information(self, "提示", "下载失败;状态码：" + str(response.status_code))



    # def mousePressEvent(self, event):
    #     if app.focusWidget():
    #         self.setFocus()









if __name__ == '__main__':
    from pyqtgraph.Qt import QtCore, QtWidgets
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))

    window = NoduleCADx()
    window.show()
    sys.exit(app.exec_())
