print("""
Faktoriyel

""")


def faktoriyel(sayi):

    faktoriyel1=1

    if(sayi == 0 or sayi ==1 ):

        return faktoriyel1
    else:
        while(sayi>1):
            faktoriyel1 *= sayi
            sayi -= 1
    return  faktoriyel1

while True:
    sayi=int(input("Sayı Giriniz: "))
    print(sayi, "sayısının faktoriyeli ", faktoriyel(sayi))