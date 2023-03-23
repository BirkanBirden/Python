print("""
Hesap Makinasi Uygulaması

İşlemler;

1. Toplama
2. Çıkarma
3. Bölme
4. Çarpma

""")

a = int( input("1. sayıyı giriniz: "))
b = int( input("2. sayıyı giriniz: "))
c = int( input("İşlem numarasını giriniz: "))

if  c == 1:
    print("{} ile {} toplamı {} " .format(a,b,a+b))

elif c == 2:
    print("{} ile {} çıkarması {} " .format(a,b,a-b))

elif c == 3 :
    print("{} ile {} bölümü {} " .format(a,b,a/b))

elif c == 4:
    print("{} ile {} çarpması {} " .format(a,b,a*b))

else:
    print("Geçersiz işlem")
