# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kayitlar.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(500, 300))
        MainWindow.setMaximumSize(QtCore.QSize(500, 300))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.kayitlar_textedit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.kayitlar_textedit.setGeometry(QtCore.QRect(10, 30, 481, 261))
        self.kayitlar_textedit.setReadOnly(True)
        self.kayitlar_textedit.setPlainText("")
        self.kayitlar_textedit.setObjectName("kayitlar_textedit")
        self.kayitlar_label = QtWidgets.QLabel(self.centralwidget)
        self.kayitlar_label.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.kayitlar_label.setObjectName("kayitlar_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowIcon(QtGui.QIcon('logo.ico'))
        MainWindow.setWindowTitle(_translate("MainWindow", "Kayıtlar"))
        self.kayitlar_label.setText(_translate("MainWindow", "Kayıtlar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
