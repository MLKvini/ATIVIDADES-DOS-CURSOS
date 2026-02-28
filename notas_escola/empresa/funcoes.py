from statistics import mean, median, mode, StatisticsError, stdev

def media(lista):
    return mean(lista)

def mediana(lista):
    return median(lista)

def moda(lista):
    try:
        return mode(lista)
    except StatisticsError:
        return "Sem moda"

def desvio(lista):
    # O exercício pede desvio padrão da população, então usaremos o sqrt da variância populacional
    m = mean(lista)
    variancia = sum((x - m) ** 2 for x in lista) / len(lista)
    return round(variancia ** 0.5, 2)