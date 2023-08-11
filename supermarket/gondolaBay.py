from PyQt5.QtWidgets import QApplication, QDialog, QStackedWidget
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
import sys


class GondolaBay(QDialog):
    def __init__(self, widget):
        super(GondolaBay, self).__init__()
        loadUi('interfaces/gondolaBay.ui', self)
        self.widget = widget
        #self.gbBack.clicked.connect(self.goToStoreView)


def main():
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    gondolaBay = GondolaBay()  #3

    widget.addWidget(gondolaBay)

    widget.setFixedWidth(1024)
    widget.setFixedHeight(768)
    widget.show()

    try:
        sys.exit(app.exec_())
    except:
        print("")


if __name__ == "__main__":
    main()