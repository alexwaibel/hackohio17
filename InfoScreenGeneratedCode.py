# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Owner\PycharmProjects\HackOhio17\LoginPopup.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_infoScreen(object):
    def setupUi(self, infoScreen):
        infoScreen.setObjectName("infoScreen")
        infoScreen.resize(599, 385)
        self.verticalLayout = QtWidgets.QVBoxLayout(infoScreen)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(infoScreen)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.title.setFont(font)
        self.title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title.setStyleSheet("")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.redditFrame = QtWidgets.QFrame(infoScreen)
        self.redditFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.redditFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.redditFrame.setObjectName("redditFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.redditFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.redditLbl_2 = QtWidgets.QLabel(self.redditFrame)
        self.redditLbl_2.setMinimumSize(QtCore.QSize(100, 0))
        self.redditLbl_2.setStyleSheet("QLabel {font-size: 15pt; font-family: Segoe UI }")
        self.redditLbl_2.setObjectName("redditLbl_2")
        self.horizontalLayout_2.addWidget(self.redditLbl_2)
        self.redditInfo_2 = QtWidgets.QFormLayout()
        self.redditInfo_2.setContentsMargins(0, -1, 0, -1)
        self.redditInfo_2.setHorizontalSpacing(63)
        self.redditInfo_2.setObjectName("redditInfo_2")
        self.redditClientID_2 = QtWidgets.QLabel(self.redditFrame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.redditClientID_2.setFont(font)
        self.redditClientID_2.setObjectName("redditClientID_2")
        self.redditInfo_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.redditClientID_2)
        self.redditClientIDEntry_2 = QtWidgets.QLineEdit(self.redditFrame)
        self.redditClientIDEntry_2.setMaximumSize(QtCore.QSize(160, 16777215))
        self.redditClientIDEntry_2.setText("")
        self.redditClientIDEntry_2.setObjectName("redditClientIDEntry_2")
        self.redditInfo_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.redditClientIDEntry_2)
        self.redditClientSecret_2 = QtWidgets.QLabel(self.redditFrame)
        self.redditClientSecret_2.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.redditClientSecret_2.setFont(font)
        self.redditClientSecret_2.setObjectName("redditClientSecret_2")
        self.redditInfo_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.redditClientSecret_2)
        self.redditClientSecretEntry_2 = QtWidgets.QLineEdit(self.redditFrame)
        self.redditClientSecretEntry_2.setMaximumSize(QtCore.QSize(160, 16777215))
        self.redditClientSecretEntry_2.setText("")
        self.redditClientSecretEntry_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.redditClientSecretEntry_2.setObjectName("redditClientSecretEntry_2")
        self.redditInfo_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.redditClientSecretEntry_2)
        self.redditUser_2 = QtWidgets.QLabel(self.redditFrame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.redditUser_2.setFont(font)
        self.redditUser_2.setObjectName("redditUser_2")
        self.redditInfo_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.redditUser_2)
        self.redditUserEntry_2 = QtWidgets.QLineEdit(self.redditFrame)
        self.redditUserEntry_2.setMaximumSize(QtCore.QSize(160, 16777215))
        self.redditUserEntry_2.setObjectName("redditUserEntry_2")
        self.redditInfo_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.redditUserEntry_2)
        self.redditPass_2 = QtWidgets.QLabel(self.redditFrame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.redditPass_2.setFont(font)
        self.redditPass_2.setObjectName("redditPass_2")
        self.redditInfo_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.redditPass_2)
        self.redditPassEntry_2 = QtWidgets.QLineEdit(self.redditFrame)
        self.redditPassEntry_2.setMaximumSize(QtCore.QSize(160, 16777215))
        self.redditPassEntry_2.setText("")
        self.redditPassEntry_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.redditPassEntry_2.setObjectName("redditPassEntry_2")
        self.redditInfo_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.redditPassEntry_2)
        self.horizontalLayout_2.addLayout(self.redditInfo_2)
        self.redditLbl_2.raise_()
        self.verticalLayout.addWidget(self.redditFrame)
        self.twitterFrame = QtWidgets.QFrame(infoScreen)
        self.twitterFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.twitterFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.twitterFrame.setObjectName("twitterFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.twitterFrame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.twitterLbl = QtWidgets.QLabel(self.twitterFrame)
        self.twitterLbl.setMinimumSize(QtCore.QSize(100, 0))
        self.twitterLbl.setStyleSheet("QLabel {font-size: 15pt; font-family: Segoe UI }")
        self.twitterLbl.setObjectName("twitterLbl")
        self.horizontalLayout_3.addWidget(self.twitterLbl)
        self.twitterInfo = QtWidgets.QFormLayout()
        self.twitterInfo.setContentsMargins(-1, -1, 0, -1)
        self.twitterInfo.setObjectName("twitterInfo")
        self.twitterConsumerKey = QtWidgets.QLabel(self.twitterFrame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.twitterConsumerKey.setFont(font)
        self.twitterConsumerKey.setObjectName("twitterConsumerKey")
        self.twitterInfo.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.twitterConsumerKey)
        self.twitterConsumerKeyEntry = QtWidgets.QLineEdit(self.twitterFrame)
        self.twitterConsumerKeyEntry.setMaximumSize(QtCore.QSize(160, 16777215))
        self.twitterConsumerKeyEntry.setObjectName("twitterConsumerKeyEntry")
        self.twitterInfo.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.twitterConsumerKeyEntry)
        self.twitterConsumerSecretEntry = QtWidgets.QLineEdit(self.twitterFrame)
        self.twitterConsumerSecretEntry.setMaximumSize(QtCore.QSize(160, 16777215))
        self.twitterConsumerSecretEntry.setText("")
        self.twitterConsumerSecretEntry.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.twitterConsumerSecretEntry.setObjectName("twitterConsumerSecretEntry")
        self.twitterInfo.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.twitterConsumerSecretEntry)
        self.twitterAccessToken = QtWidgets.QLabel(self.twitterFrame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.twitterAccessToken.setFont(font)
        self.twitterAccessToken.setObjectName("twitterAccessToken")
        self.twitterInfo.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.twitterAccessToken)
        self.twitterAccessTokenEntry = QtWidgets.QLineEdit(self.twitterFrame)
        self.twitterAccessTokenEntry.setMaximumSize(QtCore.QSize(160, 16777215))
        self.twitterAccessTokenEntry.setObjectName("twitterAccessTokenEntry")
        self.twitterInfo.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.twitterAccessTokenEntry)
        self.twitterAccessTokenSecret = QtWidgets.QLabel(self.twitterFrame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.twitterAccessTokenSecret.setFont(font)
        self.twitterAccessTokenSecret.setObjectName("twitterAccessTokenSecret")
        self.twitterInfo.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.twitterAccessTokenSecret)
        self.twitterAccessTokenSecretEntry = QtWidgets.QLineEdit(self.twitterFrame)
        self.twitterAccessTokenSecretEntry.setMaximumSize(QtCore.QSize(160, 16777215))
        self.twitterAccessTokenSecretEntry.setText("")
        self.twitterAccessTokenSecretEntry.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.twitterAccessTokenSecretEntry.setObjectName("twitterAccessTokenSecretEntry")
        self.twitterInfo.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.twitterAccessTokenSecretEntry)
        self.twitterConsumerSecret = QtWidgets.QLabel(self.twitterFrame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.twitterConsumerSecret.setFont(font)
        self.twitterConsumerSecret.setObjectName("twitterConsumerSecret")
        self.twitterInfo.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.twitterConsumerSecret)
        self.horizontalLayout_3.addLayout(self.twitterInfo)
        self.verticalLayout.addWidget(self.twitterFrame)
        self.doneBtn = QtWidgets.QPushButton(infoScreen)
        self.doneBtn.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.doneBtn.setFont(font)
        self.doneBtn.setTabletTracking(True)
        self.doneBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doneBtn.setStyleSheet("")
        self.doneBtn.setObjectName("doneBtn")
        self.verticalLayout.addWidget(self.doneBtn, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(infoScreen)
        self.doneBtn.clicked.connect(infoScreen.hide)
        QtCore.QMetaObject.connectSlotsByName(infoScreen)

    def retranslateUi(self, infoScreen):
        _translate = QtCore.QCoreApplication.translate
        infoScreen.setWindowTitle(_translate("infoScreen", "Dialog"))
        self.title.setText(_translate("infoScreen", "Please Enter Your Information"))
        self.redditLbl_2.setText(_translate("infoScreen", "Reddit:"))
        self.redditClientID_2.setText(_translate("infoScreen", "Client ID:"))
        self.redditClientSecret_2.setText(_translate("infoScreen", "Client Secret:"))
        self.redditUser_2.setText(_translate("infoScreen", "Username:"))
        self.redditPass_2.setText(_translate("infoScreen", "Password:"))
        self.twitterLbl.setText(_translate("infoScreen", "Twitter:"))
        self.twitterConsumerKey.setText(_translate("infoScreen", "Consumer Key:"))
        self.twitterAccessToken.setText(_translate("infoScreen", "Access Token:"))
        self.twitterAccessTokenSecret.setText(_translate("infoScreen", "Access Token Secret:"))
        self.twitterConsumerSecret.setText(_translate("infoScreen", "Consumer Secret:"))
        self.doneBtn.setText(_translate("infoScreen", "Done"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    infoScreen = QtWidgets.QDialog()
    ui = Ui_infoScreen()
    ui.setupUi(infoScreen)
    infoScreen.show()
    sys.exit(app.exec_())

