import cv2
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import numpy as np
import sys

class OzgunFunc():
    def __init__(self):
        self.ozgun_ayarlar = None

    def yazi_ekle(self, resim, text, renk=(0, 0, 0) + (255,), font="arial.ttf", size=6, pozisyon="solust", rotasyon=0):
        image = None
        if type(resim) is np.ndarray:
            resim = cv2.cvtColor(resim, cv2.COLOR_BGR2RGBA)
            image = Image.fromarray(resim).convert("RGB")
        else:
            image = Image.open(resim)
        font_type = ImageFont.truetype(font, 150)
        overlay = Image.new('RGBA', font_type.getsize(text), (0, 0, 0) + (0,))

        draw = ImageDraw.Draw(overlay)
        draw.text(xy=(0, 0), text=text, fill=renk, font=font_type)

        overlay = overlay.rotate(rotasyon, expand=1)

        width, height = image.size
        width = width / size
        oran = (overlay.size[0] / overlay.size[1])
        height = (width * (oran ** -1))
        overlay = overlay.resize((int(width), int(height)))

        pozisyon = self.pozisyon_getir(pozisyon, image, overlay)
        image.paste(overlay, box=pozisyon, mask=overlay)

        image = np.array(image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)

        return image

    def reduce_opacity(self, im, opacity):
        """Returns an image with reduced opacity."""
        assert opacity >= 0 and opacity <= 1
        if im.mode != 'RGBA':
            im = im.convert('RGBA')
        else:
            im = im.copy()
        alpha = im.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
        im.putalpha(alpha)
        im = Image.fromarray(cv2.cvtColor(np.asarray(im), cv2.COLOR_BGR2RGBA))
        return im

    def add_logo(self, resim, logo, pos="solust", size=5, rotation=0, alpha=255):
        mainim = None
        if type(resim) is np.ndarray:
            mainim = Image.fromarray(resim).convert("RGB")
        else:
            mainim = cv2.imread(resim)
            mainim = Image.fromarray(mainim).convert("RGB")
        logoim = Image.open(logo).convert("RGBA")
        logoim = logoim.rotate(rotation, expand=1)

        logoim = self.reduce_opacity(logoim, alpha / 255.0)

        # Calculate size
        width, height = mainim.size
        width = width / size
        oran = (logoim.size[0] / logoim.size[1])
        height = (width * (oran ** -1))
        logoim = logoim.resize((int(width), int(height)))

        if mainim.mode != 'RGBA':
            mainim.convert('RGBA')
        layer = Image.new('RGBA', mainim.size, (0, 0, 0, 0))
        layer.paste(logoim, self.pozisyon_getir_resim(pos, mainim, logoim))

        image = Image.composite(layer, mainim, layer)
        image = np.array(image)
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)

        return image

    def pozisyon_getir(self, pozisyon, image, overlay):
        pozisyonlar = {
            "solust": (10, 10),
            "ortaust": (int((image.width / 2) - (overlay.size[0] / 2)), 10),
            "sagust": (int((image.width) - (overlay.size[0] + 10)), 10),
            "solorta": (10, int(((image.height / 2) - (overlay.size[1] / 2)))),
            "orta": (
            int(((image.width / 2) - (overlay.size[0] / 2))), int(((image.height / 2) - (overlay.size[1] / 2)))),
            "sagorta": (int((image.width) - (overlay.size[0] + 10)), int(((image.height / 2) - (overlay.size[1] / 2)))),
            "solalt": (10, int(((image.height) - (overlay.size[1] + 10)))),
            "ortaalt": (int((image.width / 2) - (overlay.size[0] / 2)), int(((image.height) - (overlay.size[1] + 10)))),
            "sagalt": (int((image.width) - (overlay.size[0] + 10)), int(((image.height) - (overlay.size[1] + 10))))
        }

        return int(pozisyonlar[pozisyon][0]), int(pozisyonlar[pozisyon][1])

    def pozisyon_getir_resim(self, pozisyon, image, overlay):
        pozisyonlar = {
            "solust": (10, 10),
            "ortaust": (int((image.width / 2) - (overlay.size[0] / 2)), 10),
            "sagust": (int((image.width) - (overlay.size[0] + 10)), 10),
            "solorta": (10, int(((image.height / 2) - (overlay.size[1] / 2)))),
            "orta": (
            int(((image.width / 2) - (overlay.size[0] / 2))), int(((image.height / 2) - (overlay.size[1] / 2)))),
            "sagorta": (int((image.width) - (overlay.size[0] + 10)), int(((image.height / 2) - (overlay.size[1] / 2)))),
            "solalt": (10, int(((image.height) - (overlay.size[1] + 10)))),
            "ortaalt": (int((image.width / 2) - (overlay.size[0] / 2)), int(((image.height) - (overlay.size[1] + 10)))),
            "sagalt": (int((image.width) - (overlay.size[0] + 10)), int(((image.height) - (overlay.size[1] + 10))))
        }

        return pozisyonlar[pozisyon]

    def filtre_ekle(self, yol, renk, instensity=0.5):
        image = yol
        resim = self.apply_sepia(image, instensity, renk)
        # cv2.imwrite(yol, resim)
        # kayit_ekle("Filtre eklendi.")
        return resim

    def verify_alpha_channel(self, frame):
        try:
            frame.shape[3]
        except IndexError:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        return frame

    def apply_sepia(self, resim, instensity=0.5, color=(255, 255, 255)):
        frame = None
        if type(resim) is np.ndarray:
            frame = resim
            self.kayit_ekle("Ön izleme")
        else:
            frame = cv2.imread(resim)
            self.kayit_ekle("İndirme")
        frame = self.verify_alpha_channel(frame)
        frame_h, frame_w, frame_c = frame.shape
        sepia_bgra = color + (255,)
        overlay = np.full((frame_h, frame_w, 4), sepia_bgra, dtype="uint8")
        cv2.addWeighted(overlay, instensity, frame, 1.0, 0, frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
        return frame

    def renk_cevirici_filtre(self, renk):
        renk = renk
        renk = list(renk)
        renk.pop()
        renk = renk[::-1]
        renk = tuple(renk)
        return renk

    def pozisyon_cevirici(self, pozstr):
        if pozstr == "Sol Üst":
            return "solust"
        elif pozstr == "Sol Orta":
            return "solorta"
        elif pozstr == "Sol Alt":
            return "solalt"
        elif pozstr == "Orta Üst":
            return "ortaust"
        elif pozstr == "Orta":
            return "orta"
        elif pozstr == "Orta Alt":
            return "ortaalt"
        elif pozstr == "Sağ Üst":
            return "sagust"
        elif pozstr == "Sağ Orta":
            return "sagorta"
        elif pozstr == "Sağ Alt":
            return "sagalt"

    def ozgunlestir(self, yol, filtre, yazi, logo):
        if filtre:
            renk = self.ozgun_ayarlar["filtre_rengi"]
            renk = list(renk)
            renk.pop()
            renk = renk[::-1]
            renk = tuple(renk)
            cv2.imwrite(yol, self.filtre_ekle(yol, instensity=0.5, renk=renk))
        if yazi:
            text = self.ozgun_ayarlar["yazi_metni"]
            renk = self.ozgun_ayarlar["yazi_rengi"]
            size = self.ozgun_ayarlar["yazi_boyut"]
            rotasyon = self.ozgun_ayarlar["yazi_rotasyon"]
            konum = self.pozisyon_cevirici(self.ozgun_ayarlar["yazi_konum"])
            font = self.ozgun_ayarlar["yazi_font"]
            cv2.imwrite(yol, self.yazi_ekle(yol, text, renk=renk, size=size, rotasyon=rotasyon, pozisyon=konum, font=font))
        if logo:
            logoim = self.ozgun_ayarlar["logo_yolu"]
            pos = self.pozisyon_cevirici(self.ozgun_ayarlar["logo_konum"])
            size = self.ozgun_ayarlar["logo_boyut"]
            rotasyon = self.ozgun_ayarlar["logo_rotasyon"]
            alpha = self.ozgun_ayarlar["logo_saydamlik"]
            cv2.imwrite(yol, self.add_logo(resim=yol, logo=logoim, pos=pos, size=size, rotation=rotasyon, alpha=alpha))

    def ozgunlestir_on_izleme(self, yol, filtre, yazi, logo):
        image = cv2.imread(yol)
        if filtre:
            renk = self.renk_cevirici_filtre(self.ozgun_ayarlar["filtre_rengi"])
            image = self.filtre_ekle(image, instensity=0.5, renk=renk)
        if yazi:
            text = self.ozgun_ayarlar["yazi_metni"]
            renk = self.ozgun_ayarlar["yazi_rengi"]
            size = self.ozgun_ayarlar["yazi_boyut"]
            rotasyon = self.ozgun_ayarlar["yazi_rotasyon"]
            konum = self.pozisyon_cevirici(self.ozgun_ayarlar["yazi_konum"])
            font = self.ozgun_ayarlar["yazi_font"]
            image = self.yazi_ekle(image, text, renk=renk, size=size, rotasyon=rotasyon, pozisyon=konum, font=font)
        if logo:
            logoim = self.ozgun_ayarlar["logo_yolu"]
            pos = self.pozisyon_cevirici(self.ozgun_ayarlar["logo_konum"])
            size = self.ozgun_ayarlar["logo_boyut"]
            rotasyon = self.ozgun_ayarlar["logo_rotasyon"]
            alpha = self.ozgun_ayarlar["logo_saydamlik"]
            image = self.add_logo(resim=image, logo=logoim, pos=pos, size=size, rotation=rotasyon, alpha=alpha)

        cv2.imshow("On Izleme", image)
