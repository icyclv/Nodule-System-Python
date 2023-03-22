# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\a_bishe\code\Nodule-System-Python\client\ui\file\CadWindowUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import qdarkstyle
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow


class CadWindowUI(QMainWindow):
    def __init__(self):
        super(CadWindowUI, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)

        self.display_dialog = None
        # ColumnWidth of Patient List

        self.noduletreeWidget.setColumnWidth(0, 100)
        self.noduletreeWidget.setColumnWidth(1, 150)
        self.noduletreeWidget.setColumnWidth(2, 100)
        self.noduletreeWidget.setColumnWidth(3, 150)
        self.noduletreeWidget.setColumnWidth(4, 150)
        self.noduletreeWidget.setColumnWidth(5, 150)
        self.noduletreeWidget.setColumnWidth(6, 150)
        self.noduletreeWidget.setColumnWidth(7, 100)
        self.noduletreeWidget.setColumnHidden(7,True)
        # self.noduletreeWidget.header().setSectionResizeMode(QHeaderView.Stretch)
        # self.noduletreeWidget.header().setSectionResizeMode(QHeaderView.Interactive)

        self.treeWidget.setColumnWidth(0, 100)
        self.treeWidget.setColumnWidth(1, 70)
        self.treeWidget.setColumnWidth(2, 150)
        self.treeWidget.setColumnWidth(3, 150)
        self.treeWidget.setColumnWidth(4, 400)
        self.treeWidget.setColumnWidth(5, 70)
        # ColumnWidth of Scan and Nodule List

        # self.noduletreeWidget.setColumnWidth(8, 100)
        self.preferences_dialog = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 695)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget = QtWidgets.QWidget(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchEdit = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchEdit.sizePolicy().hasHeightForWidth())
        self.searchEdit.setSizePolicy(sizePolicy)
        self.searchEdit.setStyleSheet("QLineEdit {\n"
                                      "    border-radius: 5px;\n"
                                      "}")
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout.addWidget(self.searchEdit)
        self.searchButton = QtWidgets.QPushButton(self.widget)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout.addWidget(self.searchButton)
        self.horizontalLayout_3.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addUserButton = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.addUserButton.sizePolicy().hasHeightForWidth())
        self.addUserButton.setSizePolicy(sizePolicy)
        self.addUserButton.setObjectName("addUserButton")
        self.horizontalLayout_2.addWidget(self.addUserButton)
        self.loadDicomButton = QtWidgets.QPushButton(self.widget_2)
        self.loadDicomButton.setObjectName("loadDicomButton")
        self.horizontalLayout_2.addWidget(self.loadDicomButton)
        self.displayButton = QtWidgets.QPushButton(self.widget_2)
        self.displayButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.displayButton.setObjectName("displayButton")
        self.horizontalLayout_2.addWidget(self.displayButton)
        self.horizontalLayout_3.addWidget(self.widget_2)
        self.gridLayout.addWidget(self.widget_3, 0, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget_4 = QtWidgets.QWidget(self.splitter)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.widget_4)
        self.treeWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.treeWidget.setProperty("showDropIndicator", True)
        self.treeWidget.setAutoExpandDelay(-1)
        self.treeWidget.setIndentation(20)
        self.treeWidget.setRootIsDecorated(False)
        self.treeWidget.setUniformRowHeights(True)
        self.treeWidget.setItemsExpandable(True)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setWordWrap(True)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.setExpandsOnDoubleClick(True)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(1, QtCore.Qt.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(2, QtCore.Qt.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(3, QtCore.Qt.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(4, QtCore.Qt.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(5, QtCore.Qt.AlignCenter)
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setDefaultSectionSize(100)
        self.treeWidget.header().setMinimumSectionSize(50)
        self.treeWidget.header().setSortIndicatorShown(False)
        self.treeWidget.header().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.treeWidget)
        self.widget_5 = QtWidgets.QWidget(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setContentsMargins(-1, 3, -1, 3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.widget_5)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.totalPageLabel = QtWidgets.QLabel(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.totalPageLabel.sizePolicy().hasHeightForWidth())
        self.totalPageLabel.setSizePolicy(sizePolicy)
        self.totalPageLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.totalPageLabel.setObjectName("totalPageLabel")
        self.horizontalLayout_5.addWidget(self.totalPageLabel)
        self.prePageButton = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.prePageButton.sizePolicy().hasHeightForWidth())
        self.prePageButton.setSizePolicy(sizePolicy)
        self.prePageButton.setMinimumSize(QtCore.QSize(75, 0))
        self.prePageButton.setObjectName("prePageButton")
        self.horizontalLayout_5.addWidget(self.prePageButton)
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.currentPageEdit = QtWidgets.QLineEdit(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.currentPageEdit.sizePolicy().hasHeightForWidth())
        self.currentPageEdit.setSizePolicy(sizePolicy)
        self.currentPageEdit.setMinimumSize(QtCore.QSize(50, 0))
        self.currentPageEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.currentPageEdit.setObjectName("currentPageEdit")
        self.horizontalLayout_4.addWidget(self.currentPageEdit)
        self.label_3 = QtWidgets.QLabel(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_5.addWidget(self.widget_6)
        self.nextPageButton = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.nextPageButton.sizePolicy().hasHeightForWidth())
        self.nextPageButton.setSizePolicy(sizePolicy)
        self.nextPageButton.setMinimumSize(QtCore.QSize(75, 0))
        self.nextPageButton.setObjectName("nextPageButton")
        self.horizontalLayout_5.addWidget(self.nextPageButton)
        self.label_5 = QtWidgets.QLabel(self.widget_5)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.verticalLayout.addWidget(self.widget_5)
        self.line = QtWidgets.QFrame(self.widget_4)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.noduletreeWidget = QtWidgets.QTreeWidget(self.splitter)
        self.noduletreeWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.noduletreeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.noduletreeWidget.setProperty("showDropIndicator", True)
        self.noduletreeWidget.setAutoExpandDelay(-1)
        self.noduletreeWidget.setIndentation(20)
        self.noduletreeWidget.setRootIsDecorated(True)
        self.noduletreeWidget.setUniformRowHeights(True)
        self.noduletreeWidget.setItemsExpandable(True)
        self.noduletreeWidget.setAnimated(True)
        self.noduletreeWidget.setWordWrap(True)
        self.noduletreeWidget.setObjectName("noduletreeWidget")
        self.noduletreeWidget.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        self.noduletreeWidget.headerItem().setTextAlignment(1, QtCore.Qt.AlignCenter)
        self.noduletreeWidget.headerItem().setTextAlignment(2, QtCore.Qt.AlignCenter)
        self.noduletreeWidget.headerItem().setTextAlignment(3, QtCore.Qt.AlignCenter)
        self.noduletreeWidget.headerItem().setTextAlignment(4, QtCore.Qt.AlignCenter)
        self.noduletreeWidget.headerItem().setTextAlignment(5, QtCore.Qt.AlignCenter)
        self.noduletreeWidget.headerItem().setTextAlignment(6, QtCore.Qt.AlignCenter)
        self.noduletreeWidget.headerItem().setTextAlignment(7, QtCore.Qt.AlignCenter)
        self.noduletreeWidget.header().setVisible(True)
        self.noduletreeWidget.header().setCascadingSectionResizes(False)
        self.noduletreeWidget.header().setDefaultSectionSize(120)
        self.noduletreeWidget.header().setMinimumSectionSize(50)
        self.noduletreeWidget.header().setSortIndicatorShown(False)
        self.noduletreeWidget.header().setStretchLastSection(True)
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 23))
        self.menubar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.menubar.setObjectName("menubar")
        self.menuNodule_CADx = QtWidgets.QMenu(self.menubar)
        self.menuNodule_CADx.setObjectName("menuNodule_CADx")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.action22213123 = QtWidgets.QAction(MainWindow)
        self.action22213123.setObjectName("action22213123")
        self.addUserAction = QtWidgets.QAction(MainWindow)
        self.addUserAction.setObjectName("addUserAction")
        self.menubar.addAction(self.menuNodule_CADx.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "肺结节智能分析系统"))
        self.searchEdit.setPlaceholderText(_translate("MainWindow", "姓名检索"))
        self.searchButton.setText(_translate("MainWindow", "搜索"))
        self.addUserButton.setText(_translate("MainWindow", "添加患者"))
        self.loadDicomButton.setText(_translate("MainWindow", "添加影像"))
        self.displayButton.setText(_translate("MainWindow", "查看"))
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "姓名"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "性别"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "生日"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "联系电话"))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "备注信息"))
        self.treeWidget.headerItem().setText(5, _translate("MainWindow", "操作"))
        self.totalPageLabel.setText(_translate("MainWindow", "共0条,每页10条"))
        self.prePageButton.setText(_translate("MainWindow", "上一页"))
        self.label_2.setText(_translate("MainWindow", "跳转至第"))
        self.label_3.setText(_translate("MainWindow", "页"))
        self.nextPageButton.setText(_translate("MainWindow", "下一页"))
        self.noduletreeWidget.setSortingEnabled(False)
        self.noduletreeWidget.headerItem().setText(0, _translate("MainWindow", "状态"))
        self.noduletreeWidget.headerItem().setText(1, _translate("MainWindow", "检测时间"))
        self.noduletreeWidget.headerItem().setText(2, _translate("MainWindow", "检测年龄"))
        self.noduletreeWidget.headerItem().setText(3, _translate("MainWindow", "概率"))
        self.noduletreeWidget.headerItem().setText(4, _translate("MainWindow", "直径"))
        self.noduletreeWidget.headerItem().setText(5, _translate("MainWindow", "类别"))
        self.noduletreeWidget.headerItem().setText(6, _translate("MainWindow", "恶性概率"))
        self.noduletreeWidget.headerItem().setText(7, _translate("MainWindow", "信息"))
        self.menuNodule_CADx.setTitle(_translate("MainWindow", "菜单"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.action22213123.setText(_translate("MainWindow", "File"))
        self.addUserAction.setText(_translate("MainWindow", "添加患者"))

if __name__ == "__main__":

    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ui = CadWindowUI()
    ui.show()
    sys.exit(app.exec_())