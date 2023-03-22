from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog



class Register_Dialog_UI(QDialog):

    def __init__(self, parent=None):
        super(Register_Dialog_UI, self).__init__(parent)
        self.setupUi(self)


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(525, 700)
        Dialog.setMinimumSize(QtCore.QSize(525, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\Administrator\\Downloads\\Login_PyQt5-master\\Images/Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("color: rgb(200, 200, 200);\n"
"background-color: rgb(10, 10, 10);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_3 = QtWidgets.QFrame(self.widget)
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
        self.formLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.formLayout_2.setVerticalSpacing(30)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_10 = QtWidgets.QLabel(self.login_area_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(0, 33))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.usernameEdit = QtWidgets.QLineEdit(self.login_area_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.usernameEdit.setFont(font)
        self.usernameEdit.setStyleSheet("QLineEdit {\n"
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
        self.usernameEdit.setText("")
        self.usernameEdit.setMaxLength(32)
        self.usernameEdit.setObjectName("usernameEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usernameEdit)
        self.label_11 = QtWidgets.QLabel(self.login_area_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(0, 33))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.passwordEidt = QtWidgets.QLineEdit(self.login_area_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.passwordEidt.setFont(font)
        self.passwordEidt.setStyleSheet("QLineEdit {\n"
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
        self.passwordEidt.setMaxLength(16)
        self.passwordEidt.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEidt.setObjectName("passwordEidt")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwordEidt)
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
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
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
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_13)
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
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.birthdayEdit)
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
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_14)
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
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.phoneEdit)
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
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.mailEdit = QtWidgets.QLineEdit(self.login_area_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.mailEdit.setFont(font)
        self.mailEdit.setStyleSheet("QLineEdit {\n"
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
        self.mailEdit.setText("")
        self.mailEdit.setMaxLength(32)
        self.mailEdit.setObjectName("mailEdit")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.mailEdit)
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
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.frame_4)
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
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.departmentEdit = QtWidgets.QLineEdit(self.login_area_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.departmentEdit.setFont(font)
        self.departmentEdit.setStyleSheet("QLineEdit {\n"
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
        self.departmentEdit.setText("")
        self.departmentEdit.setMaxLength(32)
        self.departmentEdit.setObjectName("departmentEdit")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.departmentEdit)
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
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_17)
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
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.nameEdit)
        self.label_18 = QtWidgets.QLabel(self.login_area_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMinimumSize(QtCore.QSize(0, 33))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.positionEdit = QtWidgets.QLineEdit(self.login_area_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.positionEdit.setFont(font)
        self.positionEdit.setStyleSheet("QLineEdit {\n"
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
        self.positionEdit.setText("")
        self.positionEdit.setMaxLength(32)
        self.positionEdit.setObjectName("positionEdit")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.positionEdit)
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
        self.verticalLayout_5.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.usernameEdit, self.passwordEidt)
        Dialog.setTabOrder(self.passwordEidt, self.nameEdit)
        Dialog.setTabOrder(self.nameEdit, self.MaleButton)
        Dialog.setTabOrder(self.MaleButton, self.FemaleButton)
        Dialog.setTabOrder(self.FemaleButton, self.birthdayEdit)
        Dialog.setTabOrder(self.birthdayEdit, self.phoneEdit)
        Dialog.setTabOrder(self.phoneEdit, self.mailEdit)
        Dialog.setTabOrder(self.mailEdit, self.departmentEdit)
        Dialog.setTabOrder(self.departmentEdit, self.positionEdit)
        Dialog.setTabOrder(self.positionEdit, self.registerButton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "注册"))
        self.label_10.setText(_translate("Dialog", "用户名"))
        self.usernameEdit.setPlaceholderText(_translate("Dialog", "用户名"))
        self.label_11.setText(_translate("Dialog", "密码"))
        self.passwordEidt.setPlaceholderText(_translate("Dialog", "密码"))
        self.label_12.setText(_translate("Dialog", "性别"))
        self.label_13.setText(_translate("Dialog", "生日"))
        self.label_14.setText(_translate("Dialog", "电话"))
        self.phoneEdit.setPlaceholderText(_translate("Dialog", "电话"))
        self.label_15.setText(_translate("Dialog", "邮箱"))
        self.mailEdit.setPlaceholderText(_translate("Dialog", "邮箱"))
        self.MaleButton.setText(_translate("Dialog", "男性"))
        self.FemaleButton.setText(_translate("Dialog", "女性"))
        self.label_16.setText(_translate("Dialog", "机构"))
        self.departmentEdit.setPlaceholderText(_translate("Dialog", "机构"))
        self.label_17.setText(_translate("Dialog", "姓名"))
        self.nameEdit.setPlaceholderText(_translate("Dialog", "姓名"))
        self.label_18.setText(_translate("Dialog", "职位"))
        self.positionEdit.setPlaceholderText(_translate("Dialog", "职位"))
        self.registerButton.setText(_translate("Dialog", "注册"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Register_Dialog_UI()
    ui.show()
    sys.exit(app.exec_())
