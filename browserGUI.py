from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *



class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1127, 904)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.url_input = QtWidgets.QTextEdit(self.centralwidget)
        self.url_input.setGeometry(QtCore.QRect(30, 10, 881, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.url_input.setFont(font)
        self.url_input.setObjectName("url_input")


        self.page_view = QWebEngineView(self.centralwidget)
        self.page_view.setGeometry(QtCore.QRect(30, 50, 981, 771))
        self.page_view.setObjectName("page_view")


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(910, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton.clicked.connect(lambda: self.get_page(self.url_input))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Browser"))
        self.pushButton.setText(_translate("MainWindow", "Open"))

    def get_page(self, address):
        url = f"https://www.{address.toPlainText()}"
        self.browser = QWebEnginePage()
        self.browser.setUrl(QUrl(url))
        self.page_view.setPage(self.browser)






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
