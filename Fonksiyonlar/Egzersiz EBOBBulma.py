print("""
-------------------------
EBOB Bulma
-------------------------

""")

def EbobBulma(sayi1,sayi2):

    i=1
    ebob=1

    while(i <= sayi1 and  i <= sayi2):

        if ( not (sayi1 % i) and not  (sayi2 %i) ):
            ebob = i

        i +=1

    return ebob

while True:

    sayi1= int(input("Sayı Giriniz: "))
    sayi2 = int(input("2. Sayıyı Giriniz"))

    print("EBOB" , EbobBulma(sayi1,sayi2) )