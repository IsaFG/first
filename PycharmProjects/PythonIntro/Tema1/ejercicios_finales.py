# Ejercicio 8 :
# PARTE 1 :
# Abrir el fichero dna1.txt.
# Este fichero contiene 5 lineas de cabecero y el resto con DNA.
# Contar cuantas veces aparece cada una de las bases en la cadena de DNA.

def extraer_DNA(fichero): # funcion para extraer la cadena de DNA del fichero
    # Este fichero contiene 5 lineas de cabecero y el resto con DNA.
    f = open(fichero) # Abrir el fichero dna1.txt.
    nucChain = '' # declaramos una string vacia que sera nuestra cadena de nt
    iterador = 0
    # primera parte : procesar todas las lineas para conservar la cadena completa de ADN limpia del resto
    for line in f : # para cada linea dentro del fichero
        iterador += 1
        # print "Iteracion" + str(iterador) # CONTROL
        if iterador > 5: # si el indice de la linea del fichero es mayor que cinco
            lineList = [] # declarar una lista vacia
            lineList = line.split(' ')  # trocear la linea del fichero y volcarlo todo a una lista
            # print "Lista en bruto : " + str(lineList) # CONTROL
            # SUPRIMIR LOS PRIMEROS ELEMENTOS DE LA LISTA QUE NO SON AA
            # Metodo 1 no eficiente ya que conserva los ultimos elementos
            # lineList = lineList[-6:] # conservar los seis ultimos elementos de la lista, que son los aa
            # Metodo 2 no eficiente : suprimer los 9 primeros elementos de la lista
            # del lineList[0:8]
            # METODO 3 EFICIENTE :
            # Metodo 3.a suprimir las ocurencias de "" en la lista
            while "" in lineList:
                lineList.remove("")
            # Metodo 3.b Ahora suprimir el numero de la lista, es decir, conservar todo menos el primer elemento
            lineList = lineList[1:]
            # print "Lista limpiada : " + str(lineList) # CONTROL
            delim = ''
            chain = delim.join(lineList) # juntar los elementos de la lista en una cadena limpia de nt
            # chain.replace('\n', '') # quitar los saltos de linea # CREO QUE NO FUNCIONA
            chain.rstrip()
            # print "Cadena " + str(iterador) # CONTROL imprimir el indice de la linea que se esta procesando
            # print chain # CONTROL imprimir la linea que se esta procesando
            nucChain = nucChain + chain # juntar la linea procesada a la cadena en total
    nucChain.replace('\n', '')
    # print "Esta es toda la cadena :" # CONTROL
    # print nucChain # CONTROL
    f.close()  # cerrar el fichero de texto
    return nucChain

# PARTE 2:
# Usando un diccionario que tiene como clave los codones y como valor el aminoacido correspondiente,
# convertir todo el DNA en amino acidos
# y guardarlo en un fichero llamado amino.txt.
# Contar cuantos aminoacidos de cada tipo hay.
# Por  pantalla  solicitar  al  usuario  un  porcentaje  y
# mostrar  cuales  son  los aminoacidos por encima de ese porcentaje.
def translate_dna(sequence):
    codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    protein = ""
    x = 0
    while x < len(secuencia) :
        codon = secuencia[x:(x+3)]
        codon = codon.upper()
        aa = codontable[codon]
        print aa
        print "Esto es el codon "  + str(x) + " : " + str(codon) + " y este es el aminoacido : " + str(aa) # CONTROL
        protein = protein + aa
        x += 3
        print "Ahora x es : " + str(x) + ", y esta es la proteina actual " + protein # CONTROL
        # protein = protein + codon
        # print "Test de la iteracion. Imprimiendo proteina : "
        print ""


    # dic = {}  # definimos un diccionario vacio que vamos a llenar con las palabras que existen en el fichero
    # iterador = 1
    # for line in f:  # para cada linea del fichero
    #     print ""
    #     word_list = line.split(' ')  # en una lista, introducimos el resultado de dividir la linea en sus palabras
    #     print word_list  # imprimir la lista de lineas
    #     for word in word_list:  # para cada palabra de la lista, buscar si esta en el diccionario, y si no, aniadirla
    #         if word in dic:  # si la palabra ya esta en el diccionario
    #             dic[word] += 1  # sumar +1 al valor asociado
    #         else:  # si la palabra no esta
    #             nueva_entrada = {word: 1}  # crear la nueva entrada de diccionario con una aparicion
    #             dic.update(nueva_entrada)  # actualizar el diccionario con la nueva entrada
    #     iterador += 1
    #     print dic
    # print ""

secuencia = extraer_DNA("/home/bioinfo/PycharmProjects/PythonIntro/Tema1/dna1.txt")
print secuencia
print (len(secuencia)/3)
# print "Esta es la secuencia limpia : " + str(secuencia) # CONTROL de la secuencia obtenida
translate_dna(secuencia)