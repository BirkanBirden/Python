print("Yol hesaplayıcı")

a = float( input("Kullandığınız araç kilometrede ne kadar yakıyor? ") )
b = float( input("Kaç kilometre yol gidilecek? ") )

print("Gidilen {} km için toplamda {} TL yakıt parası ödemeniz gerekmektedir." .format(b,a*b))