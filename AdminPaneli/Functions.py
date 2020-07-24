from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql.cursors
import re, sys



class MatchDelegate(QtWidgets.QStyledItemDelegate):
    regex = re.compile('')
    fakeIndex = QtCore.QModelIndex()

    def paint(self, qp, option, index):
        self.initStyleOption(option, index)
        td = QtGui.QTextDocument()
        if self.regex.pattern:
            splitted = self.regex.split(option.text)
            matches = iter(self.regex.findall(option.text))
            text = ''
            for words in splitted[:-1]:
                text += words + '<b style="color : red; font-size:11px;">{}</b>'.format(next(matches))
            text += splitted[-1]
        else:
            text = option.text
        td.setHtml(text)
        option.text = ''
        # Using an invalid index avoids painting of the text
        QtWidgets.QStyledItemDelegate.paint(self, qp, option, self.fakeIndex)
        qp.save()
        qp.translate(option.rect.topLeft())
        td.drawContents(qp, QtCore.QRectF(0, 0, option.rect.width(), option.rect.height()))
        qp.restore()

class Functions():
    def __init__(self, ui):
        self.ui = ui
        self.delegate = MatchDelegate()
        self.baglanti = None
        self.db = None

        ui.tablo.setItemDelegate(self.delegate)
        self.veritabani_baglantisi()
        self.kullanicilari_cek()
        self.uyarilari_cek()
        self.elementleri_cek()

    def findText(self):
        text = self.ui.ara_edit.text()
        self.delegate.regex = re.compile(text, re.I)
        self.ui.tablo.viewport().update()

    def add_item(self, uye):
        l1 = QtWidgets.QTreeWidgetItem([uye[0], uye[1], uye[2], uye[3], uye[4], uye[5], uye[6]])
        l1.setFlags(l1.flags() | QtCore.Qt.ItemIsEditable)
        self.ui.tablo.addTopLevelItem(l1)

    def editItem(self):
        try:
            db_columns = ["id", "isim_soyisim", "email", "tel_no", "anahtar", "tarih", "sure"]

            items = self.ui.tablo.selectedItems()
            column = self.ui.tablo.currentColumn()

            duzenlenen_yazi = items[0].text(column)
            id = items[0].text(0)
            duzenlenen_sutun = db_columns[column]

            try:
                int(duzenlenen_yazi)
                duzenlenen_yazi = int(duzenlenen_yazi)
            except:
                duzenlenen_yazi = f"'{duzenlenen_yazi}'"
            self.baglanti.execute(f"UPDATE musteriler SET {duzenlenen_sutun}={duzenlenen_yazi} WHERE id={int(id)}")
            self.db.commit()
        except:
            print("İtem düzenlenirken bir sorun oluştu.")
            e = sys.exc_info()
            print(e)


    def findTextElem(self):
        text = self.ui.ara_edit_elem.text()
        self.delegate.regex = re.compile(text, re.I)
        self.ui.tablo_elem.viewport().update()

    def add_item_elem(self, elem):
        l1 = QtWidgets.QTreeWidgetItem([elem[0], elem[1]])
        l1.setFlags(l1.flags() | QtCore.Qt.ItemIsEditable)
        self.ui.tablo_elem.addTopLevelItem(l1)

    def editItem_elem(self):
        try:
            db_columns = ["degisken_ismi", "degisken_degeri"]

            items = self.ui.tablo_elem.selectedItems()
            column = self.ui.tablo_elem.currentColumn()

            duzenlenen_yazi = items[0].text(column)
            id = items[0].text(0)
            duzenlenen_sutun = db_columns[column]

            self.baglanti.execute(f"UPDATE elementler SET {duzenlenen_sutun}='{duzenlenen_yazi}' WHERE degisken_ismi='{id}'")
            self.db.commit()
        except:
            print("İtem düzenlenirken bir sorun oluştu.")
            e = sys.exc_info()
            print(e)


    def veritabani_baglantisi(self):
        print("Sunucuya bağlanılıyor...")
        try:
            self.db = pymysql.connect(host='',
                                 user='',
                                 password='',
                                 db='',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
            self.baglanti = self.db.cursor()
            print("Bağlantı başarılı")
        except:
            print("Sunucuya bağlanılamadı !")
            e = sys.exc_info()
            print(e)

    def uyarilari_cek(self):
        try:
            self.baglanti.execute('select * from uyarilar')
            uyarilar = self.baglanti.fetchall()

            self.ui.plainTextEdit.insertPlainText(uyarilar[0]["aciklama"])
        except:
            print("Kullanıcılar çekilirken bir sorun oluştu.")
            e = sys.exc_info()
            print(e)

    def kullanicilari_cek(self):
        try:
            self.baglanti.execute('select * from musteriler')
            musteriler = self.baglanti.fetchall()

            for i in range(len(musteriler)):
                uye = (str(musteriler[i]["id"]), str(musteriler[i]["isim_soyisim"]), str(musteriler[i]["email"]), str(musteriler[i]["tel_no"]), str(musteriler[i]["anahtar"]), str(musteriler[i]["tarih"]), str(musteriler[i]["sure"]))
                self.add_item(uye)
        except:
            print("Kullanıcılar çekilirken bir sorun oluştu.")
            e = sys.exc_info()
            print(e)

    def elementleri_cek(self):
        try:
            self.baglanti.execute('select * from elementler')
            elementler = self.baglanti.fetchall()

            for i in range(len(elementler)):
                uye = (str(elementler[i]["degisken_ismi"]), str(elementler[i]["degisken_degeri"]))
                self.add_item_elem(uye)
        except:
            print("Kullanıcılar çekilirken bir sorun oluştu.")
            e = sys.exc_info()
            print(e)

    def uye_ekle(self):
        try:
            bilgiler = {
                "isim_soyisim" : f"'{str(self.ui.isim_soyisim_edit.text())}'",
                "mail" : f"'{str(self.ui.mail_edit.text())}'",
                "tel_no" : f"'{str(self.ui.tel_no_edit.text())}'",
                "anahtar" : f"'{str(self.ui.anahtar_edit.text())}'",
                "sure" : int(self.ui.sure_edit.text())
            }

            self.baglanti.execute(f"INSERT INTO musteriler VALUES(NULL, {bilgiler['isim_soyisim']}, {bilgiler['mail']}, {bilgiler['tel_no']}, {bilgiler['anahtar']}, CURRENT_TIMESTAMP, {bilgiler['sure']})")
            self.db.commit()
            self.ui.tablo.clear()
            self.kullanicilari_cek()
        except:
            print("Üye eklenirken bir sorun oluştu.")
            e = sys.exc_info()
            print(e)


    def uyari_gonder(self):
        try:
            plain_text = self.ui.plainTextEdit
            text = plain_text.toPlainText()
            #text = text.split("\n")
            self.baglanti.execute(f'UPDATE uyarilar SET aciklama="{text}" WHERE id=1')
            self.db.commit()
        except:
            print("Uyarı gönderilirken bir sorun oluştu.")
            e = sys.exc_info()
            print(e)


"""Bu uyarıları uzaktan gönderiyorum ve önemli bilgiler vereceğim rehber niteliğinde. Bu yüzden okumayı ihmal etmemenizi tavsiye ediyorum.

Selamlar :)
Program şu an beta sürümdedir. Bazı hatalar kesinlikle olabilir. Amacımız bu hataları gidermek. Bu yüzden gördüğünüz hataları bana r10 üzerinden, skype : kihsan1543, ya da norkqstudio@gmail.com adresinden belirtirseniz beni ve diğer pinterest kullanıcılarını çok mutlu edeceksiniz :)

Bu arada yeni sürümlerde gelecek mükemmel özellikleri kaçırmamak için konuyu takip edebilirsin :)

Yeni eklenen özellikler:
- Özgünleştirme seçenekleri
    + Filtre ekleme ve renk seçme.
    + Yazı ekleme, font, renk, boyut,
    rotasyon ve pozisyon belirleme.
    + Logo ekleme, saydamlık, pozisyon,
    rotasyon, boyut belirleme.
    
- Googledan resim indirme
- Proxy kullanma (şifresiz)

**Şifreli proxy kullanımı çok yakında..."""

