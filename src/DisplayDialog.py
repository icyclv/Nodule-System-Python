import json
import sys
from functools import partial

import cv2
import numpy as np
import qdarkstyle
# From export image only
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pyqtgraph.opengl import MeshData, GLAxisItem
from pyqtgraph.opengl.items.GLMeshItem import GLMeshItem
from skimage import measure

from ui.ArchiveWeightUI import ArchiveWeightUI
from ui.DisplayDialogUI import DisplayDialogUI
from ui.component.LoadingDialog import LoadingDialog
from ui.component.ReconstructionViewer import QGlyphViewer
from utils.MyThread import CompressFileThread, RequestThread
from utils.SingletionUtils import urlConstants, GlobalDict


class DisplayDialog(DisplayDialogUI):
    finishSignal = pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.processedvoxel = None
        self.v1, self.v2, self.v3 = None, None, None
        self.axial_hSlider.valueChanged.connect(self.updateimg)
        self.axial_vSlider.valueChanged.connect(self.updateimg)
        self.coronal_vSlider.valueChanged.connect(self.updateimg)
        self.display_bbox = self.bboxcheckBox.isChecked()
        self.display_mask = self.maskcheckBox.isChecked()
        self.display_vtkmask = self.vtkMaskCheckBox.isChecked()
        self.display_crosscenter = self.crosscentercheckBox.isChecked()
        self.imgLabel_1.type = 'axial'
        self.imgLabel_2.type = 'sagittal'
        self.imgLabel_3.type = 'coronal'
        self.fullimgLabel.type = 'full'

        self.axialGrid.setSpacing(0)
        self.saggitalGrid.setSpacing(0)
        self.coronalGrid.setSpacing(0)

        self.savesliceBox.setItemDelegate(QStyledItemDelegate(self.savesliceBox))
        self.savesliceButton.clicked.connect(self.saveslice_clicked)

        self.imgLabel_1.mpsignal.connect(self.cross_center_mouse)
        self.imgLabel_2.mpsignal.connect(self.cross_center_mouse)
        self.imgLabel_3.mpsignal.connect(self.cross_center_mouse)

        self.cross_recalc = True
        self.w, self.h = 0, 0
        self.oldwidget = None

        self.item = None
        self.delete_index = []
        self.delete_un_save = False

        self.fullimage = None

        self.vtkFrame = QGlyphViewer(self.reconstructionFrame)
        self.vtk_layout = QHBoxLayout()
        self.vtk_layout.addWidget(self.vtkFrame)
        self.reconstructionFrame.setLayout(self.vtk_layout)
        self.confirmButton.clicked.connect(self.save_change)

        self.axialButton.setStyleSheet('QPushButton {min-width: 10px;  min-height: 10px;}')
        self.sagittalButton.setStyleSheet('QPushButton {min-width: 10px;  min-height: 10px;}')
        self.coronalButton.setStyleSheet('QPushButton {min-width: 10px;  min-height: 10px;}')

        self.axial_mask, self.sagittal_mask, self.coronal_mask, self.seg_mask = None, None, None, None
        self.crop_boxes, self.mask_probs, self.re = None, None, None
        self.nodules_data = None


    def load_dicomfile(self,patient_data, scan_data, ct, reconstruction, crop_boxes, mask_probs):
        self.patient_data = patient_data
        self.nodules_data = scan_data["noduleList"].copy()
        del scan_data["noduleList"]
        self.scan_data = scan_data
        self.appearanceTextEdit.setPlainText(self.scan_data["appearance"])
        self.diagnosisTextEdit.setPlainText(self.scan_data["diagnosis"])


        self.processedvoxel = ct
        self.crop_boxes = crop_boxes
        self.mask_probs = mask_probs
        self.re = reconstruction
        self.re[self.re == 255] = 254
        self.set_reconstruction()
        self.update_shape()
        self.refresh_mask()

        self.imgLabel_1.setMouseTracking(True)
        self.imgLabel_2.setMouseTracking(True)
        self.imgLabel_3.setMouseTracking(True)
        self.w = self.imgLabel_1.width()
        self.h = self.imgLabel_1.height()
        self.update_shape()
        if len(self.crop_boxes) > 0:
            self.GLViewWidget.addItem(GLAxisItem(size=QVector3D(4, 4, 4), glOptions='opaque'))
            self.set_archive(0)
        else:
            self.set_archive()

    def cross_center_mouse(self, _type):
        self.cross_recalc = False
        if _type == 'axial':
            self.axial_hSlider.valueChanged.disconnect(self.updateimg)

            self.axial_hSlider.setValue(self.imgLabel_1.crosscenter[0] *
                                        self.axial_hSlider.maximum() / self.imgLabel_1.width())
            self.axial_vSlider.setValue(self.imgLabel_1.crosscenter[1] *
                                        self.axial_vSlider.maximum() / self.imgLabel_1.height())

            self.axial_hSlider.valueChanged.connect(self.updateimg)

        elif _type == 'sagittal':
            self.axial_vSlider.valueChanged.disconnect(self.updateimg)

            self.sagittal_hSlider.setValue(self.imgLabel_2.crosscenter[0] *
                                           self.sagittal_hSlider.maximum() / self.imgLabel_2.width())
            self.sagittal_vSlider.setValue(self.sagittal_vSlider.maximum() - self.imgLabel_2.crosscenter[1] *
                                           self.sagittal_vSlider.maximum() / self.imgLabel_2.height())

            self.axial_vSlider.valueChanged.connect(self.updateimg)

        elif _type == 'coronal':
            self.axial_hSlider.valueChanged.disconnect(self.updateimg)

            self.coronal_hSlider.setValue(self.imgLabel_3.crosscenter[0] *
                                          self.coronal_hSlider.maximum() / self.imgLabel_3.width())
            self.coronal_vSlider.setValue(self.coronal_vSlider.maximum() - self.imgLabel_3.crosscenter[1] *
                                          self.coronal_vSlider.maximum() / self.imgLabel_3.height())

            self.axial_hSlider.valueChanged.connect(self.updateimg)

        self.imgLabel_1.crosscenter = [
            self.axial_hSlider.value() * self.imgLabel_1.width() / self.axial_hSlider.maximum(),
            self.axial_vSlider.value() * self.imgLabel_1.height() / self.axial_vSlider.maximum()]
        self.imgLabel_2.crosscenter = [
            self.sagittal_hSlider.value() * self.imgLabel_2.width() / self.sagittal_hSlider.maximum(),
            (self.sagittal_vSlider.maximum() - self.sagittal_vSlider.value()) *
            self.imgLabel_2.height() / self.sagittal_vSlider.maximum()]
        self.imgLabel_3.crosscenter = [
            self.coronal_hSlider.value() * self.imgLabel_3.width() / self.coronal_hSlider.maximum(),
            (self.sagittal_vSlider.maximum() - self.coronal_vSlider.value()) *
            self.imgLabel_3.height() / self.coronal_vSlider.maximum()]

        self.cross_recalc = True

    def saveslice_clicked(self):
        fname, _filter = QFileDialog.getSaveFileName(self, 'save file', '~/untitled', "Image Files (*.jpg)")
        if fname:
            if self.savesliceBox.currentText() == 'Axial':
                cv2.imwrite(fname, self.imgLabel_1.processedImage)
            elif self.savesliceBox.currentText() == 'Saggital':
                cv2.imwrite(fname, self.imgLabel_2.processedImage)
            elif self.savesliceBox.currentText() == 'Coronal':
                cv2.imwrite(fname, self.imgLabel_3.processedImage)
            else:
                print('No slice be chosen')
        else:
            print('Error')

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.w = self.imgLabel_1.width()
        self.h = self.imgLabel_1.height()

        if self.processedvoxel is not None:
            self.updateimg()



    def set_reconstruction(self):
        self.vtkFrame.load(self.re)
        self.vtkFrame.resizeEvent(None)
        self.vtkFrame.start()

    def updateReconstruction(self):
        re = self.re.copy()
        if self.display_vtkmask:
            re[self.re_mask] = 255
        self.vtkFrame.re_render(re)

    def set_archive(self, nodule_select=None):
        '''
        设定左侧边框的内容
        '''
        self.v = QVBoxLayout()
        self.v.setAlignment(Qt.AlignTop)
        self.v.setSpacing(10)
        self.groupBox.setLayout(self.v)
        # 根据结节数量设定边框大小
        if len(self.crop_boxes) > 3:
            self.scrollAreaWidgetContents_2.setMinimumSize(442, len(self.crop_boxes) * 120)
        for i, (d, b, p) in enumerate(zip(self.nodules_data, self.crop_boxes, self.mask_probs)):
            w = ArchiveWeightUI(d["id"])

            # TODO 到底xyz还是zyx... 要搞清楚
            z, y, x = d["coordinate"].split(',')
            w.tableWidget.setItem(0, 0, QTableWidgetItem(f"{x}, {y}, {z}"))
            w.tableWidget.setItem(1, 0, QTableWidgetItem(str(d['confidence'])))
            # diameter
            w.tableWidget.setItem(2, 0, QTableWidgetItem(str(d['diameter'])))
            infomation = ['良性', '恶性']
            combox = QComboBox(w.tableWidget)
            combox.addItems(infomation)
            combox.setCurrentIndex(d["type"])
            # QDarkStyle的combobox有bug，要加這句delegate才可以解決
            combox.setItemDelegate(QStyledItemDelegate(combox))

            w.tableWidget.setCellWidget(3, 0, combox)
            # score
            w.tableWidget.setItem(4, 0, QTableWidgetItem(str(d['classificationProbability'])))
            # thumbnail
            w.imgLabel.coord = [int(x), int(y), int(z)]
            w.deleteButton.clicked.connect(partial(self.delete_nodule, w, i))

            self.v.addWidget(w)
            w.imgLabel.processedImage = self.processedvoxel[b[1]:b[4], b[2]:b[5], (b[3] + b[6]) // 2].copy()
            w.imgLabel.display_image(1)

            w.imgLabel.mpsignal.connect(partial(self.changeSelectedNodule, w))
            w.imgLabel.index = i

            if nodule_select == i:
                w.imgLabel.mousePressEvent(event=None)

    def delete_nodule(self, archive_widget: ArchiveWeightUI, i):
        if archive_widget == self.oldwidget:
            self.remove3d()
        archive_widget.setVisible(False)
        self.v.removeWidget(archive_widget)
        self.refresh_mask(i)

    @pyqtSlot()
    def on_zoomButton_clicked(self):
        self.fullimgLabel.zoom = True

    @pyqtSlot()
    def on_returnButton_clicked(self):
        self.stackedWidget.setCurrentIndex(0)
        self.fullimage = None
        self.full_vSlider.valueChanged.disconnect()
        self.full_vSlider.setValue(self.full_vSlider.maximum() // 2)
        self.fullimgLabel.zoom = False
        self.fullimgLabel.zoom_corner = [[0, 0]]
        self.update_shape()
        self.updateimg()

    @pyqtSlot()
    def on_axialButton_clicked(self):
        self.stackedWidget.setCurrentIndex(1)
        self.fullimage = 'axial'
        self.full_vSlider.setMaximum(self.sagittal_vSlider.maximum())
        self.full_vSlider.setValue(self.sagittal_vSlider.value())
        self.full_vSlider.valueChanged.connect(self.sagittal_vSlider.setValue)
        self.updateimg()

    @pyqtSlot()
    def on_sagittalButton_clicked(self):
        self.stackedWidget.setCurrentIndex(1)
        self.fullimage = 'sagittal'
        self.full_vSlider.setMaximum(self.axial_hSlider.maximum())
        self.full_vSlider.setValue(self.full_vSlider.value())
        self.full_vSlider.valueChanged.connect(self.axial_hSlider.setValue)
        self.updateimg()

    @pyqtSlot()
    def on_coronalButton_clicked(self):
        self.stackedWidget.setCurrentIndex(1)
        self.fullimage = 'coronal'
        self.full_vSlider.setMaximum(self.axial_vSlider.maximum())
        self.full_vSlider.setValue(self.full_vSlider.value())
        self.full_vSlider.valueChanged.connect(self.axial_vSlider.setValue)
        self.updateimg()



    def refresh_mask(self, i=None):
        # 更新self.crop_boxes, self.mask_probs
        if i is not None:
            self.delete_index.append(i)
            self.delete_un_save = True

        self.axial_mask = np.zeros_like(self.processedvoxel, dtype=bool)
        self.sagittal_mask = np.zeros_like(self.processedvoxel, dtype=bool)
        self.coronal_mask = np.zeros_like(self.processedvoxel, dtype=bool)
        self.seg_mask = np.zeros_like(self.processedvoxel, dtype=bool)
        self.re_mask = np.zeros_like(self.processedvoxel, dtype=bool)
        for j, (b, p) in enumerate(zip(self.crop_boxes, self.mask_probs)):
            if j in self.delete_index:
                continue
            self.axial_mask[b[1]:b[4], b[2]:b[5], b[3]:b[6]] = True
            self.sagittal_mask[b[1]:b[4], b[2]:b[5], b[3]:b[6]] = True
            self.coronal_mask[b[1]:b[4], b[2]:b[5], b[3]:b[6]] = True
            # line width
            lw = 2
            self.axial_mask[b[1]:b[4], b[2] + lw:b[5] - lw, b[3] + lw:b[6] - lw] = False
            self.sagittal_mask[b[1] + lw:b[4] - lw, b[2] + lw:b[5] - lw, b[3]:b[6]] = False
            self.coronal_mask[b[1] + lw:b[4] - lw, b[2]:b[5], b[3] + lw:b[6] - lw] = False

            self.seg_mask[b[1]:b[4], b[2]:b[5], b[3]:b[6]][p > 0] = True
            self.re_mask[b[1]:b[4], b[2]:b[5], b[3]:b[6]][p > 0] = True

        self.updateimg()
        self.updateReconstruction()

    def changeSelectedNodule(self, widget, coord, index):
        # 设置当前选中的widget的边框为红色，此前选中的widget的边框恢复蓝色
        if self.oldwidget is not None:
            self.oldwidget.imgLabel.setStyleSheet('border: 1px solid SteelBlue;')
        widget.imgLabel.setStyleSheet('border: 1px solid red;')
        self.oldwidget = widget

        # 更新三个slider的位置
        self.axial_hSlider.setValue(coord[0] / self.v3 * self.axial_hSlider.maximum())
        self.axial_vSlider.setValue(coord[1] / self.v2 * self.axial_vSlider.maximum())
        self.coronal_vSlider.setValue(coord[2] / self.v1 * self.coronal_vSlider.maximum())

        self.updateimg()
        self.display3d(index)

    def remove3d(self):
        if self.item in self.GLViewWidget.items:
            self.GLViewWidget.removeItem(self.item)

    def display3d(self, index):

        self.remove3d()
        b = self.crop_boxes[index]
        voxel = np.zeros((b[4] - b[1], b[5] - b[2], b[6] - b[3]))
        voxel[self.seg_mask[b[1]:b[4], b[2]:b[5], b[3]:b[6]]] = 1

        # q
        verts, faces, norm, val = measure.marching_cubes_lewiner(voxel, level=0.5, spacing=(1, 1, 1),
                                                                 gradient_direction='descent', step_size=1,
                                                                 allow_degenerate=True)

        mesh = MeshData(verts / 4, faces)  # 缩小尺寸，否则3d模型太大，需要用户自行调整
        mesh._vertexNormals = norm  # 设置法向量
        # mesh.setFaceColors(colors)
        # self.item = GLMeshItem(meshdata=mesh, color=[1, 1, 1, 1], shader="normalColor", drawEdges = False, smooth=True)
        self.item = GLMeshItem(meshdata=mesh, shader='shaded', color=(1, 20 / 255, 60 / 255, 1), drawEdges=False,
                               smooth=True)

        # 设置3d模型的位置，使其位于中心
        t1 = (mesh._vertexes[:, 0].max() + mesh._vertexes[:, 0].min()) / 2
        t2 = (mesh._vertexes[:, 1].max() + mesh._vertexes[:, 1].min()) / 2
        t3 = (mesh._vertexes[:, 2].max() + mesh._vertexes[:, 2].min()) / 2

        self.item.translate(-t1, -t2, -t3, local=True)
        self.GLViewWidget.addItem(self.item)

    def on_bboxcheckBox_toggled(self, _bool):
        self.display_bbox = _bool
        self.updateimg()

    def on_maskcheckBox_toggled(self, _bool):
        self.display_mask = _bool
        self.updateimg()

    def on_vtkMaskCheckBox_toggled(self, _bool):
        self.display_vtkmask = _bool
        self.updateReconstruction()

    def on_crosscentercheckBox_toggled(self, _bool):
        self.display_crosscenter = _bool
        self.imgLabel_1.show_cross = _bool
        self.imgLabel_2.show_cross = _bool
        self.imgLabel_3.show_cross = _bool
        self.updateimg()

    def update_shape(self):
        self.axial_hSlider.valueChanged.disconnect(self.updateimg)
        self.axial_vSlider.valueChanged.disconnect(self.updateimg)
        self.coronal_vSlider.valueChanged.disconnect(self.updateimg)

        self.v1, self.v2, self.v3 = self.processedvoxel.shape

        self.sagittal_vSlider.setMaximum(self.v1 - 1)
        self.coronal_vSlider.setMaximum(self.v1 - 1)
        self.sagittal_hSlider.setMaximum(self.v2 - 1)
        self.axial_vSlider.setMaximum(self.v2 - 1)
        self.coronal_hSlider.setMaximum(self.v3 - 1)
        self.axial_hSlider.setMaximum(self.v3 - 1)
        self.sagittal_vSlider.setValue(self.sagittal_vSlider.maximum() // 2)
        self.coronal_vSlider.setValue(self.coronal_vSlider.maximum() // 2)
        self.sagittal_hSlider.setValue(self.sagittal_hSlider.maximum() // 2)
        self.axial_vSlider.setValue(self.axial_vSlider.maximum() // 2)
        self.coronal_hSlider.setValue(self.coronal_hSlider.maximum() // 2)
        self.axial_hSlider.setValue(self.axial_hSlider.maximum() // 2)

        self.axial_hSlider.valueChanged.connect(self.updateimg)
        self.axial_vSlider.valueChanged.connect(self.updateimg)
        self.coronal_vSlider.valueChanged.connect(self.updateimg)



    def get_three_img(self, z, y, x):
        a_loc = z
        c_loc = y
        s_loc = x

        axial = cv2.cvtColor((self.processedvoxel[a_loc, :, :]).astype(np.uint8), cv2.COLOR_GRAY2RGB)
        sagittal = cv2.cvtColor((self.processedvoxel[:, :, s_loc]).astype(np.uint8), cv2.COLOR_GRAY2RGB)
        coronal = cv2.cvtColor((self.processedvoxel[:, c_loc, :]).astype(np.uint8), cv2.COLOR_GRAY2RGB)

        if self.display_bbox:
            axial_mask = np.zeros_like(axial)
            axial_mask[:, :, 0][self.axial_mask[a_loc, :, :]] = 255
            sagittal_mask = np.zeros_like(sagittal)
            sagittal_mask[:, :, 0][self.sagittal_mask[:, :, s_loc]] = 255
            coronal_mask = np.zeros_like(coronal)
            coronal_mask[:, :, 0][self.coronal_mask[:, c_loc, :]] = 255

            axial = cv2.addWeighted(axial, 1, axial_mask, 1, 0)
            sagittal = cv2.addWeighted(sagittal, 1, sagittal_mask, 1, 0)
            coronal = cv2.addWeighted(coronal, 1, coronal_mask, 1, 0)

        if self.display_mask:
            # 如果需要在图像上显示分割结果的轮廓，可以使用下面的代码
            axial_mask2 = np.zeros_like(axial)
            axial_mask2[:, :, 0][self.seg_mask[a_loc, :, :]] = 255
            axial_mask2[:, :, 1][self.seg_mask[a_loc, :, :]] = 255
            sagittal_mask2 = np.zeros_like(sagittal)
            sagittal_mask2[:, :, 0][self.seg_mask[:, :, s_loc]] = 255
            sagittal_mask2[:, :, 1][self.seg_mask[:, :, s_loc]] = 255
            coronal_mask2 = np.zeros_like(coronal)
            coronal_mask2[:, :, 0][self.seg_mask[:, c_loc, :]] = 255
            coronal_mask2[:, :, 1][self.seg_mask[:, c_loc, :]] = 255

            axial = cv2.addWeighted(axial, 1, axial_mask2, 0.2, 0)
            sagittal = cv2.addWeighted(sagittal, 1, sagittal_mask2, 0.2, 0)
            coronal = cv2.addWeighted(coronal, 1, coronal_mask2, 0.2, 0)

        sagittal = cv2.flip(sagittal, 0)
        coronal = cv2.flip(coronal, 0)

        return axial, sagittal, coronal

    def updateimg(self):
        a_loc = self.coronal_vSlider.value()
        c_loc = self.axial_vSlider.value()
        s_loc = self.axial_hSlider.value()

        axial = cv2.cvtColor((self.processedvoxel[a_loc, :, :]).astype(np.uint8), cv2.COLOR_GRAY2RGB)
        sagittal = cv2.cvtColor((self.processedvoxel[:, :, s_loc]).astype(np.uint8), cv2.COLOR_GRAY2RGB)
        coronal = cv2.cvtColor((self.processedvoxel[:, c_loc, :]).astype(np.uint8), cv2.COLOR_GRAY2RGB)

        if self.display_bbox:
            axial_mask = np.zeros_like(axial)
            axial_mask[:, :, 0][self.axial_mask[a_loc, :, :]] = 255
            sagittal_mask = np.zeros_like(sagittal)
            sagittal_mask[:, :, 0][self.sagittal_mask[:, :, s_loc]] = 255
            coronal_mask = np.zeros_like(coronal)
            coronal_mask[:, :, 0][self.coronal_mask[:, c_loc, :]] = 255

            axial = cv2.addWeighted(axial, 1, axial_mask, 1, 0)
            sagittal = cv2.addWeighted(sagittal, 1, sagittal_mask, 1, 0)
            coronal = cv2.addWeighted(coronal, 1, coronal_mask, 1, 0)

        if self.display_mask:
            # 如果需要在图像上显示分割结果的轮廓，可以使用下面的代码
            axial_mask2 = np.zeros_like(axial)
            axial_mask2[:, :, 0][self.seg_mask[a_loc, :, :]] = 255
            axial_mask2[:, :, 1][self.seg_mask[a_loc, :, :]] = 255
            sagittal_mask2 = np.zeros_like(sagittal)
            sagittal_mask2[:, :, 0][self.seg_mask[:, :, s_loc]] = 255
            sagittal_mask2[:, :, 1][self.seg_mask[:, :, s_loc]] = 255
            coronal_mask2 = np.zeros_like(coronal)
            coronal_mask2[:, :, 0][self.seg_mask[:, c_loc, :]] = 255
            coronal_mask2[:, :, 1][self.seg_mask[:, c_loc, :]] = 255

            axial = cv2.addWeighted(axial, 1, axial_mask2, 0.2, 0)
            sagittal = cv2.addWeighted(sagittal, 1, sagittal_mask2, 0.2, 0)
            coronal = cv2.addWeighted(coronal, 1, coronal_mask2, 0.2, 0)

        sagittal = cv2.flip(sagittal, 0)
        coronal = cv2.flip(coronal, 0)

        self.imgLabel_1.slice_loc = [s_loc, c_loc, a_loc]
        self.imgLabel_2.slice_loc = [s_loc, c_loc, a_loc]
        self.imgLabel_3.slice_loc = [s_loc, c_loc, a_loc]

        if self.cross_recalc:
            self.imgLabel_1.crosscenter = [self.w * s_loc // self.v3, self.h * c_loc // self.v2]
            self.imgLabel_2.crosscenter = [self.w * c_loc // self.v2,
                                           self.h * (self.sagittal_vSlider.maximum() - a_loc) // self.v1]
            self.imgLabel_3.crosscenter = [self.w * s_loc // self.v3,
                                           self.h * (self.sagittal_vSlider.maximum() - a_loc) // self.v1]

        if self.fullimage:

            self.fullimgLabel.processedImage = eval(self.fullimage)
            self.fullimgLabel.display_image(1)

        else:
            self.imgLabel_1.processedImage = axial
            self.imgLabel_2.processedImage = sagittal
            self.imgLabel_3.processedImage = coronal

            self.imgLabel_1.display_image(1)
            self.imgLabel_2.display_image(1)
            self.imgLabel_3.display_image(1)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        super().closeEvent(a0)
        self.vtkFrame.close()
        self.GLViewWidget.close()

    def save_change(self):
        # TODO (1)從現有archive把資料存起來，之後要回傳給main修改scan內容的 (2)更新self.crop_boxes, self.mask_probs，離開此畫面時要重存npy
        # 這邊要做的事類似'detect' function
        print(11)
        for i in range(self.v.count()):
            if i in self.delete_index:
                self.nodules_data[i]["isDeleted"] = True
                continue
            w = self.v.itemAt(i).widget()
            x, y, z = [s.strip() for s in w.tableWidget.item(0, 0).text().split(',')]

            self.nodules_data[i]["coordinate"] = f"{z},{y},{x}"

            confidence = w.tableWidget.item(1, 0).text()

            self.nodules_data[i]["confidence"] = float(confidence)

            diameter = w.tableWidget.item(2, 0).text()

            self.nodules_data[i]["diameter"] = float(diameter)

            nodule_type = w.tableWidget.cellWidget(3, 0).currentIndex()

            self.nodules_data[i]["type"] = nodule_type

            classificationProbability = w.tableWidget.item(4, 0).text()
            self.nodules_data[i]["classificationProbability"] = float(classificationProbability)

        if len(self.delete_index) > 0 and self.delete_un_save == True:

            crop_boxes = np.delete(self.crop_boxes, self.delete_index, axis=0)
            mask_probs = np.delete(self.mask_probs, self.delete_index, axis=0)
            self.delete_un_save = False
            self.loadingDialog = LoadingDialog(self, "压缩中...")
            self.loadingDialog.show()
            self.compress_changed_files(crop_boxes, mask_probs)
        else:

            self.loadingDialog = LoadingDialog(self, "上传中...")
            self.loadingDialog.show()
            self.upload_changed_info(True, None)

    def compress_changed_files(self, crop_boxes, mask_probs):

        self.compressThread = CompressFileThread(self.processedvoxel, self.re, crop_boxes, mask_probs)
        self.compressThread.finishSignal.connect(self.upload_changed_info)
        self.compressThread.start()

    def upload_changed_info(self, type, compressed_file):

        if type == False:
            self.loadingDialog.close()
            self.loadingDialog = None
            QtWidgets.QMessageBox.information(self, "提示", "保存失败")
            return

        self.loadingDialog.label.setText("上传中...")
        self.nodules_data = self.nodules_data[:2]
        self.scan_data["noduleList"] = self.nodules_data
        self.scan_data["appearance"] = self.appearanceTextEdit.toPlainText()
        self.scan_data["diagnosis"] = self.diagnosisTextEdit.toPlainText()

        params = {
            "scan": json.dumps(self.scan_data),

        }

        url = urlConstants.SCAN_UPDATE_WITH_FILE_URL

        if compressed_file is None:
            self.request_thread = RequestThread("post", url, data=params)
        else:
            self.request_thread = RequestThread("post", url, data=params, files={'file': compressed_file})

        self.request_thread.finishSignal.connect(self.upload_post)
        self.request_thread.start()

    def upload_post(self, response):
        self.loadingDialog.close()
        self.loadingDialog = None
        if response.status_code == 200:
            res = response.content.decode("utf-8")
            res = json.loads(res)
            if res['success'] == True:
                QtWidgets.QMessageBox.information(self, "提示", "提交成功")
                self.finishSignal.emit(1)
                self.close()
            else:
                if "errorMsg" in res:
                    QtWidgets.QMessageBox.information(self, "提示", res['errorMsg'])
        else:

            QtWidgets.QMessageBox.information(self, "提示", "提交失败;状态码：" + str(response.status_code))

    def get_img_list(self):
        self.img_list = []
        for nodule in self.nodules_data:
            if nodule["isDeleted"] == True:
                continue
            else:
                z, y, x = nodule["coordinate"].split(',')
                z, y, x = int(z), int(y), int(x)
                self.img_list.append(self.get_three_img(z, y, x))




    def report_pre(self):
        report_config = GlobalDict.get("pdfReport").copy()







if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    ex = DisplayDialog()
    ex.show()
    ex.w, ex.h = ex.imgLabel_1.width(), ex.imgLabel_1.height()
    sys.exit(app.exec_())
