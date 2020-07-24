# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pinterest.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMenu, QSplashScreen
from PyQt5.QtCore import QSize, QTimer
from PyQt5.QtGui import QPixmap
from norkqdownloader import Ui_NorkQDownloader
import norkqlogger
from norkqeditor import Ui_NorkkQEditor
from uyarilar import Ui_uyari_penceresi
from proxy import Ui_proxy_panel
from Functions.Functions import Functions
from ozgunlestirici import Ui_ozgunlestirici_ayar
from threading import Thread
from functools import partial
import sys, time
import urllib.request


class Ui_MainWindow(object):
    def NorkQ_Proxy_Ac(self, functions):
        self.proxy_window = QtWidgets.QMainWindow()
        self.proxy_ui = Ui_proxy_panel()
        self.proxy_ui.setupUi(self.proxy_window)
        self.proxy_ui.kaydet_buton.clicked.connect(self.proxy_kontrol)
        self.proxy_window.show()
    def NorkQ_Uyari_Ac(self, mesaj):
        self.uyari_window = QtWidgets.QMainWindow()
        self.uyari_ui = Ui_uyari_penceresi()
        self.uyari_ui.setupUi(self.uyari_window)

        url = mesaj
        urllib.request.urlretrieve(url, 'uyari.png')
        pixmap = QPixmap("uyari.png")
        self.uyari_ui.plainTextEdit.setPixmap(QPixmap(pixmap))
        self.uyari_window.resize(pixmap.width(), pixmap.height())

        self.uyari_window.show()
    def NorkQ_Downloader_Ac(self, functions):
        self.downloader_window = QtWidgets.QMainWindow()
        self.downloader_ui = Ui_NorkQDownloader()
        self.downloader_ui.setupUi(self.downloader_window)
        self.downloader_ui.indirme_yolu_buton.clicked.connect(partial(functions.indirme_yolu_sec, self.downloader_ui.indirme_yolu_edit))
        self.downloader_ui.baslat_buton.clicked.connect(partial(self.indirmeye_basla, self.downloader_ui.pin_adedi_spin_box, self.downloader_ui.indirme_yolu_edit_2))
        self.downloader_ui.ozgun_ayar_buton.clicked.connect(partial(self.Ozgun_Ayar_Ac, functions))
        self.downloader_window.show()
    def Ozgun_Ayar_Ac(self, functions):
        self.ozgun_window = QtWidgets.QMainWindow()
        self.ozgun_ui = Ui_ozgunlestirici_ayar(functions)
        self.ozgun_ui.setupUi(self.ozgun_window)
        self.ozgun_window.show()
    def NorkQ_Logger_Ac(self, functions):
        self.logger_window = QtWidgets.QMainWindow()
        self.logger_ui = norkqlogger.Ui_MainWindow()
        self.logger_ui.setupUi(self.logger_window)
        functions.kayitlari_getir(self.logger_ui.kayitlar_textedit)
        self.logger_window.show()
    def NorkQ_Editor_Ac(self, functions):
        self.editor_window = QtWidgets.QMainWindow()
        self.editor_ui = Ui_NorkkQEditor()
        self.editor_ui.setupUi(self.editor_window)
        self.editor_ui.pini_ekle_buton.clicked.connect(functions.manuel_pin_olustur)
        self.editor_ui.goruntu_sec_buton.clicked.connect(functions.goruntu_sec)

        #ekle
        self.editor_ui.baslik_ekle_buton.clicked.connect(partial(functions.anahtar_ekle, self.editor_ui.baslik_entry, "baslik"))
        self.editor_ui.aciklama_ekle_buton.clicked.connect(partial(functions.anahtar_ekle, self.editor_ui.aciklama_entry, "aciklama"))
        self.editor_ui.link_ekle_buton.clicked.connect(partial(functions.anahtar_ekle, self.editor_ui.link_entry, "link"))
        self.editor_ui.pano_ekle_buton.clicked.connect(partial(functions.anahtar_ekle, self.editor_ui.pano_entry, "pano"))

        #sil
        self.editor_ui.baslik_sil_buton.clicked.connect(partial(functions.anahtar_sil, self.editor_ui.baslik_entry, "baslik"))
        self.editor_ui.aciklama_sil_buton.clicked.connect(partial(functions.anahtar_sil, self.editor_ui.aciklama_entry, "aciklama"))
        self.editor_ui.link_sil_buton.clicked.connect(partial(functions.anahtar_sil, self.editor_ui.link_entry, "link"))
        self.editor_ui.pano_sil_buton.clicked.connect(partial(functions.anahtar_sil, self.editor_ui.pano_entry, "pano"))

        #temizle
        self.editor_ui.basliklar_sil.clicked.connect(partial(functions.liste_temizle, self.basliklar_list))
        self.editor_ui.aciklamalar_sil.clicked.connect(partial(functions.liste_temizle, self.aciklamalar_list))
        self.editor_ui.linkler_sil.clicked.connect(partial(functions.liste_temizle, self.linkler_list))
        self.editor_ui.resimler_sil.clicked.connect(partial(functions.liste_temizle, self.resimler_list))
        self.editor_ui.panolar_sil.clicked.connect(partial(functions.liste_temizle, self.panolar_list))

        self.editor_window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 460)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(16777194, 16777215))
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        MainWindow.setAcceptDrops(False)
        MainWindow.setStyleSheet("background-color: rgb(248, 248, 248);")
        MainWindow.setFixedSize(QSize(900, 460))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.hesap_ayarlari = QtWidgets.QGroupBox(self.centralwidget)
        self.hesap_ayarlari.setGeometry(QtCore.QRect(10, 80, 380, 111))
        self.hesap_ayarlari.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.hesap_ayarlari.setObjectName("hesap_ayarlari")
        self.kullanici_adi_label = QtWidgets.QLabel(self.hesap_ayarlari)
        self.kullanici_adi_label.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.kullanici_adi_label.setObjectName("kullanici_adi_label")
        self.kullanici_adi_entry = QtWidgets.QLineEdit(self.hesap_ayarlari)
        self.kullanici_adi_entry.setGeometry(QtCore.QRect(10, 40, 360, 20))
        self.kullanici_adi_entry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.kullanici_adi_entry.setObjectName("kullanici_adi_entry")
        self.sifre_entry = QtWidgets.QLineEdit(self.hesap_ayarlari)
        self.sifre_entry.setGeometry(QtCore.QRect(10, 80, 360, 20))
        self.sifre_entry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sifre_entry.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sifre_entry.setObjectName("sifre_entry")
        self.sifre_label = QtWidgets.QLabel(self.hesap_ayarlari)
        self.sifre_label.setGeometry(QtCore.QRect(10, 60, 61, 16))
        self.sifre_label.setObjectName("sifre_label")
        self.pin_zaman_ayarlari = QtWidgets.QGroupBox(self.centralwidget)
        self.pin_zaman_ayarlari.setGeometry(QtCore.QRect(400, 80, 490, 111))
        self.pin_zaman_ayarlari.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.pin_zaman_ayarlari.setObjectName("pin_zaman_ayarlari")
        self.tek_aralik_label = QtWidgets.QLabel(self.pin_zaman_ayarlari)
        self.tek_aralik_label.setGeometry(QtCore.QRect(10, 20, 201, 16))
        self.tek_aralik_label.setObjectName("tek_aralik_label")
        self.pin_grubu_sayisi_label = QtWidgets.QLabel(self.pin_zaman_ayarlari)
        self.pin_grubu_sayisi_label.setGeometry(QtCore.QRect(10, 60, 201, 16))
        self.pin_grubu_sayisi_label.setObjectName("pin_grubu_sayisi_label")
        self.grup_arasi_label = QtWidgets.QLabel(self.pin_zaman_ayarlari)
        self.grup_arasi_label.setGeometry(QtCore.QRect(250, 20, 201, 16))
        self.grup_arasi_label.setObjectName("grup_arasi_label")
        self.max_pin_label = QtWidgets.QLabel(self.pin_zaman_ayarlari)
        self.max_pin_label.setGeometry(QtCore.QRect(250, 60, 201, 16))
        self.max_pin_label.setObjectName("max_pin_label")
        self.tek_aralik_entry = QtWidgets.QSpinBox(self.pin_zaman_ayarlari)
        self.tek_aralik_entry.setGeometry(QtCore.QRect(10, 40, 230, 22))
        self.tek_aralik_entry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tek_aralik_entry.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.tek_aralik_entry.setMaximum(999999999)
        self.tek_aralik_entry.setProperty("value", 60)
        self.tek_aralik_entry.setObjectName("tek_aralik_label_2")
        self.pin_grubu_sayisi_entry = QtWidgets.QSpinBox(self.pin_zaman_ayarlari)
        self.pin_grubu_sayisi_entry.setGeometry(QtCore.QRect(10, 80, 230, 22))
        self.pin_grubu_sayisi_entry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pin_grubu_sayisi_entry.setMaximum(999999999)
        self.pin_grubu_sayisi_entry.setProperty("value", 10)
        self.pin_grubu_sayisi_entry.setObjectName("pin_grubu_sayisi_entry")
        self.grup_arasi_entry = QtWidgets.QSpinBox(self.pin_zaman_ayarlari)
        self.grup_arasi_entry.setGeometry(QtCore.QRect(250, 40, 230, 22))
        self.grup_arasi_entry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.grup_arasi_entry.setMaximum(999999999)
        self.grup_arasi_entry.setProperty("value", 3600)
        self.grup_arasi_entry.setObjectName("grup_arasi_entry")
        self.max_pin_entry = QtWidgets.QSpinBox(self.pin_zaman_ayarlari)
        self.max_pin_entry.setGeometry(QtCore.QRect(250, 80, 230, 22))
        self.max_pin_entry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.max_pin_entry.setMaximum(999999999)
        self.max_pin_entry.setProperty("value", 50)
        self.max_pin_entry.setObjectName("max_pin_entry")
        self.anahtar_grup = QtWidgets.QGroupBox(self.centralwidget)
        self.anahtar_grup.setGeometry(QtCore.QRect(10, 10, 880, 51))
        self.anahtar_grup.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.anahtar_grup.setObjectName("anahtar_grup")
        self.anahtar_entry = QtWidgets.QLineEdit(self.anahtar_grup)
        self.anahtar_entry.setGeometry(QtCore.QRect(10, 24, 700, 20))
        self.anahtar_entry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.anahtar_entry.setObjectName("anahtar_entry")
        self.onayla_buton = QtWidgets.QPushButton(self.anahtar_grup)
        self.onayla_buton.setGeometry(QtCore.QRect(720, 24, 150, 22))
        self.onayla_buton.setObjectName("onayla_buton")
        self.pin_ayarlari_grup = QtWidgets.QGroupBox(self.centralwidget)
        self.pin_ayarlari_grup.setGeometry(QtCore.QRect(10, 200, 880, 221))
        self.pin_ayarlari_grup.setObjectName("pin_ayarlari_grup")
        self.basliklar_label = QtWidgets.QLabel(self.pin_ayarlari_grup)
        self.basliklar_label.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.basliklar_label.setObjectName("basliklar_label")
        self.aciklamalar_label = QtWidgets.QLabel(self.pin_ayarlari_grup)
        self.aciklamalar_label.setGeometry(QtCore.QRect(193, 20, 61, 16))
        self.aciklamalar_label.setObjectName("aciklamalar_label")
        self.linkler_label = QtWidgets.QLabel(self.pin_ayarlari_grup)
        self.linkler_label.setGeometry(QtCore.QRect(365, 20, 61, 16))
        self.linkler_label.setObjectName("linkler_label")
        self.resimler_label = QtWidgets.QLabel(self.pin_ayarlari_grup)
        self.resimler_label.setGeometry(QtCore.QRect(537, 20, 61, 16))
        self.resimler_label.setObjectName("panolar_label")
        self.panolar_label = QtWidgets.QLabel(self.pin_ayarlari_grup)
        self.panolar_label.setGeometry(QtCore.QRect(710, 20, 61, 16))
        self.panolar_label.setObjectName("panolar_label")

        self.basliklar_dosya_buton = QtWidgets.QPushButton(self.pin_ayarlari_grup)
        self.basliklar_dosya_buton.setGeometry(QtCore.QRect(10, 140, 170, 23))
        self.basliklar_dosya_buton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.basliklar_dosya_buton.setCheckable(False)
        self.basliklar_dosya_buton.setObjectName("basliklar_dosya_buton")


        self.basliklar_list = QtWidgets.QListWidget(self.pin_ayarlari_grup)
        self.basliklar_list.setGeometry(QtCore.QRect(10, 40, 170, 91))
        self.basliklar_list.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.basliklar_list.setObjectName("basliklar_list")


        self.aciklamalar_list = QtWidgets.QListWidget(self.pin_ayarlari_grup)
        self.aciklamalar_list.setGeometry(QtCore.QRect(193, 40, 160, 91))
        self.aciklamalar_list.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.aciklamalar_list.setObjectName("aciklamalar_list")


        self.linkler_list = QtWidgets.QListWidget(self.pin_ayarlari_grup)
        self.linkler_list.setGeometry(QtCore.QRect(365, 40, 160, 91))
        self.linkler_list.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.linkler_list.setObjectName("linkler_list")


        self.resimler_list = QtWidgets.QListWidget(self.pin_ayarlari_grup)
        self.resimler_list.setGeometry(QtCore.QRect(537, 40, 160, 91))
        self.resimler_list.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.resimler_list.setObjectName("resimler_list")


        self.panolar_list = QtWidgets.QListWidget(self.pin_ayarlari_grup)
        self.panolar_list.setGeometry(QtCore.QRect(710, 40, 160, 91))
        self.panolar_list.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.panolar_list.setObjectName("basliklar_list")


        self.rastgele_pin_checkbox = QtWidgets.QCheckBox(self.pin_ayarlari_grup)
        self.rastgele_pin_checkbox.setGeometry(QtCore.QRect(320, 190, 231, 23))
        self.rastgele_pin_checkbox.setIconSize(QtCore.QSize(16, 16))
        self.rastgele_pin_checkbox.setChecked(False)
        self.rastgele_pin_checkbox.setTristate(False)
        self.rastgele_pin_checkbox.setObjectName("rastgele_pin_checkbox")
        self.aciklamalar_dosya_buton = QtWidgets.QPushButton(self.pin_ayarlari_grup)
        self.aciklamalar_dosya_buton.setGeometry(QtCore.QRect(193, 140, 160, 23))
        self.aciklamalar_dosya_buton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.aciklamalar_dosya_buton.setCheckable(False)
        self.aciklamalar_dosya_buton.setObjectName("aciklamalar_dosya_buton")
        self.linkler_dosya_buton = QtWidgets.QPushButton(self.pin_ayarlari_grup)
        self.linkler_dosya_buton.setGeometry(QtCore.QRect(365, 140, 160, 23))
        self.linkler_dosya_buton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.linkler_dosya_buton.setCheckable(False)
        self.linkler_dosya_buton.setObjectName("linkler_dosya_buton")
        self.resimler_dosya_buton = QtWidgets.QPushButton(self.pin_ayarlari_grup)
        self.resimler_dosya_buton.setGeometry(QtCore.QRect(537, 140, 75, 23))
        self.resimler_dosya_buton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.resimler_dosya_buton.setCheckable(False)
        self.resimler_dosya_buton.setObjectName("resimler_dosya_buton")
        self.resimler_klasor_buton = QtWidgets.QPushButton(self.pin_ayarlari_grup)
        self.resimler_klasor_buton.setGeometry(QtCore.QRect(623, 140, 75, 23))
        self.resimler_klasor_buton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.resimler_klasor_buton.setCheckable(False)
        self.resimler_klasor_buton.setObjectName("resimler_klasor_buton")
        self.panolar_dosya_buton = QtWidgets.QPushButton(self.pin_ayarlari_grup)
        self.panolar_dosya_buton.setGeometry(QtCore.QRect(710, 140, 160, 23))
        self.panolar_dosya_buton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.panolar_dosya_buton.setCheckable(False)
        self.panolar_dosya_buton.setObjectName("panolar_dosya_buton")

        self.resim_indirici_buton = QtWidgets.QPushButton(self.centralwidget)
        self.resim_indirici_buton.setGeometry(QtCore.QRect(10, 430, 150, 23))
        self.resim_indirici_buton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.resim_indirici_buton.setCheckable(False)
        self.resim_indirici_buton.setObjectName("resim_indirici_buton")

        self.kayit_buton = QtWidgets.QPushButton(self.centralwidget)
        self.kayit_buton.setGeometry(QtCore.QRect(170, 430, 150, 23))
        self.kayit_buton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.kayit_buton.setCheckable(False)
        self.kayit_buton.setObjectName("kayit_buton")

        self.manuel_buton = QtWidgets.QPushButton(self.centralwidget)
        self.manuel_buton.setGeometry(QtCore.QRect(330, 430, 150, 23))
        self.manuel_buton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.manuel_buton.setCheckable(False)
        self.manuel_buton.setObjectName("manuel_buton")

        self.proxy_buton = QtWidgets.QPushButton(self.centralwidget)
        self.proxy_buton.setGeometry(QtCore.QRect(490, 430, 150, 23))
        self.proxy_buton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.proxy_buton.setCheckable(False)
        self.proxy_buton.setObjectName("proxy_buton")

        self.baslat_buton = QtWidgets.QPushButton(self.centralwidget)
        self.baslat_buton.setGeometry(QtCore.QRect(650, 430, 240, 23))
        self.baslat_buton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.baslat_buton.setCheckable(False)
        self.baslat_buton.setObjectName("baslat_buton")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NorkQ Pinner"))
        MainWindow.setWindowIcon(QtGui.QIcon('logo.ico'))
        self.hesap_ayarlari.setTitle(_translate("MainWindow", "Hesap Ayarları"))
        self.kullanici_adi_label.setText(_translate("MainWindow", "Kullanıcı Adı :"))
        self.sifre_label.setText(_translate("MainWindow", "Şifre :"))
        self.pin_zaman_ayarlari.setTitle(_translate("MainWindow", "Pin Zaman Ayarları"))
        self.tek_aralik_label.setText(_translate("MainWindow", "Kaç Saniyede Bir Pin Atılsın ?"))
        self.pin_grubu_sayisi_label.setText(_translate("MainWindow", "Kaç Pin Atıldıktan Sonra Beklensin ?"))
        self.grup_arasi_label.setText(_translate("MainWindow", "Pin Grubu Arası Bekleme Kaç Saniye Olsun ?"))
        self.max_pin_label.setText(_translate("MainWindow", "Bugünkü Atılacak Max Pin Sayısı"))
        self.anahtar_grup.setTitle(_translate("MainWindow", "Anahtar"))
        self.onayla_buton.setText(_translate("MainWindow", "Onayla"))
        self.pin_ayarlari_grup.setTitle(_translate("MainWindow", "Pin Ayarları"))
        self.basliklar_label.setText(_translate("MainWindow", "Başlıklar"))
        self.aciklamalar_label.setText(_translate("MainWindow", "Açıklamalar"))
        self.linkler_label.setText(_translate("MainWindow", "Linkler"))
        self.resimler_label.setText(_translate("MainWindow", "Resimler"))
        self.panolar_label.setText(_translate("MainWindow", "Panolar"))
        self.basliklar_dosya_buton.setText(_translate("MainWindow", "Dosyayı Seç"))
        self.rastgele_pin_checkbox.setText(_translate("MainWindow", "Verilen Değerlerden Rastgele Pinler Oluştur"))
        self.aciklamalar_dosya_buton.setText(_translate("MainWindow", "Dosyayı Seç"))
        self.linkler_dosya_buton.setText(_translate("MainWindow", "Dosyayı Seç"))
        self.resimler_dosya_buton.setText(_translate("MainWindow", "Dosyayı Seç"))
        self.panolar_dosya_buton.setText(_translate("MainWindow", "Dosyayı Seç"))
        self.resimler_klasor_buton.setText(_translate("MainWindow", "Klasörü Seç"))
        self.resim_indirici_buton.setText(_translate("MainWindow", "Resim İndirici Ayarları"))
        self.baslat_buton.setText(_translate("MainWindow", "Başlat"))
        self.kayit_buton.setText(_translate("MainWindow", "Kayıtlar"))
        self.manuel_buton.setText(_translate("MainWindow", "Manuel Pin Ekle"))
        self.proxy_buton.setText(_translate("MainWindow", "Proxy Ayarları"))

        self.functions = Functions(self)
        self.resim_indirici_buton.clicked.connect(partial(self.NorkQ_Downloader_Ac, self.functions))
        self.kayit_buton.clicked.connect(partial(self.NorkQ_Logger_Ac, self.functions))
        self.manuel_buton.clicked.connect(partial(self.NorkQ_Editor_Ac, self.functions))
        self.onayla_buton.clicked.connect(self.functions.anahtar_kontrol)
        self.proxy_buton.clicked.connect(partial(self.NorkQ_Proxy_Ac, self.functions))
        self.baslat_buton.clicked.connect(self.pinlemeye_basla)

        self.basliklar_dosya_buton.clicked.connect(partial(self.functions.metin_ac, self.basliklar_list))
        self.aciklamalar_dosya_buton.clicked.connect(partial(self.functions.metin_ac, self.aciklamalar_list))
        self.linkler_dosya_buton.clicked.connect(partial(self.functions.metin_ac, self.linkler_list))
        self.resimler_dosya_buton.clicked.connect(partial(self.functions.resim_ac, self.resimler_list))
        self.resimler_klasor_buton.clicked.connect(partial(self.functions.klasor_ac, self.resimler_list))
        self.panolar_dosya_buton.clicked.connect(partial(self.functions.metin_ac, self.panolar_list))

        self.basliklar_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.basliklar_list.customContextMenuRequested[QtCore.QPoint].connect(partial(self.sag_tik, self.basliklar_list))

        self.aciklamalar_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.aciklamalar_list.customContextMenuRequested[QtCore.QPoint].connect(partial(self.sag_tik, self.aciklamalar_list))

        self.linkler_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.linkler_list.customContextMenuRequested[QtCore.QPoint].connect(partial(self.sag_tik, self.linkler_list))

        self.resimler_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.resimler_list.customContextMenuRequested[QtCore.QPoint].connect(partial(self.sag_tik, self.resimler_list))

        self.panolar_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.panolar_list.customContextMenuRequested[QtCore.QPoint].connect(partial(self.sag_tik, self.panolar_list))


    #Thread fonksiyonları
    def pinlemeye_basla(self):
        basla = Thread(target=self.functions.pinlemeye_basla, daemon=True)
        basla.start()

    def indirmeye_basla(self, adet, adres):
        pin_adet = adet.value()
        pin_adres = adres.text()
        #self.kayit_ekle(pin_adet, pin_adres)
        basla = Thread(target=self.functions.indirmeye_basla, args=(pin_adet, pin_adres,))
        basla.start()

    def proxy_kontrol(self):
        kontrol = Thread(target=self.functions.proxy_kontrol, daemon=True, args=(self.proxy_ui.checkBox, self.proxy_ui.lineEdit,))
        kontrol.start()

    def sag_tik(self, liste):
        menu = QMenu(liste)
        sil_Action = menu.addAction("Sil")
        action = menu.exec_(QtGui.QCursor.pos())
        if action == sil_Action:
            self.functions.item_sil(liste)

    def flashSplash(self):
        self.splash = QSplashScreen(QPixmap('splash.png'))

        # By default, SplashScreen will be in the center of the screen.
        # You can move it to a specific location if you want:
        # self.splash.move(10,10)

        self.splash.show()

        # Close SplashScreen after 2 seconds (2000 ms)
        QTimer.singleShot(2000, self.splash.close)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.flashSplash()
    time.sleep(4)
    MainWindow.show()
    ui.functions.start()
    sys.exit(app.exec_())
