import re

resultado = re.search("hola", "que tal, hola")
print 1
print resultado
print ""
print 2
resultado = re.fullmatch('hola', "que tal, hola")
print resultado


