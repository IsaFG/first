import re

# EJERCICIO 14
def DNA_to_RNA(secuencia):
    secuencia = secuencia.upper()
    secuencia = re.sub("T", "U", secuencia)
    return secuencia

RNAchain = DNA_to_RNA("agatggcggcgctgaggggt")
print RNAchain
print ""

# EJERCICIO 15
print 'EJERCICIO 15'
# Para el siguiente codigo:

resultado1 = re.match('(.*)(cat)(.*)', 'the cat in the hat')
# Determinar que se identifica en cada uno de los grupos.
# Hacer lo mismo con:
resultado2 = re.match('(.*)(at)(.*)', 'the cat in the hat')
print str(resultado1) + " and " + str(resultado2)

# Ejercicio 16:
# En PERL los nombres de variable se forman igual que en Python pero van precedidos del simbolo $.
# Crear un programa que pida al usuario una palabra y diga si es una variable legal de PERL
# PERLvariable = raw_input("Please enter a valid variable for PERL")
# if re.match('(^\$)', PERLvariable) :
#     print "OK"
# else:
#     print "Not valid"

# EJERCICIO 17
floatNum = raw_input("Please enter a float : ")
if re.match('(.*)(\.)(.*)', floatNum) :
    print "OK"
elif re.match('(.*)("E")(.*)', floatNum) :
    print "OK, exposant"
else :
    print "Nooooo"