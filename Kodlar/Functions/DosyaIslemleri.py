import glob
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
import sys
class DosyaIslemleri():
    #başlık, açıklama gibi değişkenler için kullanıcı txt dosyası seçebilecek.
    def metin_ac(self, liste):
        try:
            filename = QFileDialog.getOpenFileName(None, 'Open File', 'c:\\', "Text Files (*.txt)")
            file = open(filename[0], "r", encoding="utf-8")
            kelimeler = file.readlines()
            file.close()

            for kelime in kelimeler:
                liste.addItem(kelime.strip())
            self.kayit_ekle("Metin başarıyla açıldı.")
        except:
            self.kayit_ekle("Metin açılırken bir hata oluştu")
            e = sys.exc_info()
            self.kayit_ekle(e)

    def logo_sec(self, edit):
        filename = QFileDialog.getOpenFileName(None, 'Open File', 'c:\\', "Image Files (*.png *.jpg)")
        self.kayit_ekle(filename[0])
        edit.setText(filename[0])

    #burası klasör seçebilmek için. Klasördeki bütün resimleri getirebilirim.
    def klasor_ac(self, liste):
        try:
            foldername = QFileDialog.getExistingDirectory(None, 'Select Folder')
            files_png = [f for f in glob.glob(foldername + "**/*.png", recursive=True)]
            files_jpg = [f for f in glob.glob(foldername + "**/*.jpg", recursive=True)]

            files = files_jpg + files_png

            for f in files:
                liste.addItem(f)
            self.kayit_ekle("Klasör başarıyla açıldı.")
        except :
            self.kayit_ekle("Klasör açılırken bir hata oluştu !")
            e = sys.exc_info()
            self.kayit_ekle(e)

    #tek bir resim eklenmek istediği zaman
    def resim_ac(self, liste):
        try:
            filename = QFileDialog.getOpenFileName(None, 'Open File', 'c:\\',"Image Files (*.png *.jpg)")
            liste.addItem(filename[0])
            self.kayit_ekle("Görüntü başarıyla açıldı.")
        except :
            self.kayit_ekle("Görüntü açılırken bir hata oluştu !")
            e = sys.exc_info()
            self.kayit_ekle(e)

    #Manuel pin oluştur panceresindeki görüntü seç butonu
    def goruntu_sec(self):
        try:
            filename = QFileDialog.getOpenFileName(None, 'Open File', 'c:\\',"Image Files (*.png *.jpg)")
            self.goruntu = filename[0]
            pixmap = QPixmap(self.goruntu)
            self.ui.editor_ui.goruntu_view.setPixmap(QPixmap(pixmap))
            self.kayit_ekle("Görüntü başarıyla açıldı.")
        except :
            self.kayit_ekle("Görüntü açılırken bir hata oluştu !")
            e = sys.exc_info()
            self.kayit_ekle(e)

    #Resimler için indirme yolu seçer
    def indirme_yolu_sec(self, edit):
        try:
            foldername = QFileDialog.getExistingDirectory(None, 'Select Folder')
            self.kayit_ekle("Klasör başarıyla açıldı.")
            edit.setText(foldername)
            self.options.add_argument('--no-sandbox')
            prefs = {"profile.default_content_settings.popups": 0,
                         "download.default_directory": foldername, # IMPORTANT - ENDING SLASH V IMPORTANT
                         "directory_upgrade": True}
            self.options.add_experimental_option("prefs", prefs)
            self.resim_yolu = foldername
        except :
            self.kayit_ekle("Klasör açılırken bir hata oluştu !")
            e = sys.exc_info()
            self.kayit_ekle(e)