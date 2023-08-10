from PyQt5.QtWidgets import QApplication, QStackedWidget
from PyQt5 import QtCore
import sys

from menu import Menu
from shoppingList import ShoppingList
from storeView import StoreView
from gondolaBay import GondolaBay



if __name__ == '__main__':
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    widget = QStackedWidget()

    menu = Menu(widget, app)  # 0
    shoppingList = ShoppingList(widget) #1
    storeView = StoreView(widget) #2
    gondolaBay = GondolaBay(widget) #3

    widget.addWidget(menu)
    widget.addWidget(shoppingList)
    widget.addWidget(storeView)
    widget.addWidget(gondolaBay)

    widget.setFixedWidth(1024)
    widget.setFixedHeight(768)
    widget.show()

    try:
        sys.exit(app.exec_())
    except:
        pass
