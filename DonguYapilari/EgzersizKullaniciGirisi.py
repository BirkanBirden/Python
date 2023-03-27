print("""
----------------------------------
Kullanıcı Girişi
----------------------------------
""")

sys_kullaniciAdi = "Birkan"
sys_parola = "123"
girisHakki = 3
bitir = 0

while True:
    kullaniciAdi = input("Kullanıcı Adı:")
    parola = input("Parola")

    if  (kullaniciAdi == sys_kullaniciAdi and parola != sys_parola) :
        print("Parolanız hatalı\n")
        girisHakki -= 1

    elif (kullaniciAdi != sys_kullaniciAdi and parola == sys_parola) :
        print("Hatalı kullanıcı adı\n")
        girisHakki -= 1

    elif (kullaniciAdi != sys_kullaniciAdi and parola != sys_parola) :
        print("kullanıcı adı ve parola hatalı\n")
        girisHakki -= 1

    else :
        print("Başarıyla giriş yapılmıştır\n")
        break

    if (girisHakki ==0):
        print("Giriş Hakkınız bitmiştir. Kullanıcı adınızı biliyorsanız şifrenizi sıfırlayınız!!\n")
        kullaniciAdi2 = input("Kullanıcı adı\n")


        if (kullaniciAdi2 == sys_kullaniciAdi):
            sys_parola = input("Şifrenizi giriniz: ")
            girisHakki=2
            bitir=1

            print("Şifreniz değişmiştir\n")
            continue

        else:
            print("hatalı\n")
        break

    if (bitir == 1):
        print("Hatalı girişler sonucu program kapanmıştır.\n")
        break

