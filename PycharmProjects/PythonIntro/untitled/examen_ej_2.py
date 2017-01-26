# EJERCICIO 2 - CREACION DE DICCIONARIOS


# Definimos un diccionario vacio
dic_productos = {}

# Definimos la funcion que crea un pequenio diccionario con el producto y su precio final
# y actualizamos el diccionario de productos con ese pequenio diccionario
def crearDiccionario(Producto, Cantidad, Precio):
    for i in range(0,(len(Producto))) :
        precio_final = int(Cantidad[i]) * int(Precio[i])
        unProducto = {Producto[i]:precio_final}
        dic_productos.update(unProducto)
    return dic_productos

# Con este bloque definimos las listas que vamos a usar como ejemplo
Producto = ["arroz", "harina", "leche", "garbanzos"]
Cantidad = [4,5,3,65]
Precio = [10,15,20,21]

# Llamamos a la funcion que crea el diccionario, pasandole las listas como argumento
Todos_Productos = crearDiccionario(Producto, Cantidad, Precio)
print Todos_Productos


