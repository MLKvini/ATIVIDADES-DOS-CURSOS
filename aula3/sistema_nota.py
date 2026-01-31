print('SISTEMA DE NOTAS')
print('-'*30)

nome_aluno = input('nome do estudante: ')

n1_port = float(input('Nota de Portugues: '))
n2_mat = float(input('Nota de Matematica: '))
n3_ing = float(input('Nota de Ingles:' ))

media = (n1_port + n2_mat + n3_ing)/3
print(media)
print('-'*30)

print('SITUAÇÃO DO ALUNO: ')
aprovado = media >= 7
reprovado = media < 5
recuperacao = media >=5 and media < 7
print(nome_aluno,'APROVADO ?', aprovado)
print(nome_aluno,'REPROVADO ?', reprovado)
print(nome_aluno,'RECUPERAÇÃO ?', recuperacao)
print('-'*30)
