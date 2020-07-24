# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uyarilar.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_uyari_penceresi(object):
    def setupUi(self, uyari_penceresi):
        uyari_penceresi.setObjectName("uyari_penceresi")
        uyari_penceresi.resize(300, 340)
        self.centralwidget = QtWidgets.QWidget(uyari_penceresi)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QLabel(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        uyari_penceresi.setCentralWidget(self.centralwidget)

        self.retranslateUi(uyari_penceresi)
        QtCore.QMetaObject.connectSlotsByName(uyari_penceresi)

    def retranslateUi(self, uyari_penceresi):
        _translate = QtCore.QCoreApplication.translate
        uyari_penceresi.setWindowIcon(QtGui.QIcon('logo.ico'))
        uyari_penceresi.setWindowTitle(_translate("uyari_penceresi", "Uyarılar ve Açıklamalar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    uyari_penceresi = QtWidgets.QMainWindow()
    ui = Ui_uyari_penceresi()
    ui.setupUi(uyari_penceresi)
    uyari_penceresi.show()
    sys.exit(app.exec_())
