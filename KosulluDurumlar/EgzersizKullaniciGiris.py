print("""
Kullanıcı Giriş Paneli
""")

sysKullaniciAdi = "Birkan"
sysySifre= "123"

kullaniciAdi = input("Kullanıcı Adını Giriniz: ")
sifre = input("Şifreyi giriniz: ")

if kullaniciAdi == sysKullaniciAdi and sifre != sysySifre:
    print("Parola Hatalı!!!!")

elif kullaniciAdi != sysKullaniciAdi and sifre == sysySifre:
    print("Hatalı Kullanıcı Adı")

elif kullaniciAdi != sysKullaniciAdi and sifre != sysySifre:
    print("Kullanıcı Adı ve Parola Hatalı")

else:
    print("Sisteme Giriş Yapılmıştır")













