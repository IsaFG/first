
# Definimos una funcion que calcula la potencia de 2.
def calc_exponente (potencia):
    i = 1
    resultado = 2
    while i < (potencia + 1):
        resultado = resultado*2
        i = i + 1
    return resultado

calcular = calc_exponente(3)

print calcular
