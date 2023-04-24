print("""
---------------------------------
Sayı Tahmin Oyunu
---------------------------------

""")

import random
import time


rastgeleSayi = random.randint(1,20)
tahminHakki=10

while True:

    tahmin= int(input("Tahmininizi Giriniz: "))

    if(tahmin > rastgeleSayi):
        print("Bilgiler Sorgulanıyor.....")
        time.sleep(1)
        print("Daha düşük bir sayı söyleyiniz!!!")

        tahminHakki -=1

    elif (tahmin < rastgeleSayi):
        print("Bilgiler Sorgulanıyor....")
        time.sleep(2)
        print("Daha yüksek bir sayı söyleyiniz!!!")

        tahminHakki-=1

    else:
        print("Bilgiler Sorgulanıyor....")
        time.sleep(3)
        print("Tebrikler Doğru Tahmin ettiniz!!!!!")
        print("Sayı " , rastgeleSayi)
        break

    if (tahminHakki == 0):
        print("Üzgünüm tahmin hakkınız kalmadı :(")
        print("Sayımız ", rastgeleSayi)
        break