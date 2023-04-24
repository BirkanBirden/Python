print("""
EKOK Bulma
""")


def EKOKBulma(sayi1,sayi2):
    i=2
    ekok=1

    while True:
        if ( sayi1 % i == 0 and sayi2 % i ==0):
            ekok *= i

            sayi1 //= i
            sayi2 //= i


        elif (sayi1 % i == 0 and sayi2 % i != 0):
            ekok *= i

            sayi1 //=i

        elif (sayi1 % i != 0 and sayi2 % i == 0):
            ekok *= i

            sayi2 //= i

        else:
            i += 1
        if (sayi1 == 1 and sayi2 == 1):
            break
    return ekok

while True:
    sayi1 = int(input("1. Sayıyı Giriniz: "))
    sayi2= int(input("2. Sayıyı Giriniz"))

    print("EKOK: ", EKOKBulma(sayi1,sayi2))