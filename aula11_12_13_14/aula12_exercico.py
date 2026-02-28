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

# 3. CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.
def elevar_numero(base, expoente):
    resultado = base ** expoente
    print(f"{base} elevado a {expoente} é {resultado}.")

# 4. CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO DIGITAR, 18 ANOS.
def mensagem_idade(idade):
    if idade == 18:
        print("bem vindo a vida adulta, ja voce vai pro exercito")
    else:
        print(f"Você tem {idade} anos.")

# 5. DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.
def descobrir_idade(ano_nascimento, ano_atual):
    idade = ano_atual - ano_nascimento
    print(f"Sua idade é: {idade} anos.")

# 6. DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999.
def brasil_ganhou_copa_1999():
    brasil_copas = [1958, 1962, 1970, 1994, 2002]
    if 1999 in brasil_copas:
        print("O Brasil ganhou a Copa em 1999.")
    else:
        print("O Brasil NÃO ganhou a Copa em 1999.")

# 7. DESENVOLVA UM SISTEMA DE RESTAURANTE,
def cumprimentar_cliente(nome):
    print(f"Boa tarde, {nome} de boa ?")

def restaurante():
    opcoes = ["Salada", "Macarronada", "Sanduíche", "Sorvete"]
    print("\nOpções disponíveis:")
    for i, prato in enumerate(opcoes, 1):
        print(f"{i} - {prato}")

    escolha = int(input("Escolha o número do prato : "))
    if 1 <= escolha <= len(opcoes):
        print(f"Você escolheu: {opcoes[escolha - 1]}")
    else:
        print("nao tem, tente novamente.")


print("\nExercicio 1: Comparar 2 números (par ou ímpar)")
num1 = int(input("coloca algum numero: "))
num2 = int(input("coloca outro número: "))
comparar_par_impar(num1, num2)

print("\nExercicio 2: Multiplicar 3 números")
a = int(input("coloca o primeiro numero: "))
b = int(input("coloca o segundo número: "))
c = int(input("coloca o terceiro número: "))
multiplicar_tres_numeros(a, b, c)

print("\nExercicio 3: Elevar um número (potência)")
base = int(input("coloca  o numero: "))
expoente = int(input("outro numero: "))
elevar_numero(base, expoente)

print("\nExercicio 4: Mensagem para quem tem 18 anos")
idade = int(input("fala a sua idade: "))
mensagem_idade(idade)

print("\nExercicio 5: Descobrir idade de uma pessoa")
ano_nasc = int(input("coloca o seu ano de nascimento: "))
ano_atual = int(input("coloca o ano atual: "))
descobrir_idade(ano_nasc, ano_atual)

print("\nExercicio 6: Brasil ganhou a Copa em 1999?")
brasil_ganhou_copa_1999()

print("\nExercicio 7: Restaurante")
nome_cliente = input("fala o seu nome: ")
cumprimentar_cliente(nome_cliente)
restaurante()