from funcoes import *

def verificar():
    print('ESCOLA: EE Prof. José Roberto Friebolin\n')
    notas_input = input("Digite as notas separadas por espaço ou vírgula:\n").strip()
    if not notas_input:
        print("Nenhuma nota inserida. Encerrando o programa.")
        return
    
    notas = [float(n.replace(',', '.')) for n in notas_input.replace(',', ' ').split()]
    print('\nNotas:', notas)
    print('Média:', media(notas))
    print('Mediana:', mediana(notas))
    print('Moda:', moda(notas))
    print('Desvio padrão:', desvio(notas))
    print('Menor nota:', menor_nota(notas))
    print('Maior nota:', maior_nota(notas))

verificar()