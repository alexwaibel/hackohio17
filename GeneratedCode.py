# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Owner\Documents\Github\HackOhio17\HackOhio17UI.ui'
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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.movieTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.movieTab)
        self.listWidget.setStyleSheet("QListWidget::item {border-bottom: 1px solid black }\n"
"QListWidget::item:selected {color: black }")
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
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
        mainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(mainWindow)
        self.statusBar.setObjectName("statusBar")
        mainWindow.setStatusBar(self.statusBar)
        self.actionQuit = QtWidgets.QAction(mainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../PycharmProjects/HackOhio17/exit-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.actionQuit.triggered.connect(mainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Placeholder"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.musicTab), _translate("mainWindow", "Music"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.movieTab), _translate("mainWindow", "Movies"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.bookTab), _translate("mainWindow", "Books"))
        self.menuFile.setTitle(_translate("mainWindow", "File"))
        self.actionQuit.setText(_translate("mainWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

