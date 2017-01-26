# EJERCICIO 21

class Fichero (object):
    def __init__(self, ruta):
        self.path = ruta
        self.text = "Test"

    def leer_fichero(self, testLectura):
        print testLectura
        print ""
        f = open(self.path)
        self.text = f.read()
        f.close()

    def mostrar_fichero(self, testMuestra):
        print testMuestra
        print ""
        print self.text

## TEST DEL EJERCICIO 21 - DESCOMENTAR
# miFichero = Fichero("/home/bioinfo/PycharmProjects/PythonIntro/Tema1/fichero1")
# miFichero.leer_fichero("Leyendo")
# miFichero.mostrar_fichero("Mostrando")

# EJERCICIO 22
# Se tratara de que cada persona es un objeto.
# Con cada persona creamos un objeto usando la clase persona
# Los objetos se aniadiran a una lista o un diccionario que esta en el fichero persona.
# En el diccionario la key es la linea del fichero por ejemplo

# Los datos de las personas se guardan en el fichero persona.txt

class Persona(object):
    def __init__(self, nombre, DNI, telefono, email):
        self.name = nombre
        self.id = DNI
        self.phone = telefono
        self.mail = email

    def imprimir_datos(self):
        datosPersona = {"nombre":self.name,"DNI":self.id,"telefono":self.phone,"email":self.mail}
        nombre = datosPersona["nombre"]
        DNI = datosPersona["DNI"]
        str(datosPersona)
        print datosPersona
        return nombre, DNI

    def introducir_datos(self, fichero):
        f = open(fichero, 'a')
        f.write("\n" + self.name + "," + self.id)
        f.close()


# PROGRAMA PARA HACER QUE SE CREE LA PERSONA POR CONSOLA
# def crear_persona():
#     print "Ahora vamos a crear una entrada con la nueva persona : "
#     nombre = raw_input("Introduzca el nombre : ")
#     DNI = raw_input("Introduzca DNI : ")
#     telefono = raw_input("Introduzca telefono : ")
#     email = raw_input("Introduzca mail : ")
#     nuevaPersona = Persona(nombre,DNI,telefono,email)
#     print "Estos son los datos introducidos : " + str(nuevaPersona)
#     print ""
# crear_persona()

nuevaPersona = Persona("Emilio","7894561V","9123647895","emilio@emilio.com")
nuevaPersona.imprimir_datos()
print nuevaPersona.imprimir_datos()
nuevaPersona.introducir_datos("/home/bioinfo/PycharmProjects/PythonIntro/Tema 2/personas.txt")



