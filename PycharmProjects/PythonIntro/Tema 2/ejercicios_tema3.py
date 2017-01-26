# EJERCICIO 20
# Cree una clase llamada Cuenta

class Cuenta(object):
    # Como atributo tendra un numero float llamado saldo , con una cantidad inicial de 0 euros
    def __init__(self, cantidad):
        self.saldo = float(cantidad) # La cantidad de 0 euros sera el parametro que pasaremos a la clase cuando creemos el objeto
        # self.sald = 0 # Esta inicializacion tambien es valida si siempre queremos crear el objeto con una cantidad inicial de 0

    # Tendra dos metodos:
    # ingresar, con un parametro que indica la cantidad a sumar al saldo
    def ingresar (self, ingreso):
        self.saldo = self.saldo + float(ingreso)
        return self.saldo

    # retirar, con un parametro que sera un numero float de euros a restar del saldo
    def retirar(self, retirada):
        self.saldo = self.saldo - float(retirada)
        return self.saldo

# Cree un programa para ingresar 125.23, 503.4 y 50 euros y luego retire, 333.34 euros.
# Muestre tras cada operacion, el saldo de la cuenta.

# PROGRAMA CREADO A PARTIR DE TRES FUNCIONES
def crear_Cuenta() :
    cantidad = raw_input("Introduzca el saldo inicial de su cuenta :")
    cantidad = float(cantidad)
    miSaldo = Cuenta(cantidad)
    print "Su saldo inicial es de :"
    print miSaldo.saldo
    return miSaldo

def ingresar():
    cantidad = raw_input("Introduzca la cantidad del ingreso :")
    miSaldo.ingresar(cantidad)
    return miSaldo.saldo

def retirar():
    cantidad = raw_input("Introduzca la cantidad a retirar :")
    miSaldo.retirar(cantidad)
    return miSaldo.saldo

# TEST > LLAMAMOS AHORA A LAS DIFERENTES FUNCIONES
# DESCOMENTAR LO QUE SIGUE PARA QUE RULE EL PROGRAMA
# miSaldo = crear_Cuenta()
# print ""
# ingresar()
# print "Ingreso 1 : "
# print miSaldo.saldo
# print ""
#
# retirar()
# print "Retirada 1 : "
# print miSaldo.saldo
# print ""
#
# miSaldo.ingresar(503.4)
# print "Ingreso 2 : "
# print miSaldo.saldo
# print ""

# EJERCICIO 23 - HERENCIA
##################################
# Cree una nueva clase que herede de Cuenta del ejercicio 20. Se llamara Cuenta_ahorro
class Cuenta_ahorro(Cuenta):
    # Contendra un nuevo metodo avisar que informara en el momento en el que se realice una
    # operacion(retirar) que de lugar a un saldo negativo. El mensaje a mostrar sera 'NUMEROS ROJOS'

    # Modifique el metodo retirar para que no deje sacar dinero si el saldo es negativo.
    # En ese caso mostrara el mensaje por pantalla 'NO  TIENE CREDITO'

    def retirar(self, retirada):
        if self.saldo < 0:
            print "Usted no tiene credito"
        else:
            self.saldo = self.saldo - float(retirada)
            if self.saldo < 0:
                print "Usted esta en NUMEROS ROJOS"
        return self.saldo

miCuenta = Cuenta_ahorro(300)
print "Saldo Actual : "
print miCuenta.saldo
print ""

print "Retirada 1"
miCuenta.retirar(290)
print "Saldo Actual : "
print miCuenta.saldo
print ""

print "Retirada 2"
miCuenta.retirar(30)
print "Saldo Actual : "
print miCuenta.saldo
print ""

print "Retirada 3"
miCuenta.retirar(20)
print "Saldo Actual : "
print miCuenta.saldo
print ""