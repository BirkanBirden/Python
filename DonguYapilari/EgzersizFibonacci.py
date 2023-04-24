print("""
Fibonacci serisi
************************


""")

a = 1
b = 1

fibonacci = [a,b]

for x in range(45):

    a,b = b,b+a

    fibonacci.append(b)

print(fibonacci)