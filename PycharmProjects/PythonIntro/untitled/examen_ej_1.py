# EJERCICIO 1 - PROGRAMA QUE RECORRE UNA LISTA DE NUMEROS

lista_num =  [0,1,1,1,3,4,3,2,1,3,21,1,1,1,1,23,4,4,6,7]

# Pedir al usuario un numero por pantalla y convertirlo a string
numero = raw_input("Introduzca un numero : ")
print "Usted ha introducido : " + str(numero)
numero = int(numero)

# El siguiente bloque recorre la lista
# y por cada posicion toma el numero para compararlo con el del usuario
# Si es igual, incremente en uno el contador que nos determina cuantas veces ha salido ese numero
j = 0
for i in range(0,(len(lista_num))):
    print "Iterando posicion : " + str(i)
    print "   y obteniendo numero : " + str(lista_num[i])
    if lista_num[i] == numero:
        j = j + 1

print ""
print "FIN"
print "Su numero aparece este numero de veces : " + str(j)
