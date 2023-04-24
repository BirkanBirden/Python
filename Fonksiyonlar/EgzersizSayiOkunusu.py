print("""
--------------------------------------
Sayı Okunuşu
--------------------------------------
""")

birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]
#yuzler = ["","yüz","iki yüz","üç yüz","dört yüz","beş yüz","altı yüz","yedi yüz","sekiz yüz","dokuz yüz"]

def SayiOkunus(sayi):
    bir= sayi % 10
    iki = sayi //10
  # uc = sayi //100

    return  " "+ onlar[iki] + " " + birler[bir]


while True:
    sayi=int(input("Sayı Giriniz: "))

    print(SayiOkunus(sayi))