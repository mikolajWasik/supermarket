from PyQt5.QtWidgets import QApplication, QDialog, QStackedWidget, QMessageBox, QHeaderView, QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets

import sys
import sqlite3 as sql



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


    def getShoppingList(self, shoppingList):
        self.shoppingList = shoppingList


    def goToShoppingList(self):
        header = self.shoppingList.shoppingListTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)

        con = sql.connect('supermarket.db')
        cur = con.cursor()
        query = cur.execute("SELECT productName, quantityNeeded, done FROM shoppingList ORDER BY ID")
        products = [prod for prod in query]
        self.shoppingList.shoppingListTable.setRowCount(len(products))
        for i in range(len(products)):
            self.shoppingList.shoppingListTable.setItem(i, 0, QTableWidgetItem(str(products[i][0])))
            self.shoppingList.shoppingListTable.setItem(i, 1, QTableWidgetItem(str(products[i][1])))
            self.shoppingList.shoppingListTable.setItem(i, 2, QTableWidgetItem(str(products[i][2])))
        con.close()

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
