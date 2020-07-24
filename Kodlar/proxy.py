# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proxy.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_proxy_panel(object):
    def setupUi(self, proxy_panel):
        proxy_panel.setObjectName("proxy_panel")
        proxy_panel.resize(190, 120)
        proxy_panel.setMinimumSize(QtCore.QSize(190, 120))
        proxy_panel.setMaximumSize(QtCore.QSize(190, 120))
        self.centralwidget = QtWidgets.QWidget(proxy_panel)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(10, 10, 171, 17))
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName("checkBox")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 60, 171, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 47, 13))
        self.label.setObjectName("label")
        self.kaydet_buton = QtWidgets.QPushButton(self.centralwidget)
        self.kaydet_buton.setGeometry(QtCore.QRect(10, 90, 171, 23))
        self.kaydet_buton.setObjectName("kaydet_buton")
        proxy_panel.setCentralWidget(self.centralwidget)

        self.retranslateUi(proxy_panel)
        QtCore.QMetaObject.connectSlotsByName(proxy_panel)

    def retranslateUi(self, proxy_panel):
        _translate = QtCore.QCoreApplication.translate
        proxy_panel.setWindowTitle(_translate("proxy_panel", "Proxy Settings"))
        self.checkBox.setText(_translate("proxy_panel", "Pinleme yapılırken proxy kullan"))
        self.lineEdit.setPlaceholderText(_translate("proxy_panel", "örn. 3.124.80.57:80"))
        self.label.setText(_translate("proxy_panel", "Proxy:"))
        self.kaydet_buton.setText(_translate("proxy_panel", "Ayarları Kaydet"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    proxy_panel = QtWidgets.QMainWindow()
    ui = Ui_proxy_panel()
    ui.setupUi(proxy_panel)
    proxy_panel.show()
    sys.exit(app.exec_())
