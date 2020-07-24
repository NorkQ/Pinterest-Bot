#Pin yüklerken pin bilgilerini ayrı ayrı çekebilmek için bu sınıfı oluşturdum.
class Pin():
    def __init__(self, baslik, aciklama, link, resim, pano):
        self.baslik = baslik
        self.aciklama = aciklama
        self.link = link
        self.resim = resim
        self.pano = pano

    def __str__(self):
        return (self.baslik, self.aciklama, self.link, self.resim, self.pano)