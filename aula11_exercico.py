#EXERCICIO 1 Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.
while True:
 try:
    num= int(input("COLOCA ALGUM NUMERO INTEIRO: "))
    print(f"O NUMERO É: {num}")
    break
 except ValueError:
    print("ERRO O NUMERO QUE VC COLOCOU NAO É INTEIRO")

#EXERCICIO 2 Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.

while True:
 try:
     n = int(input('COLOCA UM NUMERO PARA DIVIDIR:'))
     n1 = int(input('COLOCA OUTRO NUMERO PARA DIVIDIR:'))
     print(n/n1)
 except ZeroDivisionError as error:
    print('nao tem como dividir esse numero')
 else:
    print('deu tudo certo')
    break

#Exercício 3: Crie uma lista e um índice como entrada e retorne o índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).
lista = [1, 2, 3, 4, 5]
while True:
 try:
    ind = int(input("Digite o índice: "))
    print(lista[ind])
 except IndexError:
    print("O INDICE ESTA ERRADO")
    break