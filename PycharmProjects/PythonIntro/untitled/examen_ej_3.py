import re

# Con una primera funcion, buscamos todas las ocurrencias de un numero en la string
def comprobar_dia(fecha_introducida):
    listaNumeros = re.findall(r'\d+', fecha_introducida)
    if int(listaNumeros[0]) in range(1,32):
        print "Formato dia OK"
    else :
        print "Dia incorrecto"
    if int(listaNumeros[1]) in range(2000,2099):
        print "Formato anio OK"
    else:
        print "Anio incorrecto"
    return listaNumeros

# Segunda funcion : buscar si un mes aparece en la string y guardarlo en una variable si es asi
def comprobar_mes(fecha_introducida):
    meses = re.compile('enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre')
    mo = meses.search(fecha_introducida)
    if mo:
        mes = mo.group(0)
        print "Mes correcto"
    else :
        print "No hay mes correcto"
    return mes




# fecha_introducida = raw_input("Introduzca la fecha deseada : ")
fecha_introducida = "12 de diciembre de 2015"
mes = comprobar_mes(fecha_introducida)
listaNumeros = comprobar_dia(fecha_introducida)

mes_string = str(mes)

print "Estamos en " + mes_string + " de " + str(listaNumeros[1]) + " y es el dia " + str(listaNumeros[0])