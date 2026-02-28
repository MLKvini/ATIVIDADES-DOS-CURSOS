from funcoes import *

def verificar():
    empresa1 = [1000, 6000, 1200, 8000, 1400]
    empresa2 = [5000, 4000, 3000, 2000, 7000]
    empresa3 = [1200, 1300, 8000, 3000, 15000]
    empresa4 = [1400, 1750, 2000, 4500, 5900]

    print('Análise de salário:')

    # Média
    print('MÉDIA 1:', media(empresa1))
    print('MÉDIA 2:', media(empresa2))
    print('MÉDIA 3:', media(empresa3))
    print('MÉDIA 4:', media(empresa4))
    print('***' * 10)

    # Moda
    print('MODA 1:', moda(empresa1))
    print('MODA 2:', moda(empresa2))
    print('MODA 3:', moda(empresa3))
    print('MODA 4:', moda(empresa4))
    print('***' * 10)

    # Mediana
    print('MEDIANA 1:', mediana(empresa1))
    print('MEDIANA 2:', mediana(empresa2))
    print('MEDIANA 3:', mediana(empresa3))
    print('MEDIANA 4:', mediana(empresa4))
    print('***' * 10)

    # Desvio padrão
    print('DESVIO 1:', desvio(empresa1))
    print('DESVIO 2:', desvio(empresa2))
    print('DESVIO 3:', desvio(empresa3))
    print('DESVIO 4:', desvio(empresa4))

verificar()
print('***' * 10)
print('Escolhi a Empresa 2 porque os salários são mais equilibrados. A diferença entre o menor e o maior valor não é tão grande quanto nas outras empresas, o que mostra mais estabilidade e menos desigualdade entre os funcionários. Isso passa a ideia de um ambiente mais justo e organizado.')