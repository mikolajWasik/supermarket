from PyQt5.QtWidgets import QApplication, QDialog, QStackedWidget, QMessageBox
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
import sys



class Menu(QDialog):
    def __init__(self, widget, app):
        super(Menu, self).__init__()
        loadUi('interfaces/menu.ui', self)
        self.widget = widget
        self.app = app
        self.storeViewButton.clicked.connect(self.goToStoreView)
        self.shoppingListButton.clicked.connect(self.goToShoppingList)
        self.exitButton.clicked.connect(self.exitApp)

    def goToStoreView(self):
        self.widget.setCurrentIndex(2)

    def goToShoppingList(self):
        self.widget.setCurrentIndex(1)

    def exitApp(self):
        out = QMessageBox.question(self, 'Supermarket', "Do you want to exit the application?", QMessageBox.Yes | QMessageBox.No)
        if out == QMessageBox.No:
            return
        else:
            self.app.quit()
        


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
