inicio = 0
fim = 1000
divisor = float(input("Digite um número: "))

for numero in range(inicio, fim):
    if numero % divisor == 0:
        print(numero)
