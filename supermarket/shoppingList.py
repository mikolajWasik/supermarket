from PyQt5.QtWidgets import QApplication, QDialog, QStackedWidget, QHeaderView, QMessageBox, QInputDialog, QLineEdit, QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets

import sys
import sqlite3 as sql



class ShoppingList(QDialog):
    def __init__(self, widget):
        super(ShoppingList, self).__init__()
        loadUi('interfaces/shoppingList.ui', self)
        self.widget = widget
        self.productsForSavingList = []

        header = self.shoppingListTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)

        self.addAllProductsToComboBox()
        self.addButton.clicked.connect(self.addToList)
        #self.deleteButton.clicked.connect(self.deleteAllChecked)
        #self.saveList.clicked.connect(self.saveList)
        self.slBack.clicked.connect(self.goToMenu)


    def addAllProductsToComboBox(self):
        con = sql.connect('supermarket.db')
        cur = con.cursor()
        query = cur.execute(f"SELECT name FROM products")
        self.allProductsComboBox.addItem("Choose from list...")
        products = [prod for prod in query]
        for prod in products:
            self.allProductsComboBox.addItem(prod[0])
        con.close()


    def loadProducts(self):
        self.shoppingListTable.setRowCount(len(self.productsForSavingList))
        for i in range(len(self.productsForSavingList)):
            self.shoppingListTable.setItem(i, 0, QTableWidgetItem(str(self.productsForSavingList[i][0])))
            self.shoppingListTable.setItem(i, 1, QTableWidgetItem(str(self.productsForSavingList[i][1])))


    def addToList(self):
        product = self.allProductsComboBox.currentText()
        quantity, okPressed = QInputDialog.getText(self, "Supermarket", "Enter quantity: ", QLineEdit.Normal, "")
        if okPressed == False or quantity == '':
            return
        try:
            quantity = float(quantity)
            if quantity % 1 == 0:
                quantity = int(quantity)
        except Exception as e:
            msg = QMessageBox()
            msg.setText(f"The entered quantity is incorrect. Exception: {e}")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
            return

        self.productsForSavingList.append((product, quantity, False))
        self.loadProducts()



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
