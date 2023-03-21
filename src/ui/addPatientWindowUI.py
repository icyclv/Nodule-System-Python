# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\a_bishe\code\Nodule-System-Python\src\ui\file\add_patient.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class AddPatientWindowUI(QMainWindow):
    def __init__(self):
        super(AddPatientWindowUI, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(552, 530)
        MainWindow.setStyleSheet("color: rgb(200, 200, 200);\n"
                                 "background-color: rgb(20, 20, 20);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("color: rgb(200, 200, 200);\n"
                                         "background-color: rgb(10, 10, 10);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setStyleSheet("border-radius: 10px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.login_area_2 = QtWidgets.QFrame(self.frame_3)
        self.login_area_2.setMaximumSize(QtCore.QSize(500, 600))
        self.login_area_2.setStyleSheet("border-radius: 10px;")
        self.login_area_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login_area_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_area_2.setObjectName("login_area_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.login_area_2)
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(-1, 6, -1, 6)
        self.formLayout_2.setVerticalSpacing(30)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_17 = QtWidgets.QLabel(self.login_area_2)
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
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.nameEdit = QtWidgets.QLineEdit(self.login_area_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.nameEdit.setFont(font)
        self.nameEdit.setStyleSheet("QLineEdit {\n"
                                    "    border: 2px solid rgb(45, 45, 45);\n"
                                    "    border-radius: 5px;\n"
                                    "    padding: 5px;\n"
                                    "    background-color: rgb(30, 30, 30);    \n"
                                    "    color: rgb(100, 100, 100);\n"
                                    "}\n"
                                    "QLineEdit:hover {\n"
                                    "    border: 2px solid rgb(55, 55, 55);\n"
                                    "}\n"
                                    "QLineEdit:focus {\n"
                                    "    border: 2px solid rgb(170, 255, 255);    \n"
                                    "    color: rgb(200, 200, 200);\n"
                                    "}")
        self.nameEdit.setText("")
        self.nameEdit.setMaxLength(32)
        self.nameEdit.setObjectName("nameEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameEdit)
        self.label_12 = QtWidgets.QLabel(self.login_area_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(0, 33))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.frame_4 = QtWidgets.QFrame(self.login_area_2)
        self.frame_4.setStyleSheet("QFrame {\n"
                                   "    border: 2px solid rgb(45, 45, 45);\n"
                                   "    border-radius: 5px;\n"
                                   "    background-color: rgb(30, 30, 30);    \n"
                                   "    color: rgb(100, 100, 100);\n"
                                   "}\n"
                                   "")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setLineWidth(5)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.MaleButton = QtWidgets.QRadioButton(self.frame_4)
        self.MaleButton.setStyleSheet("QRadioButton {\n"
                                      "    background-color: rgb(30, 30, 30);    \n"
                                      "    color: rgb(100, 100, 100);\n"
                                      "}\n"
                                      "")
        self.MaleButton.setCheckable(True)
        self.MaleButton.setChecked(True)
        self.MaleButton.setObjectName("MaleButton")
        self.horizontalLayout_8.addWidget(self.MaleButton)
        self.FemaleButton = QtWidgets.QRadioButton(self.frame_4)
        self.FemaleButton.setStyleSheet("QRadioButton {\n"
                                        "    background-color: rgb(30, 30, 30);    \n"
                                        "    color: rgb(100, 100, 100);\n"
                                        "}\n"
                                        "r")
        self.FemaleButton.setObjectName("FemaleButton")
        self.horizontalLayout_8.addWidget(self.FemaleButton)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.frame_4)
        self.label_13 = QtWidgets.QLabel(self.login_area_2)
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
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.birthdayEdit = QtWidgets.QDateEdit(self.login_area_2)
        self.birthdayEdit.setMinimumSize(QtCore.QSize(0, 33))
        self.birthdayEdit.setStyleSheet("QLineEdit {\n"
                                        "    border: 2px solid rgb(45, 45, 45);\n"
                                        "    border-radius: 5px;\n"
                                        "    padding: 5px;\n"
                                        "    background-color: rgb(30, 30, 30);    \n"
                                        "    color: rgb(100, 100, 100);\n"
                                        "}\n"
                                        "QLineEdit:hover {\n"
                                        "    border: 2px solid rgb(55, 55, 55);\n"
                                        "}\n"
                                        "QLineEdit:focus {\n"
                                        "    border: 2px solid rgb(170, 255, 255);    \n"
                                        "    color: rgb(200, 200, 200);\n"
                                        "}")
        self.birthdayEdit.setCalendarPopup(True)
        self.birthdayEdit.setObjectName("birthdayEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.birthdayEdit)
        self.label_14 = QtWidgets.QLabel(self.login_area_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QtCore.QSize(0, 33))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.phoneEdit = QtWidgets.QLineEdit(self.login_area_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.phoneEdit.setFont(font)
        self.phoneEdit.setStyleSheet("QLineEdit {\n"
                                     "    border: 2px solid rgb(45, 45, 45);\n"
                                     "    border-radius: 5px;\n"
                                     "    padding: 5px;\n"
                                     "    background-color: rgb(30, 30, 30);    \n"
                                     "    color: rgb(100, 100, 100);\n"
                                     "}\n"
                                     "QLineEdit:hover {\n"
                                     "    border: 2px solid rgb(55, 55, 55);\n"
                                     "}\n"
                                     "QLineEdit:focus {\n"
                                     "    border: 2px solid rgb(170, 255, 255);    \n"
                                     "    color: rgb(200, 200, 200);\n"
                                     "}")
        self.phoneEdit.setText("")
        self.phoneEdit.setMaxLength(32)
        self.phoneEdit.setObjectName("phoneEdit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.phoneEdit)
        self.label_15 = QtWidgets.QLabel(self.login_area_2)
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
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.addressEdit = QtWidgets.QLineEdit(self.login_area_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.addressEdit.setFont(font)
        self.addressEdit.setStyleSheet("QLineEdit {\n"
                                       "    border: 2px solid rgb(45, 45, 45);\n"
                                       "    border-radius: 5px;\n"
                                       "    padding: 5px;\n"
                                       "    background-color: rgb(30, 30, 30);    \n"
                                       "    color: rgb(100, 100, 100);\n"
                                       "}\n"
                                       "QLineEdit:hover {\n"
                                       "    border: 2px solid rgb(55, 55, 55);\n"
                                       "}\n"
                                       "QLineEdit:focus {\n"
                                       "    border: 2px solid rgb(170, 255, 255);    \n"
                                       "    color: rgb(200, 200, 200);\n"
                                       "}")
        self.addressEdit.setText("")
        self.addressEdit.setMaxLength(32)
        self.addressEdit.setObjectName("addressEdit")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.addressEdit)
        self.label_16 = QtWidgets.QLabel(self.login_area_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMinimumSize(QtCore.QSize(0, 33))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.backupEdit = QtWidgets.QPlainTextEdit(self.login_area_2)
        self.backupEdit.setStyleSheet("QPlainTextEdit {\n"
                                      "    border: 2px solid rgb(45, 45, 45);\n"
                                      "    border-radius: 5px;\n"
                                      "    padding: 5px;\n"
                                      "    background-color: rgb(30, 30, 30);    \n"
                                      "    color: rgb(100, 100, 100);\n"
                                      "}\n"
                                      "QPlainTextEdit:hover {\n"
                                      "    border: 2px solid rgb(55, 55, 55);\n"
                                      "}\n"
                                      "QPlainTextEdit:focus {\n"
                                      "    border: 2px solid rgb(170, 255, 255);    \n"
                                      "    color: rgb(200, 200, 200);\n"
                                      "}")
        self.backupEdit.setObjectName("backupEdit")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.backupEdit)
        self.verticalLayout_4.addLayout(self.formLayout_2)
        self.registerButton = QtWidgets.QPushButton(self.login_area_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.registerButton.setFont(font)
        self.registerButton.setStyleSheet("QPushButton {    \n"
                                          "    background-color: rgb(50, 50, 50);\n"
                                          "    border: 2px solid rgb(60, 60, 60);\n"
                                          "    border-radius: 5px;\n"
                                          "}\n"
                                          "QPushButton:hover {    \n"
                                          "    background-color: rgb(60, 60, 60);\n"
                                          "    border: 2px solid rgb(70, 70, 70);\n"
                                          "}\n"
                                          "QPushButton:pressed {    \n"
                                          "    background-color: rgb(170, 255, 255);\n"
                                          "    border: 2px solid rgb(255, 165, 24);    \n"
                                          "    color: rgb(35, 35, 35);\n"
                                          "}")
        self.registerButton.setObjectName("registerButton")
        self.verticalLayout_4.addWidget(self.registerButton)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout_6.addWidget(self.login_area_2)
        self.verticalLayout.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 552, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menu)
        self.menu_2.setGeometry(QtCore.QRect(616, 390, 163, 72))
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.DICOMaction = QtWidgets.QAction(MainWindow)
        self.DICOMaction.setObjectName("DICOMaction")
        self.menu_2.addAction(self.DICOMaction)
        self.menu.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "添加患者"))
        self.label_17.setText(_translate("MainWindow", "姓名"))
        self.nameEdit.setPlaceholderText(_translate("MainWindow", "姓名"))
        self.label_12.setText(_translate("MainWindow", "性别"))
        self.MaleButton.setText(_translate("MainWindow", "男性"))
        self.FemaleButton.setText(_translate("MainWindow", "女性"))
        self.label_13.setText(_translate("MainWindow", "生日"))
        self.label_14.setText(_translate("MainWindow", "电话"))
        self.phoneEdit.setPlaceholderText(_translate("MainWindow", "电话"))
        self.label_15.setText(_translate("MainWindow", "地址"))
        self.addressEdit.setPlaceholderText(_translate("MainWindow", "地址"))
        self.label_16.setText(_translate("MainWindow", "备注"))
        self.registerButton.setText(_translate("MainWindow", "添加"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.menu_2.setTitle(_translate("MainWindow", "导入信息"))
        self.DICOMaction.setText(_translate("MainWindow", "由DICOM文件导入"))