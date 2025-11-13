NOMBRE_ARCHIVO = "productos.txt"

def leer_productos_desde_archivo():
    # Lee productos del archivo y devuelve una lista de diccionarios
    productos = []

    with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as archivo: # Abrir el archivo en modo lectura
        for linea in archivo:
            linea = linea.strip() # Eliminar espacios en blanco y saltos de línea
            if not linea: 
                continue 

            partes = linea.split(",") # Dividir la línea en partes
            if len(partes) != 3: # Verificar que haya exactamente 3 partes
                continue

            nombre, precio_txt, cantidad_txt = partes

            # Conversión 
            precio = float(precio_txt)
            cantidad = int(cantidad_txt)

            producto = {
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad
            }

            productos.append(producto)

    return productos


def mostrar_productos(productos):
    # Muestra todos los productos en la lista
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")


def agregar_producto_desde_teclado(productos):
    # Permite ingresar un nuevo producto desde teclado
    print("\n=== Agregar nuevo producto ===")
    nombre = input("Nombre: ").strip() # Eliminar espacios en blanco
    precio = float(input("Precio: ").strip())
    cantidad = int(input("Cantidad: ").strip())
    # Crear diccionario del nuevo producto
    nuevo = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    productos.append(nuevo) # Agregar a la lista

    # Agregar al archivo sin borrar lo anterior
    with open(NOMBRE_ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")


def buscar_producto_por_nombre(productos):
    # Busca un producto por nombre dentro de la lista
    print("\n=== Buscar producto ===")
    nombre_buscar = input("Ingrese el nombre del producto: ").strip()

    for p in productos:
        if p["nombre"].lower() == nombre_buscar.lower(): # Comparación sin distinguir mayúsculas/minúsculas
            print("\nProducto encontrado:")
            print(f"Nombre: {p['nombre']}")
            print(f"Precio: ${p['precio']}")
            print(f"Cantidad: {p['cantidad']}")
            return

    print("ERROR: Producto no encontrado.")


def guardar_productos_en_archivo(productos):
    # Sobrescribe el archivo con todos los productos actualizados
    with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as archivo:
        for p in productos:
            archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")


def main():
    # Leer productos del archivo
    productos = leer_productos_desde_archivo()

    print("\n=== Productos actuales ===")
    mostrar_productos(productos)

    # Agregar productos desde teclado
    while True:
        opcion = input("\n¿Desea agregar un nuevo producto? (s/n): ").strip().lower()
        if opcion == "s":
            agregar_producto_desde_teclado(productos)
        elif opcion == "n":
            break
        else:
            print("Opción inválida. Ingrese 's' o 'n'.")

    # Buscar producto
    opcion_buscar = input("\n¿Desea buscar un producto? (s/n): ").strip().lower()
    if opcion_buscar == "s":
        buscar_producto_por_nombre(productos)

    # Guardar los productos actualizados
    guardar_productos_en_archivo(productos)

    print("\nProductos actualizados guardados. Fin del programa.")


if __name__ == "__main__":
    main()
