import re

#A) Escribir un programa ciclico que abra un fichero GenBank
# cuyo nombre es introducido por el usuario #Y realice las acciones indicadas.

class analizarFichero(object):
    def __init__(self, file):
        self.fichero = file

    def mostrar_organismo(self):
        organismo = "Prueba 1"
        return organismo

    def mostrar_bases(self):
        numeroBases = "Prueba 2"
        return numeroBases

    def guardar_ADN(self):
        cadena = "Prueba 3"
        return cadena

    def salir(self):
        print "Salio del programa !"

#A) Escribir un programa ciclico que abra un fichero GenBank
# cuyo nombre es introducido por el usuario
fichero = raw_input("Introduzca el nombre del fichero : ")

## LINEA DE TEST ##
fichero = "/home/bioinfo/PycharmProjects/PythonIntro/untitled/genbank.gb"

# y muestre un menu como el siguiente:
# Pulse 1 si quiere mostrar a que organismo pertenecen los datos
# Pulse 2 si quiere mostrar cuantas bases de cada tipo existen
# Pulse 3 si quiere guardar en un fichero, con nombre elegido por el usuario, una unica cadena con todo el ADN
# Pulse 4 si desea salir del programa

variableSalir = 0

while variableSalir == 0:
    print "MENU"
    print "Pulse 1 si quiere mostrar a que organismo pertenecen los datos"
    print "Pulse 2 si quiere mostrar cuantas bases de cada tipo existen"
    print "Pulse 3 si quiere guardar en un fichero, con nombre elegido por el usuario, una unica cadena con todo el ADN"
    print "Pulse 4 si desea salir del programa"
    opcion = raw_input("Pulse : ")
    print "Usted ha introducido " + str(opcion)
    opcion = int(opcion)
    if opcion == 1:
        analizarFichero.mostrar_organismo()
        print analizarFichero.mostrar_organismo()
    elif opcion == 2:
        analizarFichero.mostrar_bases()
        print analizarFichero.mostrar_bases()
    elif opcion == 3:
        analizarFichero.guardar_ADN()
        print analizarFichero.guardar_ADN()
    elif opcion == 4:
        Salir()
        variableSalir = variableSalir + 1
    else:
        print "Opcion incorrecta, vuelva a intentarlo"

#B) Aniadir alguna otra opcion al menu que permita
# analizar algun dato significativo del fichero.