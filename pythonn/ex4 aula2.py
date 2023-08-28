# Declarando as variáveis
nome = 'João da Silva'
cidade = 'São Paulo'
cpf = '123.456.789-00'

# Transformando em maiúsculo
nome_maiusculo = nome.upper()
cidade_maiusculo = cidade.upper()
cpf_maiusculo = cpf.upper()
print('Nome em maiúsculo:', nome_maiusculo)
print('Cidade em maiúsculo:', cidade_maiusculo)
print('CPF em maiúsculo:', cpf_maiusculo)

# Transformando em minúsculo
nome_minusculo = nome.lower()
cidade_minusculo = cidade.lower()
cpf_minusculo = cpf.lower()
print('Nome em minúsculo:', nome_minusculo)
print('Cidade em minúsculo:', cidade_minusculo)
print('CPF em minúsculo:', cpf_minusculo)

# Encontrando a posição do caractere 'ã'
posicao_ã_nome = nome.find('ã')
posicao_ã_cidade = cidade.find('ã')
posicao_ã_cpf = cpf.find('ã')
print('Posição do caractere ã no nome:', posicao_ã_nome)
print('Posição do caractere ã na cidade:', posicao_ã_cidade)
print('Posição do caractere ã no CPF:', posicao_ã_cpf)

# Exibindo o número de caracteres
tamanho_nome = len(nome)
tamanho_cidade = len(cidade)
tamanho_cpf = len(cpf)
print('O número de caracteres do nome é:', tamanho_nome)
print('O número de caracteres da cidade é:', tamanho_cidade)
print('O número de caracteres do cpf é:', tamanho_cpf)

# Removendo pontos e hífen do CPF
cpf_sem_pontuacao = cpf.replace('.', '').replace('-', '')
print('O cpf sem pontos e hífen fica:', cpf_sem_pontuacao)
