# EJERCICIO 18
import re

def abrir_fichero(fichero, ficheroCabecera, ficheroSecuencia):
    f = open(fichero)
    f2 = open(ficheroCabecera, "a")
    f3 = open(ficheroSecuencia, "a")
    lines = f.readlines()
    print "Lines es: " + str(lines)
    for i in range(0,59):
        #print "Cabecera : " + lines[i]
        f2.write(str(lines[i]))
    for i in range(59,100):
        #print "Secuencia : " + lines[i]
        f3.write(str(lines[i]))
    f.close()
    f2.close()

def buscar_codon(fichero):
    i = 0
    for line in fichero:
        j = 0
        objeto_er = re.compile('tca') # crear un objeto expresion regular con lo que queremos buscar
        mo = objeto_er.search(line) # crear un objeto con el resultado matchobject de la espresion regular
        while mo:
            print mo.start()
            j = mo.end()
            mo = objeto_er.search(line, j)
        print "Linea procesada : " + str(i)
        i =+ 1

abrir_fichero("/home/bioinfo/PycharmProjects/PythonIntro/Tema 2/genbank.gb", "/home/bioinfo/PycharmProjects/PythonIntro/Tema 2/infoCabecera.txt", "/home/bioinfo/PycharmProjects/PythonIntro/Tema 2/ficheroSecuencia.txt")
buscar_codon( "/home/bioinfo/PycharmProjects/PythonIntro/Tema 2/ficheroSecuencia.txt")