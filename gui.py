import sys
from PyQt5 import QtWidgets
import GeneratedCode
import InfoScreenGeneratedCode


class InfoScreen(QtWidgets.QDialog):

    def __init__(self):
        super(InfoScreen, self).__init__()
        self.ui = InfoScreenGeneratedCode.Ui_infoScreen()
        self.ui.setupUi(self)


class ApplicationWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = GeneratedCode.Ui_mainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    infoScreen = InfoScreen()
    infoScreen.show()
    if infoScreen.exec_():
        sys.exit(-1)
    main = ApplicationWindow()
    main.show()
    sys.exit(app.exec_())
