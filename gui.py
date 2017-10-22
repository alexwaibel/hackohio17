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
        for x in range(1, 26):
            self.label = QtWidgets.QListWidgetItem()
            self.label.setText(str(x) + ".")
            self.ui.listWidget.addItem(self.label)


def main():
    app = QtWidgets.QApplication(sys.argv)
    info_screen = InfoScreen()
    info_screen.show()
    if info_screen.exec_():
        sys.exit(-1)
    main_win = ApplicationWindow()
    main_win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
