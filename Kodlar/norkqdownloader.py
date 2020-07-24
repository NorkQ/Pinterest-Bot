# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'norkqdownloader.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NorkQDownloader(object):
    def setupUi(self, NorkQDownloader):
        NorkQDownloader.setObjectName("NorkQDownloader")
        NorkQDownloader.resize(300, 260)
        NorkQDownloader.setMinimumSize(QtCore.QSize(300, 260))
        NorkQDownloader.setMaximumSize(QtCore.QSize(300, 260))
        self.centralwidget = QtWidgets.QWidget(NorkQDownloader)
        self.centralwidget.setObjectName("centralwidget")
        self.indirme_yolu_grup = QtWidgets.QGroupBox(self.centralwidget)
        self.indirme_yolu_grup.setGeometry(QtCore.QRect(10, 10, 281, 51))
        self.indirme_yolu_grup.setObjectName("indirme_yolu_grup")
        self.indirme_yolu_edit = QtWidgets.QLineEdit(self.indirme_yolu_grup)
        self.indirme_yolu_edit.setGeometry(QtCore.QRect(10, 24, 221, 20))
        self.indirme_yolu_edit.setObjectName("indirme_yolu_edit")
        self.indirme_yolu_buton = QtWidgets.QPushButton(self.indirme_yolu_grup)
        self.indirme_yolu_buton.setGeometry(QtCore.QRect(240, 24, 31, 21))
        self.indirme_yolu_buton.setObjectName("indirme_yolu_buton")
        self.indirme_sayfasi_grup = QtWidgets.QGroupBox(self.centralwidget)
        self.indirme_sayfasi_grup.setGeometry(QtCore.QRect(10, 70, 281, 51))
        self.indirme_sayfasi_grup.setObjectName("indirme_sayfasi_grup")
        self.indirme_yolu_edit_2 = QtWidgets.QLineEdit(self.indirme_sayfasi_grup)
        self.indirme_yolu_edit_2.setGeometry(QtCore.QRect(10, 24, 261, 20))
        self.indirme_yolu_edit_2.setObjectName("indirme_yolu_edit_2")
        self.pin_adedi_grup = QtWidgets.QGroupBox(self.centralwidget)
        self.pin_adedi_grup.setGeometry(QtCore.QRect(10, 130, 281, 51))
        self.pin_adedi_grup.setObjectName("pin_adedi_grup")
        self.pin_adedi_spin_box = QtWidgets.QSpinBox(self.pin_adedi_grup)
        self.pin_adedi_spin_box.setGeometry(QtCore.QRect(10, 24, 261, 22))
        self.pin_adedi_spin_box.setObjectName("pin_adedi_spin_box")
        self.pin_adedi_spin_box.setMaximum(99999999)
        self.filtre_ekle_check = QtWidgets.QCheckBox(self.centralwidget)
        self.filtre_ekle_check.setGeometry(QtCore.QRect(10, 190, 160, 23))
        self.filtre_ekle_check.setObjectName("filtre_check")
        self.ozgun_ayar_buton = QtWidgets.QPushButton(self.centralwidget)
        self.ozgun_ayar_buton.setGeometry(QtCore.QRect(200, 190, 92, 23))
        self.ozgun_ayar_buton.setObjectName("ozgun_ayar_buton")
        self.baslat_buton = QtWidgets.QPushButton(self.centralwidget)
        self.baslat_buton.setGeometry(QtCore.QRect(10, 225, 281, 23))
        self.baslat_buton.setObjectName("baslat_buton")
        NorkQDownloader.setCentralWidget(self.centralwidget)

        self.retranslateUi(NorkQDownloader)
        QtCore.QMetaObject.connectSlotsByName(NorkQDownloader)

    def retranslateUi(self, NorkQDownloader):
        _translate = QtCore.QCoreApplication.translate
        NorkQDownloader.setWindowTitle(_translate("NorkQDownloader", "NorkQ Downloader"))
        NorkQDownloader.setWindowIcon(QtGui.QIcon('logo.ico'))
        self.indirme_yolu_grup.setTitle(_translate("NorkQDownloader", "İndirme Yolu"))
        self.indirme_yolu_buton.setText(_translate("NorkQDownloader", "..."))
        self.indirme_sayfasi_grup.setTitle(_translate("NorkQDownloader", "İndirme Sayfası"))
        self.pin_adedi_grup.setTitle(_translate("NorkQDownloader", "Kaç adet pin indirilsin ?"))
        self.filtre_ekle_check.setText(_translate("NorkQDownloader", "İndirilen Resimleri Özgünleştir"))
        self.baslat_buton.setText(_translate("NorkQDownloader", "İndirmeyi Başlat"))
        self.filtre_ekle_check.stateChanged.connect(self.checkBoxChangedAction)
        self.ozgun_ayar_buton.setText(_translate("NorkQDownloader", "Ayarlar"))
        self.ozgun_ayar_buton.setEnabled(False)

    def checkBoxChangedAction(self, state):
        if (QtCore.Qt.Checked == state):
            self.ozgun_ayar_buton.setEnabled(True)
        else:
            self.ozgun_ayar_buton.setEnabled(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    NorkQDownloader = QtWidgets.QMainWindow()
    ui = Ui_NorkQDownloader()
    ui.setupUi(NorkQDownloader)
    NorkQDownloader.show()
    sys.exit(app.exec_())
