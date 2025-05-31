class Kitap:
    def __init__(self, ad, yazar, yil):
        self.ad = ad.strip()
        self.yazar = yazar.strip()
        self.yil = yil.strip()

    def __str__(self):
        return f"{self.ad} - {self.yazar} ({self.yil})"


class Kutuphane:
    def __init__(self):
        self.kitaplar = []

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)
        print(f"\n'{kitap.ad}' başarıyla kütüphaneye eklendi.")

    def kitap_sil(self, ad):
        ad = ad.strip()
        for kitap in self.kitaplar:
            if kitap.ad.lower() == ad.lower():
                self.kitaplar.remove(kitap)
                print(f"\n'{ad}' başarıyla silindi.")
                return
        print(f"\n'{ad}' kütüphanede bulunamadı.")

    def kitap_bul_isim(self, ad):
        ad = ad.strip()
        bulunan_kitaplar = [kitap for kitap in self.kitaplar if ad.lower() in kitap.ad.lower()]
        if bulunan_kitaplar:
            print("\nBulunan kitaplar:")
            for kitap in bulunan_kitaplar:
                print(f"{kitap}")
        else:
            print(f"\n'{ad}' adında bir kitap bulunamadı.")

    def kitap_bul_yazar(self, yazar):
        yazar = yazar.strip()
        bulunan_kitaplar = [kitap for kitap in self.kitaplar if yazar.lower() in kitap.yazar.lower()]
        if bulunan_kitaplar:
            print("\nBu yazara ait bulunan kitaplar:")
            for kitap in bulunan_kitaplar:
                print(f"{kitap}")
        else:
            print(f"\n'{yazar}' adlı yazara ait bir kitap bulunamadı.")

    def kitaplari_listele(self):
        if self.kitaplar:
            print("\nKütüphanedeki kitaplar:")
            for kitap in self.kitaplar:
                print(f"{kitap}")
        else:
            print("\nKütüphane şu anda boş.")

def main():
    kutuphane = Kutuphane()
    print("\nKütüphane Yönetim Sistemine Hoş Geldiniz!")

    while True:
        print("\n***** Menü *****")
        print("1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Kitap Ara (İsim ile)")
        print("4. Kitap Ara (Yazar ile)")
        print("5. Tüm Kitapları Listele")
        print("6. Çıkış")
        secim = input("Bir işlem seçin (1-6): ").strip()

        if secim == "1":
            ad = input("Kitap adı: ")
            yazar = input("Yazar: ")
            yil = input("Yayın yılı: ")
            kutuphane.kitap_ekle(Kitap(ad, yazar, yil))

        elif secim == "2":
            ad = input("Silmek istediğiniz kitabın adı: ")
            kutuphane.kitap_sil(ad)

        elif secim == "3":
            ad = input("Aramak istediğiniz kitabın adı: ")
            kutuphane.kitap_bul_isim(ad)

        elif secim == "4":
            yazar = input("Aramak istediğiniz yazarın adı: ")
            kutuphane.kitap_bul_yazar(yazar)

        elif secim == "5":
            kutuphane.kitaplari_listele()

        elif secim == "6":
            print("\nKütüphaneden çıkılıyor...")
            break

        else:
            print("\nGeçerli olmayan seçim! Lütfen 1-6 arasında bir sayı girin.")

main()
