import pymysql.cursors
import time
import sys

hedef_saat = input("Hangi saatte azaltılsın : ")
saniye = input("Kaç saniye beklensin : ")
musteriler = None

print("Sunucuya bağlanılıyor...")
try:
    db = pymysql.connect(host='',
                         user='',
                         password='',
                         db='',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    baglanti = db.cursor()
    print("Bağlantı başarılı")
except:
    print("Sunucuya bağlanılamadı !")
    e = sys.exc_info()
    print(e)


print("Bağlantı kuruldu")
guncellendi = True

def sure_azalt(musteriler):
    for musteri in musteriler:
        musteri["sure"] -= 1

    return musteriler

def verileri_guncelle(musteriler):
    for musteri in musteriler:
        baglanti.execute(f"UPDATE musteriler SET sure = {int(musteri['sure'])} WHERE id = {int(musteri['id'])}")
        db.commit()
    print("Tüm kullanıcıların süresi 1 güna azaltıldı.")

while True:
    saat = time.strftime("%H:%M")
    if saat == hedef_saat:
        baglanti.execute('SELECT * FROM musteriler')
        musteriler = baglanti.fetchall()
        verileri_guncelle(sure_azalt(musteriler))
        time.sleep(int(saniye))
        print("80 saniye bekleniyor...")
    time.sleep(1)