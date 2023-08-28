# //Lista Estruturas de decisão:

# Ex:1
import math
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Verifica qual número é maior
if num1 > num2:
    maior = num1
else:
    maior = num2

# Imprime o maior número
print("O maior número é:", maior)


# Ex:2
valor = float(input("Digite um valor: "))

# Verifica se o valor é positivo, negativo ou zero
if valor > 0:
    print("O valor é positivo.")
elif valor < 0:
    print("O valor é negativo.")
else:
    print("O valor é zero.")


# Ex:3
# Solicita ao usuário que digite uma letra
letra = input("Digite uma letra (F/M): ")

# Converte a letra para maiúscula para evitar problemas de comparação
letra = letra.upper()

# Verifica a letra digitada e imprime a mensagem correspondente
if letra == "F":
    print("F - Feminino")
elif letra == "M":
    print("M - Masculino")
else:
    print("Sexo Inválido")


# Ex:4
# Solicita ao usuário que digite uma letra
letra = input("Digite uma letra: ")

# Converte a letra para minúscula para evitar problemas de comparação
letra = letra.lower()

# Verifica se a letra é uma vogal ou uma consoante e imprime a mensagem correspondente
if letra in "aeiou":
    print("A letra digitada é uma vogal.")
elif letra.isalpha():
    print("A letra digitada é uma consoante.")
else:
    print("O caractere digitado não é uma letra.")


# Ex:5
# Solicita ao usuário que digite as notas parciais
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média
media = (nota1 + nota2) / 2

# Verifica a média alcançada e imprime a mensagem correspondente
if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")


# Ex:6
# Solicita ao usuário que digite três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Verifica o maior número entre os três
maior = num1

if num2 > maior:
    maior = num2

if num3 > maior:
    maior = num3

# Imprime o maior número
print("O maior número é:", maior)


# Ex:7
# Solicita ao usuário que digite três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Inicializa as variáveis de maior e menor
maior = num1
menor = num1

# Verifica o maior e o menor número entre os três
if num2 > maior:
    maior = num2

if num3 > maior:
    maior = num3

if num2 < menor:
    menor = num2

if num3 < menor:
    menor = num3

# Imprime o maior e o menor número
print("O maior número é:", maior)
print("O menor número é:", menor)


# Ex:8
# Solicita ao usuário que digite o preço de três produtos
preco1 = float(input("Digite o preço do primeiro produto: "))
preco2 = float(input("Digite o preço do segundo produto: "))
preco3 = float(input("Digite o preço do terceiro produto: "))

# Verifica qual produto é o mais barato
if preco1 <= preco2 and preco1 <= preco3:
    print("O primeiro produto é o mais barato.")
elif preco2 <= preco1 and preco2 <= preco3:
    print("O segundo produto é o mais barato.")
else:
    print("O terceiro produto é o mais barato.")


# Ex:9
# Solicita ao usuário que digite três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Armazena os números em uma lista
numeros = [num1, num2, num3]

# Ordena a lista em ordem decrescente
numeros.sort(reverse=True)

# Imprime os números em ordem decrescente
print("Os números em ordem decrescente são:", numeros)


# Ex:10
# Solicita ao usuário que digite o turno de estudo
turno = input(
    "Em que turno você estuda? Digite M para Matutino, V para Vespertino ou N para Noturno: ")

# Verifica o turno digitado e imprime a mensagem apropriada
if turno.upper() == "M":
    print("Bom Dia!")
elif turno.upper() == "V":
    print("Boa Tarde!")
elif turno.upper() == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")


# Ex:11
# Solicita ao usuário que digite o salário atual do colaborador
salario_atual = float(input("Digite o salário atual do colaborador: "))

# Define os critérios de reajuste
if salario_atual <= 280.00:
    percentual_reajuste = 20
elif salario_atual <= 700.00:
    percentual_reajuste = 15
elif salario_atual <= 1500.00:
    percentual_reajuste = 10
else:
    percentual_reajuste = 5

# Calcula o valor do aumento
aumento = salario_atual * percentual_reajuste / 100

# Calcula o novo salário com o aumento
novo_salario = salario_atual + aumento

# Imprime as informações do reajuste
print("Salário antes do reajuste: R$", salario_atual)
print("Percentual de aumento aplicado: ", percentual_reajuste, "%")
print("Valor do aumento: R$", aumento)
print("Novo salário: R$", novo_salario)


# Ex:12
# Solicita ao usuário o valor da hora e a quantidade de horas trabalhadas
valor_hora = float(input("Digite o valor da hora de trabalho: "))
horas_trabalhadas = float(
    input("Digite a quantidade de horas trabalhadas no mês: "))

# Calcula o salário bruto
salario_bruto = valor_hora * horas_trabalhadas

# Define os critérios de desconto do Imposto de Renda
if salario_bruto <= 900.00:
    ir_percentual = 0
elif salario_bruto <= 1500.00:
    ir_percentual = 5
elif salario_bruto <= 2500.00:
    ir_percentual = 10
else:
    ir_percentual = 20

# Calcula o valor do desconto de Imposto de Renda
ir_desconto = salario_bruto * ir_percentual / 100

# Calcula o valor do desconto do INSS (fixo em 3%)
inss_desconto = salario_bruto * 3 / 100

# Calcula o valor do FGTS (fixo em 11%)
fgts = salario_bruto * 11 / 100

# Calcula o total de descontos
total_descontos = ir_desconto + inss_desconto

# Calcula o salário líquido
salario_liquido = salario_bruto - total_descontos

# Imprime as informações da folha de pagamento
print("Salário Bruto: R$ {:.2f}".format(salario_bruto))
print("(-) IR ({}%): R$ {:.2f}".format(ir_percentual, ir_desconto))
print("(-) INSS (3%): R$ {:.2f}".format(inss_desconto))
print("FGTS (11%): R$ {:.2f}".format(fgts))
print("Total de descontos: R$ {:.2f}".format(total_descontos))
print("Salário Líquido: R$ {:.2f}".format(salario_liquido))

# Ex:13
# Solicita ao usuário um número correspondente ao dia da semana
numero_dia = int(
    input("Digite um número de 1 a 7 correspondente ao dia da semana: "))

# Verifica o valor digitado e exibe o dia da semana correspondente
if numero_dia == 1:
    print("Domingo")
elif numero_dia == 2:
    print("Segunda-feira")
elif numero_dia == 3:
    print("Terça-feira")
elif numero_dia == 4:
    print("Quarta-feira")
elif numero_dia == 5:
    print("Quinta-feira")
elif numero_dia == 6:
    print("Sexta-feira")
elif numero_dia == 7:
    print("Sábado")
else:
    print("Valor inválido")


# Ex:14
# Solicita as duas notas parciais ao usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média das notas
media = (nota1 + nota2) / 2

# Determina o conceito correspondente
conceito = None
if media >= 9.0 and media <= 10.0:
    conceito = "A"
elif media >= 7.5 and media < 9.0:
    conceito = "B"
elif media >= 6.0 and media < 7.5:
    conceito = "C"
elif media >= 4.0 and media < 6.0:
    conceito = "D"
else:
    conceito = "E"

# Exibe as notas, a média e o conceito correspondente
print("Nota 1: ", nota1)
print("Nota 2: ", nota2)
print("Média: ", media)
print("Conceito: ", conceito)

# Verifica se o aluno está aprovado ou reprovado
if conceito in ["A", "B", "C"]:
    print("APROVADO")
else:
    print("REPROVADO")


# Ex:15
# Solicita os 3 lados do triângulo ao usuário
lado1 = float(input("Digite o valor do primeiro lado: "))
lado2 = float(input("Digite o valor do segundo lado: "))
lado3 = float(input("Digite o valor do terceiro lado: "))

# Verifica se os lados formam um triângulo
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    # Verifica o tipo de triângulo
    if lado1 == lado2 == lado3:
        print("Os lados formam um triângulo equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Os lados formam um triângulo isósceles.")
    else:
        print("Os lados formam um triângulo escaleno.")
else:
    print("Os lados não formam um triângulo.")

# Ex: 16

a = float(input("Digite o valor de a: "))
if a == 0:
    print("O valor de a não pode ser zero. O programa será encerrado.")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = b**2 - 4*a*c

    if delta < 0:
        print("A equação não possui raízes reais. O programa será encerrado.")
    elif delta == 0:
        raiz = -b / (2*a)
        print("A equação possui uma raiz real: {}".format(raiz))
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print("A equação possui duas raízes reais:")
        print("Raiz 1: {}".format(raiz1))
        print("Raiz 2: {}".format(raiz2))

# Ex: 17

ano = int(input("Digite um ano: "))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print(ano, "é um ano bissexto.")
else:
    print(ano, "não é um ano bissexto.")

 # Ex: 18

dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

validade = False

if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
    if (dia <= 31):
        validade = True
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    if (dia <= 30):
        validade = True
elif (mes == 2):

    if ((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)):
        if (dia <= 29):
            validade = True
        elif (dia <= 28):
            validade = True
elif (mes > 12):
    validade = False

if (validade == True):
    print("Data Válida")
else:
    print("Data Inválida")

# Ex: 19

numero = int(input("Digite um número inteiro menor que 1000: "))

if numero >= 1000:
    print("Número inválido. Digite um número menor que 1000.")
else:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = (numero % 100) % 10

    resultado = ""

    if centenas > 0:
        resultado += f"{centenas} {'centena' if centenas == 1 else 'centenas'}"

    if dezenas > 0:
        if resultado:
            resultado += ", "

        resultado += f"{dezenas} {'dezena' if dezenas == 1 else 'dezenas'}"

    if unidades > 0:
        if resultado:
            resultado += " e "

        resultado += f"{unidades} {'unidade' if unidades == 1 else 'unidades'}"

    print(resultado)

# Ex: 20

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media == 10:
    print("Aprovado com Distinção. Média:", media)
elif media >= 7:
    print("Aprovado. Média:", media)
else:
    print("Reprovado. Média:", media)

# Ex: 21

solicitacao = int(input(
    'Bem vindo(a) ao Banco da Hidekolandia, informe a quantia de reais que deseja sacar: vmin:10 vmax:600 '))
if solicitacao > 600:
    print("Valor acima do limite permitido")
elif solicitacao < 10:
    print("Valor abaixo do limite permitido")
else:
    valor = solicitacao
    cem = int(solicitacao/100)
    for i in range(cem):
        valor = valor-100

    cinquenta = int(valor/50)
    for i in range(cinquenta):
        valor = valor-50

    dez = int(valor/10)
    for i in range(dez):
        valor = valor-10

    cinco = int(valor/5)
    for i in range(cinco):
        valor = valor-5

    um = int(valor/1)
    for i in range(um):
        valor = valor-1

    notas = [cem, cinquenta, dez, cinco, um]
    numeros = [100, 50, 10, 5, 1]
    i = 0
    print("O valor solicitado Ã© {} reais e sera distribuito em: ".format(solicitacao))
    for nota in notas:
        if nota != 0:
            print("{} notas de {} reais".format(nota, numeros[i]))
        i = i+1

# Ex: 22

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(numero, "é um número par.")
else:
    print(numero, "é um número ímpar.")

# Ex:23

numero = input("Digite um número: ")

if "." in numero:
    print(numero, "é um número decimal.")
else:
    print(numero, "é um número inteiro.")

# Ex: 24

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

operacao = input("Qual operação você deseja realizar (+, -, *, /): ")

resultado = None

if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    resultado = numero1 / numero2

if resultado is not None:
    print("O resultado da operação é:", resultado)

    if resultado % 2 == 0:
        print(resultado, "é um número par.")
    else:
        print(resultado, "é um número ímpar.")

    if resultado >= 0:
        print(resultado, "é um número positivo.")
    else:
        print(resultado, "é um número negativo.")

    if resultado == round(resultado):
        print(resultado, "é um número inteiro.")
    else:
        print(resultado, "é um número decimal.")
else:
    print("Operação inválida. Por favor, escolha uma operação válida (+, -, *, /).")

# Ex: 25

print("Responda às perguntas com 'Sim' ou 'Não'.")
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

respostas_positivas = 0

for pergunta in perguntas:
    resposta = input(pergunta + " ")
    if resposta.lower() == "sim":
        respostas_positivas += 1

if respostas_positivas == 2:
    print("Suspeita")
elif 3 <= respostas_positivas <= 4:
    print("Cúmplice")
elif respostas_positivas == 5:
    print("Assassino")
else:
    print("Inocente")

# Ex: 26

print("Digite o tipo de combustivel: (A para alcoll e G para gasolina)")
tp = input()

if tp == 'A':
    print("Você escolhe alcool")
    print("Digite a quantida de litros a serem comprados:")
    lt = float(input())
    if lt <= 20:
        print("Desconto de 3% por litro")
        vlt = (lt*2.50)
        vltd = (vlt*0.03)
        vlta = vlt-vltd
        print("O valor a ser pago com o desconto de 3% no litro é de R${}".format(vlta))
    if lt > 20:
        print("Desconto de 5% por litro")
        vlt = (lt*2.50)
        vltd = (vlt*0.05)
        vlta = vlt-vltd
        print("O valor a ser pago com o desconto de 5% no litro é de R${}".format(vlta))

if tp == 'G':
    print("Você escolhe gasolina")
    print("Digite a quantida de litros a serem comprados:")
    lt = float(input())
    if lt <= 20:
        print("Desconto de 4% por litro")
        vlt = (lt*1.90)
        vltd = (vlt*0.04)
        vlta = vlt-vltd
        print("O valor a ser pago com o desconto de 3% no litro é de R${}".format(vlta))
    if lt > 20:
        print("Desconto de 5% por litro")
        vlt = (lt*1.90)
        vltd = (vlt*0.06)
        vlta = vlt-vltd
        print("O valor a ser pago com o desconto de 5% no litro é de R${}".format(vlta))

# Ex: 27

peso_morangos = float(input("Quantidade de morangos (em Kg): "))
peso_macas = float(input("Quantidade de maçãs (em Kg): "))

preco_morangos = 0.0
preco_macas = 0.0

if peso_morangos <= 5:
    preco_morangos = 2.50 * peso_morangos
else:
    preco_morangos = 2.20 * peso_morangos

if peso_macas <= 5:
    preco_macas = 1.80 * peso_macas
else:
    preco_macas = 1.50 * peso_macas

peso_total = peso_morangos + peso_macas
preco_total = preco_morangos + preco_macas

if peso_total > 8 or preco_total > 25.00:
    preco_total -= preco_total * 0.10

print("Valor a ser pago: R$", preco_total)

# Ex: 28

print("Tipos de carne disponíveis na promoção:")
print("1 - File Duplo")
print("2 - Alcatra")
print("3 - Picanha")

tipo_carne = int(input("Digite o número correspondente ao tipo de carne: "))
quantidade = float(input("Digite a quantidade de carne (em Kg): "))
forma_pagamento = input(
    "Digite a forma de pagamento (cartão Tabajara - S ou N): ")

preco_total = 0.0

if tipo_carne == 1:
    if quantidade <= 5:
        preco_total = 4.90 * quantidade
    else:
        preco_total = 5.80 * quantidade
    tipo_carne = "File Duplo"
elif tipo_carne == 2:
    if quantidade <= 5:
        preco_total = 5.90 * quantidade
    else:
        preco_total = 6.80 * quantidade
    tipo_carne = "Alcatra"
elif tipo_carne == 3:
    if quantidade <= 5:
        preco_total = 6.90 * quantidade
    else:
        preco_total = 7.80 * quantidade
    tipo_carne = "Picanha"

if forma_pagamento.lower() == "s":
    desconto = preco_total * 0.05
    preco_total -= desconto
    forma_pagamento = "Cartão Tabajara"
else:
    desconto = 0.0
    forma_pagamento = "Outro"

print("CUPOM FISCAL")
print("Tipo de carne:", tipo_carne)
print("Quantidade:", quantidade, "Kg")
print("Preço total: R$", preco_total)
print("Forma de pagamento:", forma_pagamento)
print("Valor do desconto: R$", desconto)
print("Valor a pagar: R$", preco_total)
