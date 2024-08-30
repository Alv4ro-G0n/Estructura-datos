inventario = {}

def mostrar_menu():
    print("==========================")
    print("¿Qué quiere hacer?")
    print("1) Agregar Producto")
    print("2) Actualizar stock")
    print("3) Eliminar producto")
    print("4) Buscar producto")
    print("5) **SALIR**")

def agregar_producto(nombre, cantidad, precio):
    if nombre in inventario:
        return "El producto ya se encuentra registrado en el inventario"
    datos = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio,
    }
    inventario[nombre] = datos
    return f"Producto '{nombre}' agregado con éxito."

def actualizar_stock(nombre, cantidad_nueva):
    if nombre in inventario:
        inventario[nombre]['cantidad'] = cantidad_nueva
        return f"Stock del producto '{nombre}' actualizado con éxito."
    else:
        return "El producto no se encuentra en el inventario."

def eliminar_producto(nombre):
    if nombre in inventario:
        del inventario[nombre]
        return f"Producto '{nombre}' eliminado con éxito."
    else:
        return "El producto no se encuentra en el inventario."

def buscar_producto(nombre):
    if nombre in inventario:
        producto = inventario[nombre]
        return {
            "nombre": nombre,
            "cantidad": producto['cantidad'],
            "precio": producto['precio']
        }
    else:
        return "El producto no se encuentra en el inventario."

def salir():
    
    inventario.clear()
    return "Inventario limpio, fin del programa."
    

def pedir_opcion():
    while True:
        try:
            opcion = int(input("Ingrese la opción que desea: "))
            if 1 <= opcion <= 5:
                return opcion
            else:
                print("Número no válido, ingrese nuevamente.")
        except ValueError:
            print("Entrada no válida, por favor ingrese un número.")

def hacer_accion(opcion):
    if opcion == 1:
        nombre = input("Nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad de productos (stock): "))
        precio = float(input("Ingrese el precio: "))
        print(agregar_producto(nombre, cantidad, precio))
    elif opcion == 2:
        nombre = input("Ingrese el nombre del producto: ")
        cantidad_nueva = int(input("Ingrese la nueva cantidad: "))
        print(actualizar_stock(nombre, cantidad_nueva))
    elif opcion == 3:
        nombre = input("Ingrese el nombre del producto que desea eliminar: ")
        print(eliminar_producto(nombre))
    elif opcion == 4:
        nombre = input("¿Qué producto busca? Ingrese el nombre: ")
        producto = buscar_producto(nombre)
        if isinstance(producto, dict):
            print(f"Nombre: {producto['nombre']}")
            print(f"Stock: {producto['cantidad']}")
            print(f"Precio: {producto['precio']}")
        else:
            print(producto)
    elif opcion == 5:
        print(salir())
        exit()

# Programa principal
if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = pedir_opcion()
        hacer_accion(opcion)



"Ultimo cambio"
