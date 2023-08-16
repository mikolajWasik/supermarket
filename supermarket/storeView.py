from PyQt5.QtWidgets import QApplication, QDialog, QStackedWidget
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
import sys



class StoreView(QDialog):
    def __init__(self, widget):
        super(StoreView, self).__init__()
        loadUi('interfaces/storeView.ui', self)
        self.widget = widget
        #for i in range(1,31):
        #    eval(f"self.gb{i}").clicked.connect(lambda x, i=i: self.goToGondolaBay(i))
        self.svBack.clicked.connect(self.goToMenu)

    def goToGondolaBay(self, gondolaBayId):
        pass

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
