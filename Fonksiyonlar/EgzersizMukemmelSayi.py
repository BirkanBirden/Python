print("""
--------------------------------------
Egzersiz Mükemmel Sayı Bulma
--------------------------------------
""")

def MukemmelSayi(sayi):
    toplam = 0

    for i in range (1,sayi):
        if (sayi % i ==0):
            toplam += i
    return toplam ==sayi

while True:
    sayi = input("Sayı Giriniz: ")
    if (sayi == "q"):
        break

    sayi = int(sayi)

    if (MukemmelSayi(sayi)):
        print(sayi , "Mükemmel Sayıdır")
    else:
        print(sayi , "Mükemmel Sayı Değildir.")