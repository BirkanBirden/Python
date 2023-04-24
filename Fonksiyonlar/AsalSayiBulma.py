print("""
----------------------------------------
Asal Sayı Bulma
----------------------------------------

""")

def AsalSayiBulma(sayi):
    if (sayi == 1):
        return False
    if (sayi== 2):
        return True
    else:
        for i in range(2,sayi):
            if (sayi % i == 0):
                return False
        return True


while True:
    sayi = input("Sayı Giriniz : ")

    if (sayi =="q"):
        break

    else:
        sayi = int(sayi)

        if (AsalSayiBulma(sayi)):
            print(sayi, "Asal sayıdır.")
        else :
            print(sayi, "Asal değildir")
