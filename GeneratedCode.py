# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Owner\PycharmProjects\HackOhio17\HackOhio17UI.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1026, 716)
        mainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabBar::tab { height: 30px; width: 100px; font-size: 9pt }")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.musicTab = QtWidgets.QWidget()
        self.musicTab.setObjectName("musicTab")
        self.tabWidget.addTab(self.musicTab, "")
        self.movieTab = QtWidgets.QWidget()
        self.movieTab.setObjectName("movieTab")
        self.tabWidget.addTab(self.movieTab, "")
        self.bookTab = QtWidgets.QWidget()
        self.bookTab.setObjectName("bookTab")
        self.tabWidget.addTab(self.bookTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(mainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1026, 26))
        self.menuBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuLog_In = QtWidgets.QMenu(self.menuBar)
        self.menuLog_In.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.menuLog_In.setObjectName("menuLog_In")
        mainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(mainWindow)
        self.statusBar.setObjectName("statusBar")
        mainWindow.setStatusBar(self.statusBar)
        self.actionQuit = QtWidgets.QAction(mainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("exit-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuLog_In.menuAction())

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.actionQuit.triggered.connect(mainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Placeholder"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.musicTab), _translate("mainWindow", "Music"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.movieTab), _translate("mainWindow", "Movies"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.bookTab), _translate("mainWindow", "Books"))
        self.menuFile.setTitle(_translate("mainWindow", "File"))
        self.menuLog_In.setTitle(_translate("mainWindow", "Log In"))
        self.actionQuit.setText(_translate("mainWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

