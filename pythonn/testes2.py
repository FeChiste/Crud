n = int(input("Digite o valor de n: "))

a, b = 0, 1
for i in range(n):
    print(b, end=' ')
    a, b = b, a + b
