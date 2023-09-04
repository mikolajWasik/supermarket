from PyQt5.QtWidgets import QApplication, QDialog, QStackedWidget
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
import sys



class ShoppingList(QDialog):
    def __init__(self, widget):
        super(ShoppingList, self).__init__()
        loadUi('interfaces/shoppingList.ui', self)
        self.widget = widget
        #self.addAccept.clicked.connect(self.addToList)
        #self.deleteButton.clicked.connect(self.deleteAllChecked)
        self.slBack.clicked.connect(self.goToMenu)
        self.saveList.clicked.connect(self.saveList)

    def addToList(self):
        pass

    def deleteAllChecked(self):
        pass

    def goToMenu(self):
        self.widget.setCurrentIndex(0)

    def saveList(self):
        pass



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
