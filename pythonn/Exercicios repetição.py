# Exercício 1

nota = float(input("Digite uma nota entre zero e dez: "))

while nota < 0 or nota > 10:
    print("Valor inválido. Digite novamente.")
    nota = float(input("Digite uma nota entre zero e dez: "))

print("Nota válida:", nota)

# Exercício 2

while True:
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if senha == nome_usuario:
        print("Erro: A senha não pode ser igual ao nome de usuário. Tente novamente.")
    else:
        break

print("Nome de usuário:", nome_usuario)
print("Senha:", senha)

# Exercício 3

nome = input("Digite seu nome: ")
while len(nome) <= 3:
    nome = input("Nome inválido. Digite novamente: ")

idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    idade = int(input("Idade inválida. Digite novamente: "))

salario = float(input("Digite seu salário: "))
while salario <= 0:
    salario = float(input("Salário inválido. Digite novamente: "))

sexo = input("Digite seu sexo (f/m): ")
while sexo != 'f' and sexo != 'm':
    sexo = input("Sexo inválido. Digite novamente (f/m): ")

estado_civil = input("Digite seu estado civil (s/c/v/d): ")
while estado_civil not in ['s', 'c', 'v', 'd']:
    estado_civil = input("Estado civil inválido. Digite novamente (s/c/v/d): ")

# Exercício 4


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

print("O maior número é:", maior)

# Exercício 5

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print("O maior número é:", maior)
print("O menor número é:", menor)

# Exercício 6

valor_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(
    input("Digite o número de horas trabalhadas no mês: "))

salario = valor_hora * horas_trabalhadas
print("O total do seu salário neste mês é:", salario)

# Exercício 7

fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

celsius = 5 * ((fahrenheit - 32) / 9)
print("A temperatura em graus Celsius é:", celsius)

# Exercício 8

celsius = float(input("Digite a temperatura em graus Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32
print("A temperatura em graus Fahrenheit é:", fahrenheit)

# Exercício 9


raio = float(input("Digite o raio do círculo: "))

area = math.pi * raio ** 2
print("A área do círculo é:", area)

# Exercício 10

base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))

area = (base * altura) / 2
print("A área do triângulo é:", area)

# Exercício 11

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = float(input("Digite um número real: "))

resultado_a = (2 * num1) * (num2 / 2)
resultado_b = (3 * num1) + num3
resultado_c = num3 ** 3

print("Resultado a:", resultado_a)
print("Resultado b:", resultado_b)
print("Resultado c:", resultado_c)

# Exercício 12

peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

imc = peso / altura ** 2
print("Seu IMC é:", imc)

# Exercício 13

valor = float(input("Digite um valor monetário: "))

novo_valor = valor * 1.15
print("O novo valor é R$", novo_valor)

# Exercício 14

valor = float(input("Digite um valor monetário: "))

novo_valor = valor * 0.9
print("O novo valor é R$", novo_valor)

# Exercício 15

valor_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(
    input("Digite o número de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas
imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - imposto_renda - inss - sindicato

print("Salário Bruto: R$", salario_bruto)
print("Imposto de Renda (11%): R$", imposto_renda)
print("INSS (8%): R$", inss)
print("Sindicato (5%): R$", sindicato)
print("Salário Líquido: R$", salario_liquido)

# Exercício 16

tamanho_arquivo = float(
    input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_internet = float(
    input("Digite a velocidade do link de Internet (em Mbps): "))

tempo_download = tamanho_arquivo / (velocidade_internet / 8) / 60
print("O tempo aproximado de download é de", tempo_download, "minutos")

# Exercício 17

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano", ano, "é bissexto")
else:
    print("O ano", ano, "não é bissexto")

# Exercício 18

data = input("Digite uma data no formato dd/mm/aaaa: ")

dia, mes, ano = map(int, data.split('/'))

data_valida = True

if dia < 1 or dia > 31:
    data_valida = False
elif mes < 1 or mes > 12:
    data_valida = False
elif mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        if dia > 29:
            data_valida = False
    elif dia > 28:
        data_valida = False
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
    data_valida = False

if data_valida:
    print("A data", data, "é válida")
else:
    print("A data", data, "não é válida")

# Exercício 19

num = int(input("Digite um número inteiro positivo: "))

if num >= 0:
    for i in range(num + 1):
        print(i)
else:
    print("O número digitado não é válido")

# Exercício 20

num = int(input("Digite um número inteiro positivo: "))

fibonacci = [0, 1]

while fibonacci[-1] < num:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

for termo in fibonacci:
    if termo <= num:
        print(termo)
    else:
        break

# Exercício 21

num = int(input("Digite um número inteiro positivo: "))

if num > 1:
    primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break
else:
    primo = False

if primo:
    print("O número", num, "é primo")
else:
    print("O número", num, "não é primo")

# Exercício 22

N = int(input("Digite a quantidade de números primos desejada: "))

count = 0
num = 2

while count < N:
    primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break
    if primo:
        print(num)
        count += 1
    num += 1

# Exercício 23

num = int(input("Digite um número inteiro positivo: "))

if num >= 2:
    for n in range(2, num + 1):
        primo = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                primo = False
                break
        if primo:
            print(n)
else:
    print("O número digitado não é válido")

# Exercício 24

N = int(input("Digite a quantidade de números naturais desejada: "))

soma = 0

for i in range(1, N + 1):
    soma += i

print("A soma dos", N, "primeiros números naturais é:", soma)

# Exercício 25

num = int(input("Digite um número inteiro positivo: "))

soma = 0

for i in range(1, num + 1, 2):
    soma += i

print("A soma dos números naturais ímpares até", num, "é:", soma)

# Exercício 26

num = int(input("Digite um número inteiro positivo: "))

for n in range(2, num + 1):
    soma_divisores = 0
    for i in range(1, n):
        if n % i == 0:
            soma_divisores += i
    if soma_divisores == n:
        print(n)

# Exercício 27

num = int(input("Digite um número inteiro positivo: "))

num_str = str(num)
num_digitos = len(num_str)

soma_digitos = 0

for digito in num_str:
    soma_digitos += int(digito) ** num_digitos

if soma_digitos == num:
    print("O número", num, "é um número de Armstrong")
else:
    print("O número", num, "não é um número de Armstrong")

# Exercício 28

N = int(input("Digite a quantidade de números de Fibonacci desejada: "))

fibonacci = [0, 1]

for i in range(2, N):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

for termo in fibonacci:
    print(termo)

# Exercício 29

num = int(input("Digite um número inteiro positivo: "))

p = 2

while 2 ** p - 1 < num:
    p_primo = True
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            p_primo = False
            break
    if p_primo and (2 ** p - 1) == num:
        print("O número", num, "é um número primo de Mersenne")
        break
    p += 1
else:
    print("O número", num, "não é um número primo de Mersenne")

# Exercício 30


def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


num = int(input("Digite um número inteiro positivo: "))

num_str = str(num)

soma_fatoriais = 0

for digito in num_str:
    soma_fatoriais += fatorial(int(digito))

if soma_fatoriais == num:
    print("O número", num, "é um número de Euler")
else:
    print("O número", num, "não é um número de Euler")
# Exercício 31


def calcular_quadrado_digitos(num):
    soma_quadrados = 0
    while num != 0:
        digito = num % 10
        soma_quadrados += digito ** 2
        num //= 10
    return soma_quadrados


def verificar_felicidade(num):
    while num != 1 and num != 4:
        num = calcular_quadrado_digitos(num)
    if num == 1:
        return True
    return False


num = int(input("Digite um número inteiro positivo: "))

if verificar_felicidade(num):
    print("O número", num, "é um número feliz")
else:
    print("O número", num, "não é um número feliz")

# Exercício 32

num = int(input("Digite um número inteiro positivo: "))

while num != 1:
    print(num)
    if num % 2 == 0:
        num //= 2
    else:
        num = num * 3 + 1

print(num)

# Exercício 33


def verificar_numero_lucas(num):
    a, b = 2, 1
    if num == a or num == b:
        return True
    while b < num:
        a, b = b, a + b
        if b == num:
            return True
    return False


num = int(input("Digite um número inteiro positivo: "))

if verificar_numero_lucas(num):
    print("O número", num, "é um número de Lucas")
else:
    print("O número", num, "não é um número de Lucas")

# Exercício 34


def verificar_numero_tetranacci(num):
    seq_tetranacci = [0, 0, 0, 1]
    if num in seq_tetranacci:
        return True
    while seq_tetranacci[-1] < num:
        seq_tetranacci.append(sum(seq_tetranacci[-4:]))
        if seq_tetranacci[-1] == num:
            return True
    return False


num = int(input("Digite um número inteiro positivo: "))

if verificar_numero_tetranacci(num):
    print("O número", num, "é um número tetranacci")
else:
    print("O número", num, "não é um número tetranacci")

# Exercício 35


def verificar_numero_perrin(num):
    seq_perrin = [3, 0, 2]
    if num in seq_perrin:
        return True
    while seq_perrin[-1] < num:
        seq_perrin.append(seq_perrin[-2] + seq_perrin[-3])
        if seq_perrin[-1] == num:
            return True
    return False


num = int(input("Digite um número inteiro positivo: "))

if verificar_numero_perrin(num):
    print("O número", num, "é um número de Perrin")
else:
    print("O número", num, "não é um número de Perrin")

# Exercício 36


def verificar_numero_triangular(num):
    soma = 0
    i = 1
    while soma < num:
        soma += i
        if soma == num:
            return True
        i += 1
    return False


num = int(input("Digite um número inteiro positivo: "))

if verificar_numero_triangular(num):
    print("O número", num, "é um número triangular")
else:
    print("O número", num, "não é um número triangular")

# Exercício 37


def verificar_quadrado_perfeito(num):
    raiz_quadrada = int(num ** 0.5)
    if raiz_quadrada ** 2 == num:
        return True
    return False


num = int(input("Digite um número inteiro positivo: "))

if verificar_quadrado_perfeito(num):
    print("O número", num, "é um número quadrado perfeito")
else:
    print("O número", num, "não é um número quadrado perfeito")

# Exercício 38


def verificar_cubo_perfeito(num):
    raiz_cubica = int(num ** (1/3))
    if raiz_cubica ** 3 == num:
        return True
    return False


num = int(input("Digite um número inteiro positivo: "))

if verificar_cubo_perfeito(num):
    print("O número", num, "é um número cúbico perfeito")
else:
    print("O número", num, "não é um número cúbico perfeito")

# Exercício 39


def verificar_palindromo(num):
    str_num = str(num)
    if str_num == str_num[::-1]:
        return True
    return False


num = int(input("Digite um número inteiro positivo: "))

if verificar_palindromo(num):
    print("O número", num, "é um número palíndromo")
else:
    print("O número", num, "não é um número palíndromo")

# Exercício 40


def verificar_numero_armstrong(num):
    str_num = str(num)
    n = len(str_num)
    soma = sum(int(digito) ** n for digito in str_num)
    if soma == num:
        return True
    return False


num = int(input("Digite um número inteiro positivo: "))

if verificar_numero_armstrong(num):
    print("O número", num, "é um número de Armstrong")
else:
    print("O número", num, "não é um número de Armstrong")

# Exercício 41


def verificar_numero_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


num = int(input("Digite um número inteiro positivo: "))

if verificar_numero_primo(num):
    print("O número", num, "é um número primo")
else:
    print("O número", num, "não é um número primo")

# Exercício 42


def verificar_numero_perfeito(num):
    soma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            soma_divisores += i
    if soma_divisores == num:
        return True
    return False


num = int(input("Digite um número inteiro positivo: "))

if verificar_numero_perfeito(num):
    print("O número", num, "é um número perfeito")
else:
    print("O número", num, "não é um número perfeito")

# Exercício 43


def verificar_numero_abundante(num):
    soma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            soma_divisores += i
    if soma_divisores > num:
        return True
    return False


num = int(input("Digite um número inteiro positivo: "))

if verificar_numero_abundante(num):
    print("O número", num, "é um número abundante")
else:
    print("O número", num, "não é um número abundante")

# Exercício 44


def verificar_numero_deficiente(num):
    soma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            soma_divisores += i
    if soma_divisores < num:
        return True
    return False


num = int(input("Digite um número inteiro positivo: "))

if verificar_numero_deficiente(num):
    print("O número", num, "é um número deficiente")
else:
    print("O número", num, "não é um número deficiente")

# Exercício 45


def verificar_numero_quadrado_livre(num):
    for i in range(2, int(num ** 0.5) + 1):
        if i ** 2 > 1 and num % (i ** 2) == 0:
            return False
    return True


num = int(input("Digite um número inteiro positivo: "))

if verificar_numero_quadrado_livre(num):
    print("O número", num, "é um número quadrado livre")
else:
    print("O número", num, "não é um número quadrado livre")

# Exercício 46


def verificar_numero_primo_mersenne(num):
    if num < 2:
        return False
    exp = 1
    mersenne = 2 ** exp - 1
    while mersenne < num:
        exp += 1
        mersenne = 2 ** exp - 1
    if mersenne == num:
        return True
    return False


num = int(input("Digite um número inteiro positivo: "))

if verificar_numero_primo_mersenne(num):
    print("O número", num, "é um número primo de Mersenne")
else:
    print("O número", num, "não é um número primo de Mersenne")

# Exercício 47


def verificar_numero_primo_fermat(num):
    if num < 2:
        return False
    exp = 0
    fermat = 2 ** (2 ** exp) + 1
    while fermat < num:
        exp += 1
        fermat = 2 ** (2 ** exp) + 1
    if fermat == num:
        return True
    return False


num = int(input("Digite um número inteiro positivo: "))

if verificar_numero_primo_fermat(num):
    print("O número", num, "é um número primo de Fermat")
else:
    print("O número", num, "não é um número primo de Fermat")

# Exercício 48


def verificar_numero_perfeito_euler(num):
    if num < 2:
        return False
    exp = 0
    mersenne = 2 ** exp - 1
    euler = (2 ** (exp - 1)) * mersenne
    while euler < num:
        exp += 1
        mersenne = 2 ** exp - 1
        euler = (2 ** (exp - 1)) * mersenne
    if euler == num:
        return True
    return False


num = int(input("Digite um número inteiro positivo: "))

if verificar_numero_perfeito_euler(num):
    print("O número", num, "é um número perfeito de Euler")
else:
    print("O número", num, "não é um número perfeito de Euler")

# Exercício 49


def verificar_numero_quase_perfeito(num):
    for i in range(1, num):
        soma_divisores = 0
        if num % i == 0:
            soma_divisores += i
            for j in range(i + 1, num):
                if num % j == 0:
                    soma_divisores += j
                if soma_divisores == num:
                    return True
    return False


num = int(input("Digite um número inteiro positivo: "))

if verificar_numero_quase_perfeito(num):
    print("O número", num, "é um número quase perfeito")
else:
    print("O número", num, "não é um número quase perfeito")

# Exercício 50


def calcular_soma_quadrados(num):
    soma = 0
    while num > 0:
        digito = num % 10
        soma += digito ** 2
        num = num // 10
    return soma


def verificar_numero_feliz(num):
    while True:
        num = calcular_soma_quadrados(num)
        if num == 1:
            return True
        elif num == 4:
            return False


num = int(input("Digite um número inteiro positivo: "))

if verificar_numero_feliz(num):
    print("O número", num, "é um número feliz")
else:
    print("O número", num, "não é um número feliz")

# Exercício 51


def calcular_serie(n):
    soma = 0.0
    m = 1
    for i in range(1, n+1):
        termo = i / m
        soma += termo
        m += 2
    return soma


n = int(input("Digite o número de termos da série: "))

resultado = calcular_serie(n)

print("A soma da série é:", resultado)
