print("değişken yer değiştirme")

a = input("1. değişken: ")
b = input("2. değişken: ")

a,b = b,a

print("Yer değişimi yapılmış ve ilk değer {} ve ikinci değer {} olarak kaydedilmiştir." .format(a,b))