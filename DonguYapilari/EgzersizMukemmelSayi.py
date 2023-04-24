print("*********************Mükemmel Sayı Bulma Programı**********************\n")

a = int(input("Bir sayı giriniz: "))
i = 1
toplam = 0


while (i < a ) :
    if (a % i ==0 ):
        toplam += i

    i += 1
if  (toplam == a):
    print(a , " Mükemmel sayıdır.")

else:
    print(a , " Mükemmel sayı değildir.")
