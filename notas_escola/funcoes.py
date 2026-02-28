import statistics

def moda(valores):
    try:
        return statistics.mode(valores)
    except statistics.StatisticsError:
        return statistics.multimode(valores)

def media(valores):
    return statistics.mean(valores)

def mediana(valores):
    return statistics.median(valores)

def menor_nota(valores):
    return min(valores)

def maior_nota(valores):
    return max(valores)

def desvio(valores):
    return statistics.stdev(valores)