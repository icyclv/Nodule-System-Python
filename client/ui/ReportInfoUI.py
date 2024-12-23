# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\a_bishe\code\Nodule-System-Python\client\ui\file\report_info.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import qdarkstyle
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class ReportInfoUI(QDialog):
    def __init__(self, parent=None):
        super(ReportInfoUI, self).__init__(parent)

        self.setupUi(self)
        self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(772, 936)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setContentsMargins(12, -1, 12, -1)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.titleEdit = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.titleEdit.setFont(font)
        self.titleEdit.setStyleSheet("QLineEdit {\n"
                                     "    border-radius: 5px;\n"
                                     "}")
        self.titleEdit.setText("")
        self.titleEdit.setMaxLength(32)
        self.titleEdit.setReadOnly(False)
        self.titleEdit.setObjectName("titleEdit")
        self.gridLayout.addWidget(self.titleEdit, 0, 2, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit.setStyleSheet("QDateTimeEdit {\n"
                                        "    border-radius: 5px;\n"
                                        "}")
        self.dateTimeEdit.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 3, 14), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout.addWidget(self.dateTimeEdit, 2, 2, 1, 1)
        self.appearanceBox = QtWidgets.QCheckBox(Dialog)
        self.appearanceBox.setChecked(True)
        self.appearanceBox.setObjectName("appearanceBox")
        self.gridLayout.addWidget(self.appearanceBox, 4, 0, 1, 1)
        self.appearancePlainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.appearancePlainTextEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.appearancePlainTextEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.appearancePlainTextEdit.setObjectName("appearancePlainTextEdit")
        self.gridLayout.addWidget(self.appearancePlainTextEdit, 4, 2, 1, 1)
        self.diagnosisBox = QtWidgets.QCheckBox(Dialog)
        self.diagnosisBox.setChecked(True)
        self.diagnosisBox.setObjectName("diagnosisBox")
        self.gridLayout.addWidget(self.diagnosisBox, 5, 0, 1, 1)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 8, 0, 1, 3)
        self.diagnosPlainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.diagnosPlainTextEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.diagnosPlainTextEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.diagnosPlainTextEdit.setObjectName("diagnosPlainTextEdit")
        self.gridLayout.addWidget(self.diagnosPlainTextEdit, 5, 2, 1, 1)
        self.subtitleEdit = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.subtitleEdit.setFont(font)
        self.subtitleEdit.setStyleSheet("QLineEdit {\n"
                                        "    border-radius: 5px;\n"
                                        "}")
        self.subtitleEdit.setText("")
        self.subtitleEdit.setMaxLength(32)
        self.subtitleEdit.setReadOnly(False)
        self.subtitleEdit.setObjectName("subtitleEdit")
        self.gridLayout.addWidget(self.subtitleEdit, 1, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QtCore.QSize(0, 33))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMinimumSize(QtCore.QSize(0, 33))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setMinimumSize(QtCore.QSize(0, 33))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.noduleTableBox = QtWidgets.QCheckBox(Dialog)
        self.noduleTableBox.setChecked(True)
        self.noduleTableBox.setObjectName("noduleTableBox")
        self.horizontalLayout_2.addWidget(self.noduleTableBox)
        self.noduleImgBox = QtWidgets.QCheckBox(Dialog)
        self.noduleImgBox.setChecked(True)
        self.noduleImgBox.setObjectName("noduleImgBox")
        self.horizontalLayout_2.addWidget(self.noduleImgBox)
        self.footerBox = QtWidgets.QCheckBox(Dialog)
        self.footerBox.setChecked(True)
        self.footerBox.setObjectName("footerBox")
        self.horizontalLayout_2.addWidget(self.footerBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 0, 1, 3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.patientInfoBox = QtWidgets.QCheckBox(Dialog)
        self.patientInfoBox.setChecked(True)
        self.patientInfoBox.setObjectName("patientInfoBox")
        self.horizontalLayout.addWidget(self.patientInfoBox)
        self.addButton = QtWidgets.QPushButton(Dialog)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.changeButton = QtWidgets.QPushButton(Dialog)
        self.changeButton.setObjectName("changeButton")
        self.horizontalLayout.addWidget(self.changeButton)
        self.deleteButton = QtWidgets.QPushButton(Dialog)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setLineWidth(1)
        self.listWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.DoubleClicked | QtWidgets.QAbstractItemView.EditKeyPressed | QtWidgets.QAbstractItemView.SelectedClicked)
        self.listWidget.setDragEnabled(True)
        self.listWidget.setDragDropOverwriteMode(False)
        self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.gridLayout.addLayout(self.verticalLayout, 6, 0, 1, 3)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.reportButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.reportButton.setFont(font)
        self.reportButton.setStyleSheet("")
        self.reportButton.setObjectName("reportButton")
        self.verticalLayout_2.addWidget(self.reportButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "导出报告"))
        self.titleEdit.setPlaceholderText(_translate("Dialog", "标题"))
        self.appearanceBox.setText(_translate("Dialog", "影像所见"))
        self.diagnosisBox.setText(_translate("Dialog", "诊断意见"))
        self.subtitleEdit.setPlaceholderText(_translate("Dialog", "副标题"))
        self.label_13.setText(_translate("Dialog", "报告时间"))
        self.label_15.setText(_translate("Dialog", "标题"))
        self.label_17.setText(_translate("Dialog", "副标题"))
        self.noduleTableBox.setText(_translate("Dialog", "结节表格"))
        self.noduleImgBox.setText(_translate("Dialog", "结节图片"))
        self.footerBox.setText(_translate("Dialog", "页尾信息"))
        self.patientInfoBox.setText(_translate("Dialog", "病人信息"))
        self.addButton.setText(_translate("Dialog", "添加"))
        self.changeButton.setText(_translate("Dialog", "修改"))
        self.deleteButton.setText(_translate("Dialog", "删除"))
        self.listWidget.setSortingEnabled(False)
        self.reportButton.setText(_translate("Dialog", "导出"))
