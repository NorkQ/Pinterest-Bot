from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, random
import sys

from Functions.Pin import Pin

class PinIslemleri():
    def __init__(self):
        self.driver = None

    # pin görevini başlatır.
    def pinlemeye_basla(self):
        self.pin_listesi = []
        self.tarayici_ac()

    #pinterest açılır.
    def tarayici_ac(self):
        self.kayit_ekle("Tarayıcı açılıyor...")
        try:
            self.driver = webdriver.Chrome("chromedriver.exe", chrome_options=self.options)
            self.driver.get('https://tr.pinterest.com/')
            self.kayit_ekle("Tarayıcı başarıyla açıldı")
        except:
            self.kayit_ekle("Tarayıcı açılırken bir sorun oluştu !")
            e = sys.exc_info()
            self.kayit_ekle(e)

        self.pinterest_giris_yap()

    #pintereste giriş yapılır.
    def pinterest_giris_yap(self):
        self.kayit_ekle("Pinterest girişi yapılıyor...")
        try:
            kullanici_adi = self.ui.kullanici_adi_entry.text()
            sifre = self.ui.sifre_entry.text()

            #Giriş elementleri bulunur, değerler girilir ve giriş yapılır.
            oturum_ac_buton = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.oturum_ac_buton_selector)))
            oturum_ac_buton.click()

            hosgeldin_yazi = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.hosgeldin_yazi_selector)))

            hosgeldin_yazi.click()

            email_entry = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.email_entry_selector)))

            pass_entry = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.pass_entry_selector)))

            giris_yap_buton = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.giris_yap_buton_selector)))

            email_entry.send_keys(kullanici_adi)
            pass_entry.send_keys(sifre)
            giris_yap_buton.click()
            self.kayit_ekle("Giriş yapıldı")
            self.kayit_ekle("Bekleniyor...")
            time.sleep(10)
            self.pinleri_sirala()
        except :
            self.kayit_ekle("Giriş yapılırken bir sorun oluştu !")
            e = sys.exc_info()
            self.kayit_ekle(e)

    #kullanıcının girdiği değerleri toplar ve bu değerlerden pin objeleri oluşturur.
    #sonra bu pin objelerine ulaşabilmek için yukarıda oluşturduğum listeye ekler.
    #daha sonra pin yükleme işlemini başlatır.
    def pinleri_sirala(self):
        basliklar = []
        aciklamalar = []
        linkler = []
        resimler = []
        panolar = []

        self.listeleri_getir(basliklar, self.ui.basliklar_list)
        self.listeleri_getir(aciklamalar, self.ui.aciklamalar_list)
        self.listeleri_getir(linkler, self.ui.linkler_list)
        self.listeleri_getir(resimler, self.ui.resimler_list)
        self.listeleri_getir(panolar, self.ui.panolar_list)

        if self.ui.rastgele_pin_checkbox.isChecked():
            pin_sayisi = len(resimler)
            basliklar = self.karistir(basliklar, pin_sayisi)
            aciklamalar = self.karistir(aciklamalar, pin_sayisi)
            panolar = self.pano_karistir(panolar, pin_sayisi)
            linkler = self.pano_karistir(linkler, pin_sayisi)

        sayilar = [len(basliklar), len(aciklamalar), len(resimler)]

        self.kayit_ekle("Pinler oluşturuluyor...")
        for i in range(0, min(sayilar)):
            pin = None
            if len(linkler) - 1 < i or len(panolar) - 1 < i:
                if len(linkler) - 1 < i and len(panolar) - 1 < i:
                    uretilen_pano = panolar[random.randint(0, len(panolar) - 1)]
                    uretilen_link = linkler[random.randint(0, len(linkler) - 1)]
                    pin = Pin(basliklar[i], aciklamalar[i], uretilen_link, resimler[i], uretilen_pano)
                else:
                    if len(linkler) - 1 < i:
                        uretildi_link = linkler[random.randint(0, len(linkler) - 1)]
                        pin = Pin(basliklar[i], aciklamalar[i], uretildi_link, resimler[i], panolar[i])
                    elif len(panolar) - 1 < i:
                        uretildi_pano = panolar[random.randint(0, len(panolar) - 1)]
                        pin = Pin(basliklar[i], aciklamalar[i], linkler[i], resimler[i], uretildi_pano)
            else:
                pin = Pin(basliklar[i], aciklamalar[i], linkler[i], resimler[i], panolar[i])
            self.pin_listesi.append(pin)
        self.kayit_ekle("Pinler oluşturuldu")
        self.kayit_ekle(len(self.pin_listesi))
        self.pinleri_yukle()

    #yukarıda oluşturulan listeyi çeker ve her pin objesi için ayrı ayrı
    #pin_olustur fonksiyonunu çalıştırır.
    def pinleri_yukle(self):
        self.kayit_ekle("Pinler yükleniyor...")
        id = 1
        for pin in self.pin_listesi:
            try:
                if self.atilan_pin_sayisi < int(self.ui.max_pin_entry.text()):
                    try:
                        self.kayit_ekle("Pin Builder sayfasına gidiliyor..")
                        self.driver.get("https://tr.pinterest.com/pin-builder/")
                    except:
                        self.kayit_ekle("Pin Builder sayfası getirilemedi. Tarayıcıyı tekrar başlatın")
                        break

                    self.pin_olustur(pin.baslik, pin.aciklama, pin.link, pin.resim, pin.pano, id)
                    #atılan pin sayısı pin grubu sayısının katıysa
                    if (self.atilan_pin_sayisi % int(self.ui.pin_grubu_sayisi_entry.text())) == 0:
                        #pin gruıpları arası bekleme
                        self.kayit_ekle((self.ui.pin_grubu_sayisi_entry.text() + " adet daha pin atıldı. " + self.ui.grup_arasi_entry.text() + " saniye bekleniyor..."))
                        time.sleep(int(self.ui.grup_arasi_entry.text()))
                    else:
                        #Kac saniyede bir pin atılsın ?
                        self.kayit_ekle("Sıradaki için " + self.ui.tek_aralik_entry.text() + " saniye bekleniyor...")
                        id += 1
                        time.sleep(int(self.ui.tek_aralik_entry.text()))
                else:
                    self.kayit_ekle("Günlük sınır aşıldı...")
                    self.pin_listesi = []
                    break
            except:
                e = sys.exc_info()
                self.kayit_ekle(e)
                self.kayit_ekle("Bu pin atılırken bir sorun oluştu. Sıradakine geçiliyor...")
                time.sleep(1)
                continue
        self.kayit_ekle("Pinler yüklendi")
        self.pin_listesi = []

    #pin-builder sayfasına gelindiğinde gerekli alanları doldurur ve yayınlar.
    def pin_olustur(self, baslik, aciklama, link, resim, pano, id):
        try:
            resim_yukle_giris = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.resim_yukle_giris_selector)))

            resim_yukle_giris.send_keys(resim)
            self.kayit_ekle("Görüntü başarıyla yüklendi")
        except:
            self.kayit_ekle("Görüntü yüklenirken bir sorun oluştu !")
            e = sys.exc_info()
            self.kayit_ekle(e)

        self.kayit_ekle("Başlık, açıklama ve internet sitesi girişleri alınıyor...")

        self.kayit_ekle("Panolar getiriliyor...")

        try:
            textareas = self.driver.find_elements_by_tag_name("textarea")

            baslik_giris = textareas[0]
            aciklama_giris = textareas[1]
            site_giris = textareas[2]
            self.kayit_ekle("Başlık açıklama ve internet sitesi girişleri alındı")

            baslik_giris.send_keys(baslik)
            aciklama_giris.send_keys(aciklama)
            site_giris.send_keys(link)

            self.kayit_ekle("Başlık, açıklama ve internet sitesi girildi")
        except:
            self.kayit_ekle("Pin oluşturulurken bir sorun oluştu !")
            e = sys.exc_info()
            self.kayit_ekle(e)

        self.kayit_ekle("Yukarı kaydırılıyor")
        self.driver.execute_script("window.scrollTo(0, 0);")
        self.kayit_ekle("Kaydırıldı")

        try:
            pano_sec_buton = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.pano_sec_buton_selector)))
            pano_sec_buton.click()
            self.kayit_ekle("Panolar getirildi.")
        except:
            self.kayit_ekle("Panolar getirilirken bir sorun oluştu !")
            e = sys.exc_info()
            self.kayit_ekle(e)

        self.kayit_ekle(pano + " panosu getiriliyor...")

        try:
            pin_panolar = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, self.pano_listesi_class)))
            time.sleep(1)

            for pin_pano in pin_panolar:
                panolar = pin_pano.find_elements_by_class_name(self.pano_class)

                for f_pano in panolar:
                    if f_pano.get_attribute("title") == pano:
                        f_pano.click()

            self.kayit_ekle(pano + " panosu getirildi")
        except:
            self.kayit_ekle(pano + " panosu getirilirken bir sorun oluştu !")
            e = sys.exc_info()
            self.kayit_ekle(e)

        try:
            kaydet_buton = self.driver.find_element_by_css_selector(self.kaydet_buton_selector)
            kaydet_buton.click()
            self.kayit_ekle("Kaydet butonu bulundu")
        except:
            self.kayit_ekle("Kaydet butonu bulunamadı")

        try:
            yayinla_buton = self.driver.find_element_by_css_selector(self.yayinla_buton_selector)
            yayinla_buton.click()
            self.kayit_ekle("Yayınla butonu bulundu")
        except:
            self.kayit_ekle("Yayınla butonu bulunamadı")


        #time.sleep(20)
        #self.atilan_pin_sayisi += 1
        #self.kayit_ekle(("Pin paylaşıldı --> " + str(id)))

        try:
            paylasildi_yazi = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, self.kaydedildi_yazi_path)))
            self.kayit_ekle(f"Pin paylaşıldı --> {id}")
            self.kayit_ekle("\n----------------------------------------------------------------\n")
            self.atilan_pin_sayisi += 1
        except:
            self.kayit_ekle("Pin paylaşımı zaman aşımına uğradı ya da pinterest tarafından reddedildi")
            self.kayit_ekle("\n----------------------------------------------------------------\n")
            self.atilan_pin_sayisi += 1
            e = sys.exc_info()
            self.kayit_ekle(e)
