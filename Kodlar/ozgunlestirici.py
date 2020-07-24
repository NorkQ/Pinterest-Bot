# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ozgunlestirici_ayarlari.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QColorDialog
from PyQt5.QtGui import QColor
from functools import partial
from matplotlib import font_manager
import os.path


class Ui_ozgunlestirici_ayar(object):
    def __init__(self, functions):
        self.functions = functions

    def setupUi(self, ozgunlestirici_ayar):
        ozgunlestirici_ayar.setObjectName("ozgunlestirici_ayar")
        ozgunlestirici_ayar.resize(410, 700)
        ozgunlestirici_ayar.setMinimumSize(410, 700)
        ozgunlestirici_ayar.setMaximumSize(410, 700)
        self.centralwidget = QtWidgets.QWidget(ozgunlestirici_ayar)
        self.centralwidget.setObjectName("centralwidget")

        ######Filtre Ayarları######

        self.filtre_check = QtWidgets.QCheckBox(self.centralwidget)
        self.filtre_check.setGeometry(QtCore.QRect(10, 20, 101, 17))
        self.filtre_check.setObjectName("filtre_check")
        self.filtre_grup = QtWidgets.QGroupBox(self.centralwidget)
        self.filtre_grup.setEnabled(False)
        self.filtre_grup.setGeometry(QtCore.QRect(10, 40, 391, 80))
        self.filtre_grup.setObjectName("filtre_grup")
        self.filtre_rengi_label = QtWidgets.QLabel(self.filtre_grup)
        self.filtre_rengi_label.setGeometry(QtCore.QRect(10, 40, 301, 21))
        self.filtre_rengi_label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.filtre_rengi_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.filtre_rengi_label.setText("")
        self.filtre_rengi_label.setObjectName("filtre_rengi_label")
        self.filtre_rengi_text = QtWidgets.QLabel(self.filtre_grup)
        self.filtre_rengi_text.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.filtre_rengi_text.setObjectName("filtre_rengi_text")
        self.filtre_rengi_buton = QtWidgets.QPushButton(self.filtre_grup)
        self.filtre_rengi_buton.setGeometry(QtCore.QRect(320, 40, 61, 23))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.filtre_rengi_buton.setFont(font)
        self.filtre_rengi_buton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.filtre_rengi_buton.setCheckable(False)
        self.filtre_rengi_buton.setAutoDefault(False)
        self.filtre_rengi_buton.setObjectName("filtre_rengi_buton")

        #####Yazı Ayarları#####

        self.yazi_grup = QtWidgets.QGroupBox(self.centralwidget)
        self.yazi_grup.setEnabled(False)
        self.yazi_grup.setGeometry(QtCore.QRect(10, 160, 391, 220))
        self.yazi_grup.setObjectName("yazi_grup")
        self.yazi_edit = QtWidgets.QLineEdit(self.yazi_grup)
        self.yazi_edit.setGeometry(QtCore.QRect(10, 40, 371, 20))
        self.yazi_edit.setObjectName("yazi_edit")
        self.yazi_text = QtWidgets.QLabel(self.yazi_grup)
        self.yazi_text.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.yazi_text.setObjectName("yazi_text")
        self.yazi_boyut_spin = QtWidgets.QSpinBox(self.yazi_grup)
        self.yazi_boyut_spin.setGeometry(QtCore.QRect(10, 90, 121, 22))
        self.yazi_boyut_spin.setObjectName("yazi_boyut_spin")
        self.yazi_boyut_text = QtWidgets.QLabel(self.yazi_grup)
        self.yazi_boyut_text.setGeometry(QtCore.QRect(10, 70, 47, 13))
        self.yazi_boyut_text.setObjectName("yazi_boyut_text")
        self.yazi_konum_combo = QtWidgets.QComboBox(self.yazi_grup)
        self.yazi_konum_combo.setGeometry(QtCore.QRect(140, 90, 121, 22))
        self.yazi_konum_combo.setObjectName("yazi_konum_combo")
        self.yazi_konum_combo.addItem("")
        self.yazi_konum_combo.addItem("")
        self.yazi_konum_combo.addItem("")
        self.yazi_konum_combo.addItem("")
        self.yazi_konum_combo.addItem("")
        self.yazi_konum_combo.addItem("")
        self.yazi_konum_combo.addItem("")
        self.yazi_konum_combo.addItem("")
        self.yazi_konum_combo.addItem("")
        self.yazi_konum_text = QtWidgets.QLabel(self.yazi_grup)
        self.yazi_konum_text.setGeometry(QtCore.QRect(140, 70, 47, 13))
        self.yazi_konum_text.setObjectName("yazi_konum_text")
        self.yazi_rotasyon_text = QtWidgets.QLabel(self.yazi_grup)
        self.yazi_rotasyon_text.setGeometry(QtCore.QRect(270, 70, 47, 13))
        self.yazi_rotasyon_text.setObjectName("yazi_rotasyon_text")
        self.yazi_rotasyon_spin = QtWidgets.QSpinBox(self.yazi_grup)
        self.yazi_rotasyon_spin.setGeometry(QtCore.QRect(270, 90, 111, 22))
        self.yazi_rotasyon_spin.setObjectName("yazi_rotasyon_spin")
        self.yazi_rengi_label = QtWidgets.QLabel(self.yazi_grup)
        self.yazi_rengi_label.setGeometry(QtCore.QRect(10, 140, 301, 21))
        self.yazi_rengi_label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.yazi_rengi_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.yazi_rengi_label.setText("")
        self.yazi_rengi_label.setObjectName("yazi_rengi_label")
        self.yazi_rengi_text = QtWidgets.QLabel(self.yazi_grup)
        self.yazi_rengi_text.setGeometry(QtCore.QRect(10, 120, 51, 16))
        self.yazi_rengi_text.setObjectName("yazi_rengi_text")
        self.yazi_rengi_buton = QtWidgets.QPushButton(self.yazi_grup)
        self.yazi_rengi_buton.setGeometry(QtCore.QRect(320, 140, 61, 23))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.yazi_rengi_buton.setFont(font)
        self.yazi_rengi_buton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.yazi_rengi_buton.setCheckable(False)
        self.yazi_rengi_buton.setAutoDefault(False)
        self.yazi_rengi_buton.setObjectName("yazi_rengi_buton")
        self.yazi_font_text = QtWidgets.QLabel(self.yazi_grup)
        self.yazi_font_text.setGeometry(QtCore.QRect(10, 170, 60, 13))
        self.yazi_font_text.setObjectName("yazi_font_text")
        self.yazi_font_combo = QtWidgets.QComboBox(self.yazi_grup)
        self.yazi_font_combo.setGeometry(QtCore.QRect(10, 190, 370, 21))
        self.yazi_font_combo.setObjectName("yazi_font_combo")
        self.yazi_check = QtWidgets.QCheckBox(self.centralwidget)
        self.yazi_check.setGeometry(QtCore.QRect(10, 140, 70, 17))
        self.yazi_check.setObjectName("yazi_check")

        #####Logo Ayarları######

        self.logo_check = QtWidgets.QCheckBox(self.centralwidget)
        self.logo_check.setGeometry(QtCore.QRect(10, 400, 70, 17))
        self.logo_check.setObjectName("logo_check")
        self.logo_grup = QtWidgets.QGroupBox(self.centralwidget)
        self.logo_grup.setEnabled(False)
        self.logo_grup.setGeometry(QtCore.QRect(10, 420, 391, 181))
        self.logo_grup.setObjectName("logo_grup")
        self.logo_konum_entry = QtWidgets.QLineEdit(self.logo_grup)
        self.logo_konum_entry.setGeometry(QtCore.QRect(10, 40, 301, 21))
        self.logo_konum_entry.setObjectName("logo_konum_entry")
        self.logo_yolu_text = QtWidgets.QLabel(self.logo_grup)
        self.logo_yolu_text.setGeometry(QtCore.QRect(10, 20, 121, 16))
        self.logo_yolu_text.setObjectName("logo_yolu_text")
        self.logo_yol_buton = QtWidgets.QPushButton(self.logo_grup)
        self.logo_yol_buton.setGeometry(QtCore.QRect(320, 40, 61, 23))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.logo_yol_buton.setFont(font)
        self.logo_yol_buton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.logo_yol_buton.setCheckable(False)
        self.logo_yol_buton.setAutoDefault(False)
        self.logo_yol_buton.setObjectName("logo_yol_buton")
        self.logo_rotasyon_spin = QtWidgets.QSpinBox(self.logo_grup)
        self.logo_rotasyon_spin.setGeometry(QtCore.QRect(270, 90, 111, 22))
        self.logo_rotasyon_spin.setObjectName("logo_rotasyon_spin")
        self.logo_konum_combo = QtWidgets.QComboBox(self.logo_grup)
        self.logo_konum_combo.setGeometry(QtCore.QRect(140, 90, 121, 22))
        self.logo_konum_combo.setObjectName("logo_konum_combo")
        self.logo_konum_combo.addItem("")
        self.logo_konum_combo.addItem("")
        self.logo_konum_combo.addItem("")
        self.logo_konum_combo.addItem("")
        self.logo_konum_combo.addItem("")
        self.logo_konum_combo.addItem("")
        self.logo_konum_combo.addItem("")
        self.logo_konum_combo.addItem("")
        self.logo_konum_combo.addItem("")
        self.logo_boyut_spin = QtWidgets.QSpinBox(self.logo_grup)
        self.logo_boyut_spin.setGeometry(QtCore.QRect(10, 90, 121, 22))
        self.logo_boyut_spin.setObjectName("logo_boyut_spin")
        self.logo_boyut_spin.setMinimum(-999999)
        self.logo_rotasyon_text = QtWidgets.QLabel(self.logo_grup)
        self.logo_rotasyon_text.setGeometry(QtCore.QRect(270, 70, 47, 13))
        self.logo_rotasyon_text.setObjectName("logo_rotasyon_text")
        self.logo_konum_text = QtWidgets.QLabel(self.logo_grup)
        self.logo_konum_text.setGeometry(QtCore.QRect(140, 70, 47, 13))
        self.logo_konum_text.setObjectName("logo_konum_text")
        self.logo_boyut_text = QtWidgets.QLabel(self.logo_grup)
        self.logo_boyut_text.setGeometry(QtCore.QRect(10, 70, 47, 13))
        self.logo_boyut_text.setObjectName("logo_boyut_text")
        self.logo_saydam_slider = QtWidgets.QSlider(self.logo_grup)
        self.logo_saydam_slider.setGeometry(QtCore.QRect(110, 150, 271, 22))
        self.logo_saydam_slider.setMaximum(255)
        self.logo_saydam_slider.setSingleStep(1)
        self.logo_saydam_slider.setOrientation(QtCore.Qt.Horizontal)
        self.logo_saydam_slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.logo_saydam_slider.setTickInterval(0)
        self.logo_saydam_slider.setObjectName("logo_saydam_slider")
        self.logo_saydamlik_text = QtWidgets.QLabel(self.logo_grup)
        self.logo_saydamlik_text.setGeometry(QtCore.QRect(10, 120, 61, 16))
        self.logo_saydamlik_text.setObjectName("logo_saydamlik_text")
        self.logo_saydamlik_spin = QtWidgets.QSpinBox(self.logo_grup)
        self.logo_saydamlik_spin.setGeometry(QtCore.QRect(10, 150, 91, 22))
        self.logo_saydamlik_spin.setMaximum(255)
        self.logo_saydamlik_spin.setSingleStep(1)
        self.logo_saydamlik_spin.setObjectName("logo_saydamlik_spin")
        self.on_izleme_buton = QtWidgets.QPushButton(self.centralwidget)
        self.on_izleme_buton.setGeometry(QtCore.QRect(10, 610, 391, 51))
        self.on_izleme_buton.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.on_izleme_buton.setObjectName("on_izleme_buton")
        self.kaydet_buton = QtWidgets.QPushButton(self.centralwidget)
        self.kaydet_buton.setGeometry(QtCore.QRect(10, 670, 391, 25))
        self.kaydet_buton.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.kaydet_buton.setObjectName("kaydet_buton")
        ozgunlestirici_ayar.setCentralWidget(self.centralwidget)

        self.retranslateUi(ozgunlestirici_ayar)
        self.logo_saydam_slider.sliderMoved['int'].connect(self.logo_saydamlik_spin.setValue)
        self.logo_saydamlik_spin.valueChanged['int'].connect(self.logo_saydam_slider.setValue)
        self.filtre_check.clicked['bool'].connect(self.filtre_grup.setEnabled)
        self.yazi_check.clicked['bool'].connect(self.yazi_grup.setEnabled)
        self.logo_check.clicked['bool'].connect(self.logo_grup.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(ozgunlestirici_ayar)

    def retranslateUi(self, ozgunlestirici_ayar):
        _translate = QtCore.QCoreApplication.translate
        ozgunlestirici_ayar.setWindowTitle(_translate("ozgunlestirici_ayar", "Özgünleştirici Ayarları"))
        self.filtre_check.setText(_translate("ozgunlestirici_ayar", "Filtre Ekle"))
        self.filtre_grup.setTitle(_translate("ozgunlestirici_ayar", "Filtre Ayarları"))
        self.filtre_rengi_text.setText(_translate("ozgunlestirici_ayar", "Filtre Rengi"))
        self.filtre_rengi_buton.setText(_translate("ozgunlestirici_ayar", "Seç"))
        self.yazi_grup.setTitle(_translate("ozgunlestirici_ayar", "Yazı Ayarları"))
        self.yazi_text.setText(_translate("ozgunlestirici_ayar", "Yazı"))
        self.yazi_boyut_text.setText(_translate("ozgunlestirici_ayar", "Boyut"))
        self.yazi_konum_combo.setItemText(0, _translate("ozgunlestirici_ayar", "Sol Üst"))
        self.yazi_konum_combo.setItemText(1, _translate("ozgunlestirici_ayar", "Sol Orta"))
        self.yazi_konum_combo.setItemText(2, _translate("ozgunlestirici_ayar", "Sol Alt"))
        self.yazi_konum_combo.setItemText(3, _translate("ozgunlestirici_ayar", "Orta Üst"))
        self.yazi_konum_combo.setItemText(4, _translate("ozgunlestirici_ayar", "Orta"))
        self.yazi_konum_combo.setItemText(5, _translate("ozgunlestirici_ayar", "Orta Alt"))
        self.yazi_konum_combo.setItemText(6, _translate("ozgunlestirici_ayar", "Sağ Üst"))
        self.yazi_konum_combo.setItemText(7, _translate("ozgunlestirici_ayar", "Sağ Orta"))
        self.yazi_konum_combo.setItemText(8, _translate("ozgunlestirici_ayar", "Sağ Alt"))
        self.yazi_konum_text.setText(_translate("ozgunlestirici_ayar", "Konum"))
        self.yazi_rotasyon_text.setText(_translate("ozgunlestirici_ayar", "Rotasyon"))
        self.yazi_rengi_text.setText(_translate("ozgunlestirici_ayar", "Yazı Rengi"))
        self.yazi_rengi_buton.setText(_translate("ozgunlestirici_ayar", "Seç"))
        self.yazi_font_text.setText(_translate("ozgunlestirici_ayar", "Yazı Fontu"))
        self.yazi_check.setText(_translate("ozgunlestirici_ayar", "Yazı Ekle"))
        self.logo_check.setText(_translate("ozgunlestirici_ayar", "Logo Ekle"))
        self.logo_grup.setTitle(_translate("ozgunlestirici_ayar", "Logo Ayarları"))
        self.logo_yolu_text.setText(_translate("ozgunlestirici_ayar", "Logonun Bulunduğu Yer"))
        self.logo_yol_buton.setText(_translate("ozgunlestirici_ayar", "Seç"))
        self.logo_konum_combo.setItemText(0, _translate("ozgunlestirici_ayar", "Sol Üst"))
        self.logo_konum_combo.setItemText(1, _translate("ozgunlestirici_ayar", "Sol Orta"))
        self.logo_konum_combo.setItemText(2, _translate("ozgunlestirici_ayar", "Sol Alt"))
        self.logo_konum_combo.setItemText(3, _translate("ozgunlestirici_ayar", "Orta Üst"))
        self.logo_konum_combo.setItemText(4, _translate("ozgunlestirici_ayar", "Orta"))
        self.logo_konum_combo.setItemText(5, _translate("ozgunlestirici_ayar", "Orta Alt"))
        self.logo_konum_combo.setItemText(6, _translate("ozgunlestirici_ayar", "Sağ Üst"))
        self.logo_konum_combo.setItemText(7, _translate("ozgunlestirici_ayar", "Sağ Orta"))
        self.logo_konum_combo.setItemText(8, _translate("ozgunlestirici_ayar", "Sağ Alt"))
        self.logo_rotasyon_text.setText(_translate("ozgunlestirici_ayar", "Rotasyon"))
        self.logo_konum_text.setText(_translate("ozgunlestirici_ayar", "Konum"))
        self.logo_boyut_text.setText(_translate("ozgunlestirici_ayar", "Boyut"))
        self.logo_saydamlik_text.setText(_translate("ozgunlestirici_ayar", "Saydamlık"))
        self.on_izleme_buton.setText(_translate("ozgunlestirici_ayar", "Ön İzlemeyi Güncelle"))
        self.kaydet_buton.setText(_translate("ozgunlestirici_ayar", "Ayarları Kaydet"))

        self.filtre_rengi_buton.clicked.connect(partial(self.openColorDialog, self.filtre_rengi_label))
        self.yazi_rengi_buton.clicked.connect(partial(self.openColorDialog, self.yazi_rengi_label))
        self.kaydet_buton.clicked.connect(self.ayarlari_kaydet)
        self.on_izleme_buton.clicked.connect(partial(self.on_izlemeyi_guncelle, "3.jpg"))
        self.logo_yol_buton.clicked.connect(partial(self.functions.logo_sec, self.logo_konum_entry))
        self.fontlari_getir()

    def on_izlemeyi_guncelle(self, yol):
        self.ayarlari_kaydet()
        self.functions.ozgunlestir_on_izleme(yol, self.functions.ozgun_ayarlar["filtre"], self.functions.ozgun_ayarlar["yazi"], self.functions.ozgun_ayarlar["logo"])

    def fontlari_getir(self):
        fonts = []
        if os.path.isfile('fonts.txt'):
            print("Dosya zaten var")
        else:
            fonts_file = open("fonts.txt", "a+")
            system_fonts = font_manager.findSystemFonts()
            print(len(system_fonts))
            for font in system_fonts:
                font = font.split("\\")
                font = font[len(font) - 1]
                fonts.append(font+"\n")

            fonts.sort()
            for font in fonts:
                fonts_file.write(font)
            fonts_file.close()


        fonts = open("fonts.txt", "r").readlines()
        for font in fonts:
            font = font.strip()
            self.yazi_font_combo.addItem(font)


    def openColorDialog(self, label):
        dialog = QColorDialog()
        dialog.setOption(QColorDialog.ShowAlphaChannel, on=True)
        print(dialog.testOption(dialog.ShowAlphaChannel)) #returning True
        color = QColorDialog.getColor(options=QColorDialog.ShowAlphaChannel)

        if color.isValid():
            label.setStyleSheet("background-color:" + color.name(QColor.HexArgb) + ";")

    def ayarlari_kaydet(self):
        ayarlar = {
            #filtre
            "filtre" : self.filtre_check.isChecked(),
            "filtre_rengi" : self.filtre_rengi_label.palette().button().color().getRgb(),

            #yazi
            "yazi" : self.yazi_check.isChecked(),
            "yazi_metni" : self.yazi_edit.text(),
            "yazi_boyut" : self.yazi_boyut_spin.value(),
            "yazi_konum" : self.yazi_konum_combo.currentText(),
            "yazi_rotasyon" : self.yazi_rotasyon_spin.value(),
            "yazi_rengi" : self.yazi_rengi_label.palette().button().color().getRgb(),
            "yazi_font" : self.yazi_font_combo.currentText(),

            #logo
            "logo" : self.logo_check.isChecked(),
            "logo_yolu" : self.logo_konum_entry.text(),
            "logo_boyut" : self.logo_boyut_spin.value(),
            "logo_konum" : self.logo_konum_combo.currentText(),
            "logo_rotasyon" : self.logo_rotasyon_spin.value(),
            "logo_saydamlik" : self.logo_saydamlik_spin.value()
        }

        print(ayarlar)
        self.functions.ozgun_ayarlar = ayarlar

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    ozgunlestirici_ayar = QtWidgets.QMainWindow()
    ui = Ui_ozgunlestirici_ayar()
    ui.setupUi(ozgunlestirici_ayar)
    ozgunlestirici_ayar.show()
    sys.exit(app.exec_())
