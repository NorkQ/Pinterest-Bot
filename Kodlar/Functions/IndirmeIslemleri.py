from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, cv2, sys
import numpy as np

class IndirmeIslemleri():
    def __init__(self):
        self.browser = None

    def indirmeye_basla(self, adet, adres):
        self.kayit_ekle("İndirmeye başlanıyor...")
        self.browser = None
        if "google" in adres:
            self.browser = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=self.options)
            self.browser.get(adres)
            self.kayit_ekle("Tarayıcı açıldı")
            self.google_resimleri_indir(adet)
        else:
            self.resimleri_indir(adres, adet, self.resim_yolu)

    def indirme_giris_yap(self, adet, adres):
        self.kayit_ekle("Pinterest girişi yapılıyor...")
        try:
            kullanici_adi = self.ui.kullanici_adi_entry.text()
            sifre = self.ui.sifre_entry.text()

            # Giriş elementleri bulunur, değerler girilir ve giriş yapılır.
            oturum_ac_buton = WebDriverWait(self.browser, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.oturum_ac_buton_selector)))
            oturum_ac_buton.click()

            hosgeldin_yazi = WebDriverWait(self.browser, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.hosgeldin_yazi_selector)))

            hosgeldin_yazi.click()

            email_entry = WebDriverWait(self.browser, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.email_entry_selector)))

            pass_entry = WebDriverWait(self.browser, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.pass_entry_selector)))

            giris_yap_buton = WebDriverWait(self.browser, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.giris_yap_buton_selector)))

            email_entry.send_keys(kullanici_adi)
            pass_entry.send_keys(sifre)
            giris_yap_buton.click()
            self.kayit_ekle("Giriş yapıldı")
        except:
            self.kayit_ekle("Giriş yapılırken bir sorun oluştu !")
            e = sys.exc_info()
            self.kayit_ekle(e)

        self.kayit_ekle("Bekleniyor...")
        time.sleep(10)
        self.resimleri_indir(adet, adres)

    def indirici(self, linkler):
        i = 0

        for link in linkler:
            self.kayit_ekle("\n----------------------------------------------------------------\n")

            uzantilar = [".png", ".jpg", ".webp"]
            yanlis_link = False
            uzanti = ""
            for uz in uzantilar:
                if uz in link:
                    uzanti = uz
                    uzantilar.remove(uz)

            try:
                self.kayit_ekle(f"Resim uzantısı --> {uzanti}")
                self.browser.get(link)
                WebDriverWait(self.browser, 3).until(
                    EC.presence_of_all_elements_located((By.TAG_NAME, 'img')))
                yanlis_link = False
            except:
                self.kayit_ekle(f"{uzanti} uzantısı yanlış olabilir. Sıradaki deneniyor...")
                for uz in uzantilar:
                    link = link.replace(uzanti, uz)
                    uzanti = uz
                    try:
                        self.kayit_ekle(f"Resim uzantısı --> {uz}")
                        self.browser.get(link)
                        WebDriverWait(self.browser, 3).until(
                            EC.presence_of_all_elements_located((By.TAG_NAME, 'img')))
                        yanlis_link = False
                        break
                    except:
                        self.kayit_ekle(f"{uz} uzantısı doğrulanamadı. Sıradakine geçiliyor...")
                        yanlis_link = True
                        continue


            if yanlis_link == True:
                # self.kayit_ekle("Link alınamadı. Sıradakine geçiliyor...")
                self.kayit_ekle(f"Bu link geçersiz --> {link}")
                continue

            else:
                yol = self.resim_yolu + "/" + "indirilen" + str(i) + ".png"
                try:
                    self.browser.save_screenshot(yol)
                    self.autocrop(yol)

                    self.kayit_ekle(f"indirildi - {i} --> " + link)
                    self.kayit_ekle(yol)
                    self.ui.resimler_list.addItem(yol)
                except:
                    self.kayit_ekle("Resim alınamadı yenisi getiriliyor...")
                    e = sys.exc_info()
                    self.kayit_ekle(e)
                    continue

                if self.ui.downloader_ui.filtre_ekle_check.isChecked():
                    try:
                        self.ozgunlestir(yol, self.ozgun_ayarlar["filtre"], self.ozgun_ayarlar["yazi"],
                                         self.ozgun_ayarlar["logo"])
                        self.kayit_ekle("Özgünleştirme başarılı")
                    except:
                        self.kayit_ekle("Özgünleştirme yapılamadı ya da eksik yapıldı. Sıradaki resme geçiliyor...")
                        e = sys.exc_info()
                        self.kayit_ekle(e)
                        continue

                i += 1
                time.sleep(2)

        self.browser.close()
        if self.ui.rastgele_pin_checkbox.isChecked():
            self.pinlemeye_basla()

    def google_resimleri_indir(self, adet):
        pin_linkler = []
        pinler = {}

        deger = 600
        son_deger = 0
        while len(pinler) < adet:
            taranan_pinler = WebDriverWait(self.browser, 20).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, 'img')))
            for taranan_pin in taranan_pinler:
                if len(pin_linkler) >= adet:
                    break
                if taranan_pin not in pinler and taranan_pin.get_attribute("class") == self.google_arama_resim_class:
                    try:
                        pinler[taranan_pin] = (taranan_pin.location["y"], taranan_pin.size["height"])
                        print(taranan_pin, pinler[taranan_pin])
                        time.sleep(0.2)
                        taranan_pin.click()
                        time.sleep(2.5)
                        resim = self.browser.find_element_by_class_name(self.google_resim_class)
                        pin_linkler.append(resim.get_attribute("src"))
                    except:
                        self.kayit_ekle("Bu resim getirilemedi. Sıradakine geçiliyor...")

                else:
                    continue
            self.browser.execute_script("window.scrollTo(0, {0});".format(son_deger + deger))
            height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if son_deger + deger >= height:
                self.kayit_ekle("Sayfada daha fazla resim yok !")
                break
            son_deger = son_deger + deger
            time.sleep(2)

        self.kayit_ekle("Pinler bulundu. Bulunan pin sayısı : " + str(len(pinler)))
        self.indirici(pin_linkler)

    def autocrop(self, img, threshold=100):
        """Crops any edges below or equal to threshold

        Crops blank image to 1x1.

        Returns cropped image.

        """
        image = cv2.imread(img)

        if len(image.shape) == 3:
            flatImage = np.max(image, 2)
        else:
            flatImage = image
        assert len(flatImage.shape) == 2

        rows = np.where(np.max(flatImage, 0) > threshold)[0]
        if rows.size:
            cols = np.where(np.max(flatImage, 1) > threshold)[0]
            image = image[cols[0]: cols[-1] + 1, rows[0]: rows[-1] + 1]
        else:
            image = image[:1, :1]

        cv2.imwrite(img, image)
