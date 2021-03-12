from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.sizePolicy.setHorizontalStretch(100)
        self.sizePolicy.setVerticalStretch(100)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setSizePolicy(self.sizePolicy)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.url_input = QtWidgets.QTextEdit(self.centralwidget)
        self.url_input.setGeometry(QtCore.QRect(40, 10, 1200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.url_input.setFont(font)
        self.url_input.setObjectName("url_input")

        self.page_view = QWebEngineView(self.centralwidget)
        self.page_view.setGeometry(QtCore.QRect(40, 50, 1200, 771))
        self.page_view.setObjectName("page_view")
        self.page_view.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1140, 10, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1127, 21))
        self.menuBar.setObjectName("menuBar")

        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")

        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")

        self.menuHistory = QtWidgets.QMenu(self.menuBar)
        self.menuHistory.setObjectName("menuHistory")
        MainWindow.setMenuBar(self.menuBar)
        self.actionNew_Tab = QtWidgets.QAction(MainWindow)
        self.actionNew_Tab.setObjectName("actionNew_Tab")

        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")

        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.menuFile.addAction(self.actionNew_Tab)
        self.menuFile.addAction(self.actionExit)

        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuHistory.menuAction())



        self.pushButton.clicked.connect(lambda: self.get_page(self.url_input))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Browser"))
        self.pushButton.setText(_translate("MainWindow", "Open"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHistory.setTitle(_translate("MainWindow", "History"))

        self.actionNew_Tab.setText(_translate("MainWindow", "New Tab"))
        self.actionNew_Tab.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


    def get_page(self, address):
        url = f"https://{address.toPlainText()}"
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
