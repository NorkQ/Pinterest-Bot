from selenium import webdriver
import pymysql.cursors
from PyQt5.QtWidgets import QMessageBox
import random
from datetime import datetime
import time
import sys

#Kendi paketlerim
from Functions.OzgunFonks import OzgunFunc
from Functions.DosyaIslemleri import DosyaIslemleri
from Functions.PinlemeIslemleri import PinIslemleri
from Functions.IndirmeIslemleri import IndirmeIslemleri
import Functions.pindown as pindown

#driver ve pin listesine her yerden ulaşabilmem gerektiği için onları burada oluşturdum.
#Bu arada ui elementlerinin değerlerine ulaşmam gerektiği için bir ui parametresi aldım.
#UI elementlerinin bulunduğu kodda bu sınıfı oluşturup parametre olarak kendisini atıyorum.
class Functions(DosyaIslemleri, OzgunFunc, PinIslemleri, IndirmeIslemleri):
    def __init__(self, ui):
        self.ui = ui
        self.kayitlar = []
        self.goruntu = ""
        self.resim_yolu = ""
        self.anahtarlar = []
        self.atilan_pin_sayisi = 0
        self.pin_listesi = []
        self.options = webdriver.ChromeOptions()
        self.file = "Kayitlar/"
        self.musteriler = None

        #element bulucu kodları
        self.oturum_ac_buton_selector = ""
        self.email_entry_selector = ""
        self.pass_entry_selector = ""
        self.giris_yap_buton_selector = ""
        self.resim_yukle_giris_selector = ""
        self.pano_sec_buton_selector = ""
        self.pano_listesi_class = ''
        self.pano_class = ''
        self.hosgeldin_yazi_selector = ''
        self.kaydet_buton_selector = ''
        self.yayinla_buton_selector = ''
        self.kaydedildi_yazi_path = ""
        self.google_resim_class = ""
        self.google_arama_resim_class = ""

    #program ilk başladığında bu fonksiyon çalışacak.
    def start(self):
        self.veritabani_baglantisi()
        time.sleep(1)
        self.anahtar_kontrol()
        self.uyari_al()


    def uyari_al(self):
        self.kayit_ekle("Uyarılar getiriliyor...")
        self.baglanti.execute('select * from uyarilar')
        veri = self.baglanti.fetchall()
        self.ui.NorkQ_Uyari_Ac(veri[len(veri) - 1]["aciklama"])
        self.kayit_ekle("Uyarılar getirildi")


    #müşteri anahtarlarını kontrol edebilmek için veritabanı bağlantısı yapıyorum.
    def veritabani_baglantisi(self):
        self.kayit_ekle("Sunucuya bağlanılıyor...")
        try:
            db = pymysql.connect(host='',
                                user='',
                                password='',
                                db='',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
            self.baglanti = db.cursor()
            self.kayit_ekle("Bağlantı başarılı")
        except :
            self.kayit_ekle("Sunucuya bağlanılamadı !")
            e = sys.exc_info()
            self.kayit_ekle(e)

        self.element_bulucular()

        self.baglanti.execute('SELECT * FROM musteriler')
        self.musteriler = self.baglanti.fetchall()
        for musteri in self.musteriler:
            self.anahtarlar.append(musteri["anahtar"])



    #müşteri anahtarı kontrolü için
    def anahtar_kontrol(self):
        self.kayit_ekle("Anahtar kontrol ediliyor...")
        anahtar = self.ui.anahtar_entry.text()


        self.baglanti.execute(f"SELECT * FROM musteriler where anahtar='{anahtar}'")
        musteri = self.baglanti.fetchall()

        if len(musteri) == 0:
            self.ui.pin_ayarlari_grup.setEnabled(False)
            self.ui.hesap_ayarlari.setEnabled(False)
            self.ui.pin_zaman_ayarlari.setEnabled(False)

            self.ui.proxy_buton.setEnabled(False)
            self.ui.baslat_buton.setEnabled(False)
            self.ui.resim_indirici_buton.setEnabled(False)
            self.ui.kayit_buton.setEnabled(False)
            self.ui.manuel_buton.setEnabled(False)
            self.kayit_ekle("Geçerli bir anahtar girmediniz")

        else:

            if musteri[0]["sure"] > 0:
                self.ui.pin_ayarlari_grup.setEnabled(True)
                self.ui.hesap_ayarlari.setEnabled(True)
                self.ui.pin_zaman_ayarlari.setEnabled(True)

                self.ui.proxy_buton.setEnabled(True)
                self.ui.baslat_buton.setEnabled(True)
                self.ui.resim_indirici_buton.setEnabled(True)
                self.ui.kayit_buton.setEnabled(True)
                self.ui.manuel_buton.setEnabled(True)

                self.kayit_ekle("Anahtar kabul edildi")
            else:
                self.ui.pin_ayarlari_grup.setEnabled(False)
                self.ui.hesap_ayarlari.setEnabled(False)
                self.ui.pin_zaman_ayarlari.setEnabled(False)

                self.ui.proxy_buton.setEnabled(False)
                self.ui.baslat_buton.setEnabled(False)
                self.ui.resim_indirici_buton.setEnabled(False)
                self.ui.kayit_buton.setEnabled(False)
                self.ui.manuel_buton.setEnabled(False)
                self.kayit_ekle("Üyelik süreniz dolmuştur")
                self.mesaj_goster("Uyarı", "Üyelik süreniz dolmuştur.", QMessageBox.Critical)

    def element_bulucular(self):
        # element bulucu kodları
        self.baglanti.execute("SELECT * FROM elementler where degisken_ismi='oturum_ac_buton_selector'")
        self.oturum_ac_buton_selector = self.baglanti.fetchone()["degisken_degeri"]

        self.baglanti.execute("SELECT * FROM elementler where degisken_ismi='email_entry_selector'")
        self.email_entry_selector = self.baglanti.fetchone()["degisken_degeri"]

        self.baglanti.execute("SELECT * FROM elementler where degisken_ismi='pass_entry_selector'")
        self.pass_entry_selector = self.baglanti.fetchone()["degisken_degeri"]

        self.baglanti.execute("SELECT * FROM elementler where degisken_ismi='giris_yap_buton_selector'")
        self.giris_yap_buton_selector = self.baglanti.fetchone()["degisken_degeri"]

        self.baglanti.execute("SELECT * FROM elementler where degisken_ismi='resim_yukle_giris_selector'")
        self.resim_yukle_giris_selector = self.baglanti.fetchone()["degisken_degeri"]

        self.baglanti.execute("SELECT * FROM elementler where degisken_ismi='pano_sec_buton_selector'")
        self.pano_sec_buton_selector = self.baglanti.fetchone()["degisken_degeri"]

        self.baglanti.execute("SELECT * FROM elementler where degisken_ismi='pano_listesi_class'")
        self.pano_listesi_class = self.baglanti.fetchone()["degisken_degeri"]

        self.baglanti.execute("SELECT * FROM elementler where degisken_ismi='pano_class'")
        self.pano_class = self.baglanti.fetchone()["degisken_degeri"]

        self.baglanti.execute("SELECT * FROM elementler where degisken_ismi='hosgeldin_yazi_selector'")
        self.hosgeldin_yazi_selector = self.baglanti.fetchone()["degisken_degeri"]

        self.baglanti.execute("SELECT * FROM elementler where degisken_ismi='kaydet_buton_selector'")
        self.kaydet_buton_selector = self.baglanti.fetchone()["degisken_degeri"]

        self.baglanti.execute("SELECT * FROM elementler where degisken_ismi='yayinla_buton_selector'")
        self.yayinla_buton_selector = self.baglanti.fetchone()["degisken_degeri"]

        self.baglanti.execute("SELECT * FROM elementler where degisken_ismi='kaydedildi_yazi_path'")
        self.kaydedildi_yazi_path = self.baglanti.fetchone()["degisken_degeri"]

        self.baglanti.execute("SELECT * FROM elementler where degisken_ismi='google_resim_class'")
        self.google_resim_class = self.baglanti.fetchone()["degisken_degeri"]

        self.baglanti.execute("SELECT * FROM elementler where degisken_ismi='google_arama_resim_class'")
        self.google_arama_resim_class = self.baglanti.fetchone()["degisken_degeri"]


    def proxy_kontrol(self, proxy_status, proxy):
        proxy_status = proxy_status.isChecked()
        proxy = proxy.text()

        if proxy_status:
            if proxy == "":
                self.kayit_ekle("Proxy girilmediği için çalıştırılamıyor !")
            else:
                try:
                    self.options.add_argument('--proxy-server=%s' %proxy)
                    self.kayit_ekle(f"Proxy kaydedildi --> {proxy}")
                    self.mesaj_goster("Bilgilendirme", "Proxy doğrulaması için https://whatismyipaddress.com/ adresine gidilecektir", QMessageBox.Information)
                    ip_driver = webdriver.Chrome("chromedriver.exe", chrome_options=self.options)
                    ip_driver.get("https://whatismyipaddress.com/")
                except:
                    self.kayit_ekle(f"Proxy çalıştırılırken bir sorun oluştu --> {proxy}")
                    e = sys.exc_info()
                    self.kayit_ekle(e)

    def mesaj_goster(self, baslik, metin, ikon):
        message_box = QMessageBox()
        message_box.setIcon(ikon)
        message_box.setText(metin)
        message_box.setWindowTitle(baslik)
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.setEscapeButton(QMessageBox.Ok)
        result = message_box.exec_()

    def resimleri_indir(self, terim, adet, yol):
        pindown.run(terim,adet,yol, self.ui, self)


    #arayüzdeki listeleri toparlar.
    def listeleri_getir(self, liste, list_widget):
        self.kayit_ekle("Listeler alınıyor...")
        for i in range(0, list_widget.count()):
            liste.append(list_widget.item(i).text())
        self.kayit_ekle("Listeler alındı")


    #Başlık ve açıklamaları rastgele dizer
    def karistir(self, liste, sayi):
        yeni_liste = []
        for i in range(0, sayi):
            max_random = len(liste)
            eleman = ""
            for i in range(0, 6):
                eleman += liste[random.randint(0, max_random - 1)].strip() + " "

            yeni_liste.append(eleman)
        self.kayit_ekle("Anahtar kelimeler karıştırıldı")
        return yeni_liste


    #Birden fazla pano varsa panoları karıştırır.
    def pano_karistir(self, liste, sayi):
        yeni_liste = []
        for i in range(0, sayi):
            max_random = len(liste)
            yeni_liste.append(liste[random.randint(0, max_random - 1)])

        self.kayit_ekle("Panolar karıştırıldı")
        return yeni_liste


    #Manuel pin penceresi
    def manuel_pin_olustur(self):
        try:
            baslik = self.ui.editor_ui.pin_basligi_entry.text()
            aciklama = self.ui.editor_ui.pin_aciklamasi_entry.toPlainText()
            link = self.ui.editor_ui.pin_link_entry.text()
            pano = self.ui.editor_ui.pano_ismi_entry.text()
            goruntu = self.goruntu

            if baslik != "":
                self.ui.basliklar_list.addItem(baslik)
            if aciklama != "":
                self.ui.aciklamalar_list.addItem(aciklama)
            if link != "":
                self.ui.linkler_list.addItem(link)
            if goruntu != "":
                self.ui.resimler_list.addItem(self.goruntu)
            if pano != "":
                self.ui.panolar_list.addItem(pano)
            self.kayit_ekle("Manuel pin oluşturuldu")
        except:
            self.kayit_ekle("Manuel pin oluşturulamadı !")
            e = sys.exc_info()
            self.kayit_ekle(e)


    def anahtar_ekle(self, entry, tur):
        deger = entry.text()
        if tur == "baslik":
            self.ui.basliklar_list.addItem(deger)
        elif tur == "aciklama":
            self.ui.aciklamalar_list.addItem(deger)
        elif tur == "link":
            self.ui.linkler_list.addItem(deger)
        elif tur == "pano":
            self.ui.panolar_list.addItem(deger)


    def anahtar_sil(self, entry, tur):
        deger = entry.text()
        try:
            if tur == "baslik":
                item = self.item_kontrol(deger, self.ui.basliklar_list)
                self.ui.basliklar_list.takeItem(item)
            elif tur == "aciklama":
                item = self.item_kontrol(deger, self.ui.aciklamalar_list)
                self.ui.aciklamalar_list.takeItem(item)
            elif tur == "link":
                item = self.item_kontrol(deger, self.ui.linkler_list)
                self.ui.linkler_list.takeItem(item)
            elif tur == "pano":
                item = self.item_kontrol(deger, self.ui.panolar_list)
                self.ui.panolar_list.takeItem(item)
        except:
            self.kayit_ekle("Anahtar kelime silinirken bir sorun oluştu")
            e = sys.exc_info()
            self.kayit_ekle(e)


    def liste_temizle(self, liste):
        liste.clear()
        self.pin_listesi = []
        self.kayit_ekle("Liste temizlendi")

    def item_kontrol(self, deger, liste):
        items = []
        for i in range(liste.count()):
            items.append(liste.item(i).text())
        self.kayit_ekle(items)

        for item in items:
            if deger == item:
                return items.index(deger)



    def kayitlari_getir(self, text_edit):
        for kayit in self.kayitlar:
            text_edit.appendPlainText(kayit)


    def kayit_ekle(self, mesaj):
        tarih = datetime.now()
        dosya_ismi = (f"{str(tarih.year)}-{str(tarih.month)}-{str(tarih.day)}-{str(tarih.hour)}-{str(tarih.minute)}")
        tarih = str(tarih)
        mesaj = str(mesaj)
        print(mesaj + f"    ({tarih})")
        self.kayitlar.append(mesaj + f"    ({tarih})")

        self.kayit_dosyasi = open((self.file + dosya_ismi + ".txt"), "a", encoding="utf-8")
        self.kayit_dosyasi.write(mesaj + "\n")
        self.kayit_dosyasi.close()

    def item_sil(self, liste):
        listItems = liste.selectedItems()
        if not listItems: return
        for item in listItems:
            liste.takeItem(liste.row(item))









