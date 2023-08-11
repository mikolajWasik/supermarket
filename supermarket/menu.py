from PyQt5.QtWidgets import QApplication, QDialog, QStackedWidget
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
import sys


class Menu(QDialog):
    def __init__(self, widget, app):
        super(Menu, self).__init__()
        loadUi('interfaces/menu.ui', self)
        self.widget = widget
        self.app = app
        #self.storeViewButton.clicked.connect(self.goToStoreView)
        #self.shoppingListButton.clicked.connect(self.goToShoppingList)
        #self.exitButton.clicked.connect(self.exitApp)
        


def main():
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    menu = Menu()  #0

    widget.addWidget(menu)

    widget.setFixedWidth(1024)
    widget.setFixedHeight(768)
    widget.show()

    try:
        sys.exit(app.exec_())
    except:
        print("")


if __name__ == "__main__":
    main()
