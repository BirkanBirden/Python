print("""
Ders Notu Hesaplayıcı
""")

vize1 = float(input("Vize Notunuzu Giriniz: "))
vize2 = float(input("2. Vize Notunuzu Giriniz: "))
final = float(input("Fianl Notunuzu Giriniz: "))

genelNot= (vize1 * 3/10) + (vize2 * 3/10) + (final* 4/10)

if  genelNot >= 90 :
    print("AA")

elif  genelNot >= 85 :
    print("BA")

elif genelNot >= 80:
    print("BB")

elif  genelNot >= 75 :
    print("CB")

elif  genelNot >= 70 :
    print("CC")

elif  genelNot >= 65 :
    print("DC")

elif genelNot >= 60:
    print("DD")

elif genelNot >= 55:
    print("FD")

else:
    print("FF")



