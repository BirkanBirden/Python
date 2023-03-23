print("""
Geometrik şekil hesaplayıcı
""")

cevap = input("Hangi şeklin tipi gerekiyor (Üçgen mi Dörtgen mi) ")

if  cevap == "Dörtgen" :
    print("Kenarları sırayla girmeniz gerekmektedir.")
    a =float( input("1.kenar :") )
    b = float( input("2.kenar :") )
    c = float( input("3.kenar :") )
    d = float( input("4.kenar :") )

    if  a==b and a==c and a==d :
        print("Şekil karedir")

    if  a==c and b==d:
        print("Dikdörtgen")
    else:
        print("Dörtgen")

if cevap =="Üçgen":
    print("Kenarları sırayla girmeniz gerekmektedir.")
    a = float(input("1.kenar :"))
    b = float(input("2.kenar :"))
    c = float(input("3.kenar :"))

    if abs(a+b)>c and (a+c)>b and (b+c)> a :
        if  a==b and a==c:
            print("Eşkenar üçgen")

        elif (a==b and a !=c) or (a==c and a !=b) or (b==c and b!=a):
            print("İkizkenar")

        else:
            ("Çeşitkenar")

    else:
        print("Üçgen belirtmiyor")


else:
    print("Geçersiz cevap")