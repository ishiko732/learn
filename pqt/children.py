# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'children.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_ChildrenForm(object):
    def setupUi(self, ChildrenForm):
        ChildrenForm.setObjectName("ChildrenForm")
        ChildrenForm.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ChildrenForm)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(120, 40, 601, 431))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.MaingridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.MaingridLayout.setContentsMargins(0, 0, 0, 0)
        self.MaingridLayout.setObjectName("MaingridLayout")
        ChildrenForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ChildrenForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        ChildrenForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ChildrenForm)
        self.statusbar.setObjectName("statusbar")
        ChildrenForm.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(ChildrenForm)
        self.toolBar.setObjectName("toolBar")
        ChildrenForm.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.fileOpenAction = QtWidgets.QAction(ChildrenForm)
        self.fileOpenAction.setObjectName("fileOpenAction")
        self.addWinAction = QtWidgets.QAction(ChildrenForm)
        self.addWinAction.setObjectName("addWinAction")
        self.fileNewAction = QtWidgets.QAction(ChildrenForm)
        self.fileNewAction.setObjectName("fileNewAction")
        self.fileCloseAction = QtWidgets.QAction(ChildrenForm)
        self.fileCloseAction.setObjectName("fileCloseAction")
        self.menu.addAction(self.fileOpenAction)
        self.menu.addAction(self.fileNewAction)
        self.menu.addAction(self.fileCloseAction)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.toolBar.addAction(self.addWinAction)

        self.retranslateUi(ChildrenForm)
        QtCore.QMetaObject.connectSlotsByName(ChildrenForm)

    def retranslateUi(self, ChildrenForm):
        _translate = QtCore.QCoreApplication.translate
        ChildrenForm.setWindowTitle(_translate("ChildrenForm", "MainWindow"))
        self.menu.setTitle(_translate("ChildrenForm", "文件"))
        self.menu_2.setTitle(_translate("ChildrenForm", "编辑"))
        self.toolBar.setWindowTitle(_translate("ChildrenForm", "toolBar"))
        self.fileOpenAction.setText(_translate("ChildrenForm", "Open"))
        self.fileOpenAction.setShortcut(_translate("ChildrenForm", "Alt+S"))
        self.addWinAction.setText(_translate("ChildrenForm", "添加窗体"))
        self.addWinAction.setToolTip(_translate("ChildrenForm", "添加窗体"))
        self.fileNewAction.setText(_translate("ChildrenForm", "New"))
        self.fileNewAction.setShortcut(_translate("ChildrenForm", "Alt+N"))
        self.fileCloseAction.setText(_translate("ChildrenForm", "Close"))
        self.fileCloseAction.setShortcut(_translate("ChildrenForm", "Alt+C"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChildrenForm = QtWidgets.QMainWindow()
    ui = Ui_ChildrenForm()
    ui.setupUi(ChildrenForm)
    ChildrenForm.show()
    sys.exit(app.exec_())
