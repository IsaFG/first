# Funcion que sirve para procesar lineas de un fichero
# que contiene cadenas de nucleotidos que siguen un patron especifico. Ver archivo de texto test1.txt.

def procesar_lineas(fichero):
    # Abrir el fichero
    f = open(fichero)
    nucChain = '' # declaramos una string vacia que sera nuestra cadena de nt
    iterador = 1
    # primera parte : procesar todas las lineas para conservar la cadena completa de ADN limpia del resto
    for line in f : # para cada linea dentro del fichero
        print "Procesando linea " + str(iterador)
        lineList = [] # declarar una lista vacia
        lineList = line.split(' ')  # trocear la linea del fichero y volcarlo todo a una lista
        print lineList
        # lineList = lineList[-6:] # conservar los seis ultimos elementos de la lista, que son los aa
        lineList = lineList.pop(0 - 8)
        print lineList
        delim = ''
        chain = delim.join(lineList) # juntar los elementos de la lista en una cadena limpia de nt
        chain.replace('\n', '')
        print "Cadena " + str(iterador)
        print chain #imprimir la cadena
        nucChain = nucChain + chain
        iterador += 1
    nucChain.replace('\n', '')
    print "Esta es toda la cadena :"
    print nucChain
    f.close()  # cerrar el fichero de texto

procesar_lineas("/home/bioinfo/PycharmProjects/PythonIntro/Tema1/test1.txt")

def extraer_DNA(fichero): # funcion para extraer la cadena de DNA del fichero
    # Este fichero contiene 5 lineas de cabecero y el resto con DNA.
    f = open(fichero) # Abrir el fichero dna1.txt.
    nucChain = '' # declaramos una string vacia que sera nuestra cadena de nt
    iterador = 0
    # primera parte : procesar todas las lineas para conservar la cadena completa de ADN limpia del resto
    for line in f : # para cada linea dentro del fichero
        iterador += 1
        if iterador > 5: # si el indice de la linea del fichero es mayor que cinco
            lineList = [] # declarar una lista vacia
            lineList = line.split(' ')  # trocear la linea del fichero y volcarlo todo a una lista
            #print lineList #linea de test
            lineList = lineList[-6:] # conservar los seis ultimos elementos de la lista, que son los aa
            #print lineList #linea de test
            delim = ''
            chain = delim.join(lineList) # juntar los elementos de la lista en una cadena limpia de nt
            chain.replace('\n', '') # quitar los saltos de linea # CREO QUE NO FUNCIONA
            print "Cadena " + str(iterador) # CONTROL imprimir el indice de la linea que se esta procesando
            print chain #CONTROL imprimir la linea que se esta procesando
            nucChain = nucChain + chain # juntar la linea procesada a la cadena en total
    nucChain.replace('\n', '')
    print "Esta es toda la cadena :"
    print nucChain
    return nucChain

    f.close() #cerrar el fichero de texto

#extraer_DNA("/home/bioinfo/PycharmProjects/PythonIntro/Tema1/dna1.txt")