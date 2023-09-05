from PyQt5.QtWidgets import QApplication, QDialog, QStackedWidget, QTableWidgetItem, QHeaderView, QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets

import sys
import sqlite3 as sql



class StoreView(QDialog):
    def __init__(self, widget):
        super(StoreView, self).__init__()
        loadUi('interfaces/storeView.ui', self)
        self.widget = widget
        for i in range(1,31):
            eval(f"self.gb{i}").clicked.connect(lambda x, i=i: self.goToGondolaBay(i))
        self.svBack.clicked.connect(self.goToMenu)


    def getGondolaBay(self, gondolaBay):
        self.gondolaBay = gondolaBay


    def goToGondolaBay(self, gondolaBayId):
        header = self.gondolaBay.gondolaProductTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)

        self.gondolaBay.windowHeader.setText(f"Gondola bay {gondolaBayId} contents:")
        con = sql.connect('supermarket.db')
        cur = con.cursor()
        query = cur.execute(f"SELECT name, cost FROM products WHERE gondolaBayID = {gondolaBayId}")
        products = [prod for prod in query]
        self.gondolaBay.gondolaProductTable.setRowCount(len(products))
        for i in range(len(products)):
            self.gondolaBay.gondolaProductTable.setItem(i, 0, QTableWidgetItem(str(products[i][0])))
            self.gondolaBay.gondolaProductTable.setItem(i, 1, QTableWidgetItem(str(products[i][1])))
        con.close()

        self.widget.setCurrentIndex(3)


    def goToMenu(self):
        self.widget.setCurrentIndex(0)



def main():
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    storeView = StoreView()  #2
    widget.addWidget(storeView)

    widget.setFixedWidth(1024)
    widget.setFixedHeight(768)
    widget.show()

    try:
        sys.exit(app.exec_())
    except:
        print("")



if __name__ == "__main__":
    main()
