import math

def calcular_media(valores):
    return sum(valores) / len(valores)

def calcular_desvio_padrao(valores):
    media = calcular_media(valores)
    soma_diferencas_quadrado = sum((x - media) ** 2 for x in valores)
    variancia = soma_diferencas_quadrado / len(valores)
    desvio_padrao = math.sqrt(variancia)
    return desvio_padrao

dados = [2, 4, 6, 8, 10]
media = calcular_media(dados)
desvio_padrao = calcular_desvio_padrao(dados)

print("Média:", media)  # Output: 6.0
print("Desvio padrão:", desvio_padrao)  # Output: 2.8284271247461903
