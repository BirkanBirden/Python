print("""
ATM makinasına hoşgeldiniz.

İŞLEMLER
-----------------------------
1- Bakiye Sorgulama
2- Para Yatırma
3- Para Çekme
4- Çıkış işlemi
-----------------------------

""")
bakiye = 1000

while True:

    islem = int( input("İşlem Numarası giriniz.") )
    if  (islem == 4):
        print("Sağlıklı günler dileriz.")
        break

    elif (islem == 1 ):
        print("Bakiyeniz {} TL" .format(bakiye))

    elif (islem == 2):
        yeniPara = int( input("Yatırılacak miktarı giriniz: ") )
        bakiye += yeniPara

        print("Yeni bakiyeniz {} TL olmuştur." .format(bakiye))

    elif (islem == 3):
        paraCek = int( input("Çekilecek miktarı giriniz: ") )
        if (bakiye - paraCek < 0 ):
            print("Yetersiz limit")
            continue
        else:
            bakiye -= paraCek
            print("Kalan bakiye {} TL" .format(bakiye))
    else:
        print("Geçersiz İşlem")








