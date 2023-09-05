from PyQt5.QtWidgets import QApplication, QDialog, QStackedWidget, QHeaderView
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets

import sys



class GondolaBay(QDialog):
    def __init__(self, widget):
        super(GondolaBay, self).__init__()
        loadUi('interfaces/gondolaBay.ui', self)
        self.widget = widget

        header = self.gondolaProductTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)

        self.gbBack.clicked.connect(self.goToStoreView)


    def goToStoreView(self):
        self.widget.setCurrentIndex(2)



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
