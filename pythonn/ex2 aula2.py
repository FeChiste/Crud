inicio = 100
fim = 500

for numero in range(inicio, fim+1):
    if numero % 2 == 0 and numero % 5 == 0 and numero % 7 == 0:
        print(numero)
