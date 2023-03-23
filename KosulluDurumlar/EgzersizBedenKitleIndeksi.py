print("""
Beden Kitle İndeksi
""")

boy = float( input( "Boyunuzu giriniz: " ))
kilo = int(input("Kilonuzu giriniz: " ))

BedenIndeks = kilo / (boy ** 2)

print("Beden Kitle İndeksiniz {} olarak hesaplanmıştır" .format(BedenIndeks))

if BedenIndeks >= 30 :
    print("Obez olduğunuz belirlenmiştir.")

elif 30 > BedenIndeks > 25 :
    print("Fazla Kilolu olduğunuz belirlenmiştir.")

elif 25 > BedenIndeks > 18.5 :
    print("Normal kiloda olduğunuz belirlenmiştir.")

elif 18.5 > BedenIndeks :
    print("Zayıf olduğunuz belirlenmiştir.")
