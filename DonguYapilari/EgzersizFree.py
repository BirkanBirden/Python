print("*********************Mükemmel Sayı Bulma Programı**********************\n")


sayi = int( input("Sayı giriniz : "))
a = 1
toplam = 0
b = 1
while True:
    if(b==0):
        sayi2 = int (input("Yeniden sayı giriniz: "))
        sayi = sayi2
        b = 1

    elif (a < sayi) :
        if (sayi % a ==0 ) :
            toplam += a
        a += 1

    elif (toplam == sayi):
        print(sayi , " Mükemmel sayıdır")
        a = 1
        toplam = 0
        b = 0
        continue
    else:
        print(sayi , " Mükemmel sayı değildir")
        a = 1
        toplam = 0
        b = 0
        continue