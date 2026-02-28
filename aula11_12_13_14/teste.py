# 1. CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.
def comparar_par_impar(num1, num2):
    # variáveis locais
    if num1 % 2 == 0:
        resultado1 = "par"
    else:
        resultado1 = "ímpar"
    if num2 % 2 == 0:
        resultado2 = "par"
    else:
        resultado2 = "ímpar"
    print(f"O número {num1} é {resultado1} e o número {num2} é {resultado2}.")

# 2. CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.
def multiplicar_tres_numeros(a, b, c):
    resultado = a * b * c
    print(f"A multiplicação de {a}, {b} e {c} é {resultado}.")
    return resultado

# 3. CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.
def elevar_numero(base, expoente):
    resultado = base ** expoente
    print(f"{base} elevado a {expoente} é {resultado}.")
    return resultado

# 4. CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO DIGITAR, 18 ANOS.
def mensagem_idade(idade):
    if idade == 18:
        print("Parabéns pelos 18 anos!")
    else:
        print(f"Você tem {idade} anos.")

# 5. DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.
def descobrir_idade(ano_nascimento, ano_atual):
    idade = ano_atual - ano_nascimento
    print(f"Sua idade é: {idade} anos.")
    return idade

# 6. DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999.
def brasil_ganhou_copa_1999():
    brasil_copas = [1958, 1962, 1970, 1994, 2002]
    if 1999 in brasil_copas:
        print("O Brasil ganhou a Copa em 1999.")
    else:
        print("O Brasil NÃO ganhou a Copa em 1999.")

# 7. DESENVOLVA UM SISTEMA DE RESTAURANTE,
# ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.
# 1 - Função - cumprimentar o cliente
def cumprimentar_cliente(nome):
    print(f"Bem-vindo(a), {nome}! É um prazer tê-lo(a) conosco.")

# 2 - Função - restaurante
def restaurante():
    opcoes = ["Salada", "Macarronada", "Sanduíche", "Sorvete"]
    print("Opções disponíveis:")
    for i, prato in enumerate(opcoes, 1):
        print(f"{i} - {prato}")

    escolha = int(input("Escolha o número do prato desejado: "))
    if 1 <= escolha <= len(opcoes):
        print(f"Você escolheu: {opcoes[escolha - 1]}")
    else:
        print("Opção inválida.")
