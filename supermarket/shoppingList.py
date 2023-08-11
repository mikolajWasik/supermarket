from PyQt5.QtWidgets import QApplication, QDialog, QStackedWidget
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
import sys


class ShoppingList(QDialog):
    def __init__(self, widget):
        super(ShoppingList, self).__init__()
        loadUi('interfaces/shoppingList.ui', self)
        self.widget = widget
        #self.deleteButton.clicked.connect(self.deleteAllChecked)
        #self.slBack.clicked.connect(self.goToMenu)


def main():
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    shoppingList = ShoppingList()  #1

    widget.addWidget(shoppingList)

    widget.setFixedWidth(1024)
    widget.setFixedHeight(768)
    widget.show()

    try:
        sys.exit(app.exec_())
    except:
        print("")


if __name__ == "__main__":
    main()
