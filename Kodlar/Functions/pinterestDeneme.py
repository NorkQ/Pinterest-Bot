import time, cv2, sys, re, requests
import numpy as np
from bs4 import BeautifulSoup
import urllib3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import cv2
import sys
import numpy as np

"https://i.pinimg.com/originals/16/cb/65/16cb65d0ffc38982e6dd7df442fcbf11.jpg"
"https://i.pinimg.com/236x/16/cb/65/16cb65d0ffc38982e6dd7df442fcbf11.jpg"

a = "16/cb/65/16cb65d0ffc38982e6dd7df442fcbf11.jpg"
b = "16/cb/65/16cb65d0ffc38982e6dd7df442fcbf11.jpg"

iskelet = "https://i.pinimg.com/"
string = "https://i.pinimg.com/200x/b7/d4/47/b7d447d6e6e5eeafda680fd9a419260b.jpg"
string = string.replace(iskelet, "")
print(f'"{string}"')
string = string.split("/")
string[0] = "originals"

link = iskelet
for oge in string:
    link += oge + "/"

link = link.rstrip("/")
print(link)

if a == b:
    print(True)


"""        self.browser.get(adres)

        bulunan_resimler = list()
        linkler = list()
        bitti = False

        son_deger = 0
        deger = 500

        id = 1
        #Resimleri bul
        while True:
            if bitti == True:
                break
            else:
                taranan_pinler = WebDriverWait(self.browser, 20).until(
                    EC.presence_of_all_elements_located((By.TAG_NAME, 'img')))
                self.kayit_ekle(len(taranan_pinler))
                for taranan_pin in taranan_pinler:
                    if taranan_pin not in bulunan_resimler:
                        try:
                            string = taranan_pin.get_attribute("src")
                            iskelet = "https://i.pinimg.com/"
                            string = string.replace(iskelet, "")
                            string = string.split("/")
                            string[0] = "originals"

                            link = iskelet
                            for oge in string:
                                link += oge + "/"

                            link = link.rstrip("/")
                            linkler.append(link)
                            bulunan_resimler.append(taranan_pin)

                        except:
                            self.kayit_ekle(f"Bu link getirilemedi. Sıradakine geçiliyor... --> {id}")
                            continue

                        if len(bulunan_resimler) >= adet:
                            break
                        id += 1
                time.sleep(1)

                if len(bulunan_resimler) < adet:
                    self.browser.execute_script("window.scrollTo(0, {0});".format(son_deger + deger))
                    son_deger += deger

                    yukseklik = self.browser.execute_script("return document.documentElement.scrollHeight")
                    if son_deger >= yukseklik:
                        self.kayit_ekle("Daha fazla pin bulunamadı")
                        bitti = True
                        break
                else:
                    self.kayit_ekle(f"Tarama tamamlandı {bulunan_resimler}")
                    bitti = True
                    break

        self.indirici(linkler)"""


"""
pins = WebDriverWait(self.browser, 20).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, 'img')))

            for pin in pins:
                if not pin in pinler:
                    if len(pinler) < adet:
                        try:
                            self.kayit_ekle("\n----------------------------------------------------------------\n")
                            pin.click()
                            time.sleep(1)
                            string = WebDriverWait(self.browser, 10).until(
                                EC.presence_of_element_located((By.CLASS_NAME, "n3VNCb")))
                            string = string.get_attribute("src")
                            pin_linkler.append(string)
                            pinler.append(pin)
                        except:
                            self.kayit_ekle("Resim getirilemedi. Sıradakine geçiliyor...")
                            e = sys.exc_info()
                            self.kayit_ekle(e)
                            continue
"""














"""

browser = webdriver.Chrome(executable_path="chromedriver.exe")
browser.get(r"https://tr.pinterest.com/search/pins/?q=k%C3%B6pek%20resimleri&rs=rs&eq=&etslf=2630&term_meta[]=k%C3%B6pek%7Crecentsearch%7C0&term_meta[]=resimleri%7Crecentsearch%7C0")

pinler = []
        pin_linkler = []

        deger = 600
        son_deger = 0
        while len(pinler) < adet:
            pins = WebDriverWait(browser, 20).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, 'img')))
            for pin in pins:
                if not pin in pinler:
                    if len(pinler) < adet:
                        try:
                            pinler.append(pin)
                            string = pin.get_attribute('srcset')
                            print(string)
                            string = string.split(",")
                            string = string[len(string) - 1]
                            string = string.strip()
                            string = string.split(" ")
                            string = string[0]
                            print(string)
                            print("\n\n")
                            pin_linkler.append(string)
                        except:
                            kayit_ekle("Resim getirilemedi. Sıradakine geçiliyor...")
                            e = sys.exc_info()
                            kayit_ekle(e)
                            continue
            browser.execute_script("window.scrollTo(0, {0});".format(son_deger + deger))
            height = browser.execute_script("return document.documentElement.scrollHeight")
            if son_deger+deger >= height:
                kayit_ekle("Sayfada daha fazla resim yok !")
                break
            son_deger = son_deger + deger
            time.sleep(2)"""