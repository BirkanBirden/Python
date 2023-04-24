print("""
Faktoriyel bulma programı

*************************************
Programdan çıkmak için q tuşuna basınız
*************************************


""")

while True:

    a = input("Sayı Giriniz: ")

    if  (a == "q"):

        print("Programdan çıkılıyor......")
        break

    else:
        a = int(a)
        faktoriyel=1
    for   b in range (2,a+1) :
        faktoriyel *= b

    print(faktoriyel)