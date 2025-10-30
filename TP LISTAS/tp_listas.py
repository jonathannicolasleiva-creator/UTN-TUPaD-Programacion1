#Ejercicio 1: 
# Crear lista vacía
notas = []

print("Cargue notas de 0 a 10. Escriba 'fin' para terminar antes de las 10.")
i = 0

# Bucle de carga de notas
while i < 10:
    entrada = input("Nota #" + str(i + 1) + ": ")
    if entrada.lower() == "fin":
        print("Carga finalizada por el usuario.\n")
        break  # Sale del bucle antes de llegar a 10
    try:
        valor = float(entrada)
        if valor < 0 or valor > 10:
            print("Por favor, ingrese un número entre 0 y 10.")
            continue
        notas.append(valor)
        i += 1
    except ValueError:
        print("Entrada inválida. Ingrese un número o 'fin' para salir.")

# Mostrar la lista completa usando un bucle
print("\n--- Notas cargadas ---")
print("Cantidad de notas ingresadas:", len(notas))
indice = 0
while indice < len(notas):
    print("[" + str(indice) + "] -> " + str(notas[indice]))
    indice += 1
print("-" * 32)

# Calcular promedio solo si hay elementos cargados
if len(notas) > 0:
    suma = 0.0
    for n in notas:
        suma += n
    promedio = suma / len(notas)

    # Buscar nota más alta y más baja
    mayor = notas[0]
    menor = notas[0]
    for n in notas[1:]:
        if n > mayor:
            mayor = n
        if n < menor:
            menor = n

    # Mostrar resultados
    print("Promedio: {:.2f}".format(promedio))
    print("Nota más alta:", mayor)
    print("Nota más baja:", menor)
else:
    print("No se ingresaron notas.")


# Ejercicio 2:
# Crear la lista vacía
productos = []

print("Cargue 5 productos ")

i = 0
while i < 5:
    nombre = input("Producto #" + str(i + 1) + ": ").strip()
    if nombre == "":
        print("Debe ingresar un nombre válido.")
        continue
    productos.append(nombre)
    i += 1

# Mostrar lista original
print("\n--- Lista original de productos ---")
for p in productos:
    print("-", p)

# Mostrar lista ordenada alfabéticamente (sin modificar la original)
productos_ordenados = sorted(productos)
print("\n--- Lista ordenada alfabéticamente ---")
for p in productos_ordenados:
    print("-", p)

# Preguntar qué producto eliminar
eliminar = input("\nIngrese el nombre del producto que desea eliminar: ").strip()

# Buscar y eliminar el producto si existe
encontrado = False
for p in productos:
    if p.lower() == eliminar.lower():
        productos.remove(p)
        encontrado = True
        break  # deja de buscar una vez que lo encuentra

# Mostrar resultado
if encontrado:
    print("\nProducto eliminado correctamente.")
else:
    print("\nEl producto no estaba en la lista.")

print("\n--- Lista actualizada ---")
for p in productos:
    print("-", p)


# Ejercicio 3:
import random  # permite generar números aleatorios

# Generar lista principal con 15 números al azar entre 1 y 100
numeros = []

i = 0
while i < 15:
    numero = random.randint(1, 100)  # genera un número entero entre 1 y 100
    numeros.append(numero)
    i += 1

# Mostrar lista completa
print("\n--- Lista completa de números generados ---")
for n in numeros:
    print(n, end=" ")
print()  # salto de línea

# Crear listas para pares e impares
pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

# Mostrar listas y cantidades
print("\n--- Números pares ---")
for p in pares:
    print(p, end=" ")
print("\nCantidad de números pares:", len(pares))

print("\n--- Números impares ---")
for imp in impares:
    print(imp, end=" ")
print("\nCantidad de números impares:", len(impares))


# Ejercicio 4:

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

# Mostrar lista original
print("\n--- Lista original ---")
for e in datos:
    print(e, end=" ")
print("\n--------------------------------")

# Crear nueva lista sin elementos repetidos (manteniendo el orden original)
sin_repetidos = []

for e in datos:
    if e not in sin_repetidos:
        sin_repetidos.append(e)

# Mostrar resultado
print("\n--- Lista sin elementos repetidos ---")
for e in sin_repetidos:
    print(e, end=" ")
print("\n--------------------------------")


# Ejercicio 5:

# Lista de estudiantes
estudiantes = ["Ana", "Bruno", "Carla", "Diego", "Elena", "Facundo", "Gisela", "Hugo"]

# Mostrar la lista inicial
print("\n--- Lista de estudiantes presentes ---")
for e in estudiantes:
    print("-", e)

# Preguntar qué desea hacer
while True:
    accion = input("\n¿Desea 'agregar', 'eliminar' o 'ninguno'? ").strip().lower()

    if accion == "agregar":
        nuevo = input("Ingrese el nombre del nuevo estudiante: ").strip().title()
        # Comparamos todo en minúsculas para evitar duplicados
        if nuevo.lower() in [e.lower() for e in estudiantes]:
            print("Ese nombre ya está en la lista.")
        else:
            estudiantes.append(nuevo)
            print(nuevo, "ha sido agregado correctamente.")
        break

    elif accion == "eliminar":
        eliminar = input("Ingrese el nombre del estudiante que desea eliminar: ").strip()
        encontrado = False
        for e in estudiantes:
            if e.lower() == eliminar.lower(): # comparación sin distinguir mayúsculas/minúsculas
                estudiantes.remove(e)
                encontrado = True
                print(eliminar.title(), "ha sido eliminado correctamente.")
                break
        if not encontrado:
            print("No se encontró ese nombre en la lista.")
        break

    elif accion == "ninguno":
        print("No se realizaron cambios en la lista.")
        break

    else:
        print("Opción inválida. Intente nuevamente (agregar / eliminar / ninguno).")

# Mostrar lista final
print("\n--- Lista actualizada de estudiantes ---")
for e in estudiantes:
    print("-", e)


# Ejercicio 6:
# Crear lista vacía
numeros = []

print("Ingrese 7 números:")

i = 0
while i < 7:
    entrada = input("Número #" + str(i + 1) + ": ")
    try:
        valor = float(entrada)
        numeros.append(valor)
        i += 1
    except ValueError:
        print("Entrada inválida. Ingrese un número válido.")

# Mostrar lista original
print("\n--- Lista original ---")
for n in numeros:
    print(n, end=" ")
print("\n--------------------------------")

# Rotar los elementos una posición a la derecha
# El último elemento pasa a ser el primero
if len(numeros) > 0:
    ultimo = numeros[-1]  # se guarda el último elemento
    indice = len(numeros) - 1
    while indice > 0:
        numeros[indice] = numeros[indice - 1]  # cada elemento toma el valor del anterior
        indice -= 1
    numeros[0] = ultimo  # el primero se reemplaza por el último original

# Mostrar lista rotada
print("\n--- Lista rotada a la derecha ---")
for n in numeros:
    print(n, end=" ")
print("\n--------------------------------")


# Ejercicio 7:
# La matriz 'temps' tendrá 7 filas (días) y 2 columnas: [min, max]
temps = []

print("Cargue las temperaturas de cada día (mínima y máxima).")
dia = 0
while dia < 7:
    print("\nDía", dia + 1)
    # pedir mínima con validación numérica
    while True:
        tmin_str = input("  Mínima: ")
        try:
            tmin = float(tmin_str)
            break
        except ValueError:
            print("  Entrada inválida. Ingrese un número.")
    # pedir máxima con validación numérica y relación con mínima
    while True:
        tmax_str = input("  Máxima: ")
        try:
            tmax = float(tmax_str)
            if tmax < tmin:
                print("  La máxima no puede ser menor a la mínima. Intente de nuevo.")
                continue
            break
        except ValueError:
            print("  Entrada inválida. Ingrese un número.")

    temps.append([tmin, tmax])
    dia += 1

# Mostrar la matriz completa con bucles
print("\n--- Mínimas y máximas por día (7x2) ---")
i = 0
while i < len(temps):
    fila = temps[i]
    # fila[0] = mínima, fila[1] = máxima
    print("Día", i + 1, "-> Min:", fila[0], " Max:", fila[1])
    i += 1
print("----------------------------------------")

# Calcular promedios de mínimas y máximas con bucles
suma_min = 0.0
suma_max = 0.0
i = 0
while i < len(temps):
    suma_min += temps[i][0]
    suma_max += temps[i][1]
    i += 1

prom_min = suma_min / 7
prom_max = suma_max / 7

print("Promedio de mínimas: {:.2f}".format(prom_min))
print("Promedio de máximas: {:.2f}".format(prom_max))

# Calcular amplitud térmica por día y encontrar la mayor
# amplitud = máxima - mínima
mayor_amp = None
dia_mayor_amp = None

i = 0
while i < len(temps):
    tmin = temps[i][0]
    tmax = temps[i][1]
    amp = tmax - tmin
    if (mayor_amp is None) or (amp > mayor_amp):
        mayor_amp = amp
        dia_mayor_amp = i + 1  # numeración humana 1..7
    i += 1

print("Mayor amplitud térmica: {:.2f} (Día {})".format(mayor_amp, dia_mayor_amp))


# Ejercicio 8:
materias = ["Matemática", "Programación", "Física"]

notas = []

# Cargar las notas
i = 0
while i < 5:
    print("\nEstudiante", i + 1)
    fila = []  # lista con las 3 notas del estudiante
    j = 0
    while j < len(materias):
        entrada = input("  Nota en " + materias[j] + ": ")
        try:
            valor = float(entrada)
            if valor < 0 or valor > 10:
                print("  Ingrese una nota válida (0 a 10).")
                continue
            fila.append(valor)
            j += 1
        except ValueError:
            print("  Entrada inválida. Ingrese un número.")
    notas.append(fila)
    i += 1

# Mostrar la matriz completa
print("\n--- Matriz de notas (5x3) ---")
i = 0
while i < len(notas):
    print("Estudiante", i + 1, "->", end=" ")
    j = 0
    while j < len(materias):
        print(materias[j] + ":", notas[i][j], end="  ")
        j += 1
    print()
    i += 1
print("-------------------------------------------")

# Calcular promedio de cada estudiante
print("\n--- Promedio por estudiante ---")
i = 0
while i < len(notas):
    suma = 0
    j = 0
    while j < len(notas[i]):
        suma += notas[i][j]
        j += 1
    promedio = suma / len(notas[i])
    print("Estudiante", i + 1, "-> Promedio general: {:.2f}".format(promedio))
    i += 1

# Calcular promedio de cada materia
print("\n--- Promedio por materia ---")
j = 0
while j < len(materias):
    suma = 0
    i = 0
    while i < len(notas):
        suma += notas[i][j]
        i += 1
    promedio = suma / len(notas)
    print(materias[j] + " -> Promedio:", "{:.2f}".format(promedio))
    j += 1


# Ejercicio 9:

# Crear tablero 3x3 con guiones "-"
tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]]

# Mostrar tablero inicial
print("\nTablero inicial:")
i = 0
while i < 3:
    j = 0
    fila_str = ""
    while j < 3:
        fila_str += " " + tablero[i][j] + " "
        if j < 2:
            fila_str += "|"
        j += 1
    print(fila_str)
    if i < 2:
        print("-----------")
    i += 1

# Empieza el jugador X
jugador = "X"
jugadas_realizadas = 0

# Bucle principal (hasta 9 jugadas válidas)
while jugadas_realizadas < 9:
    print("\nTurno de", jugador)

    # Ingreso de fila (1 a 3)
    while True:
        fila_str = input("  Ingrese número de FILA (1, 2 o 3): ")
        try:
            fila = int(fila_str)
            if fila < 1 or fila > 3:
                print("La fila debe ser 1, 2 o 3.")
                continue
            fila -= 1  # ajustar a índice interno 0-2
            break
        except ValueError:
            print("Entrada inválida. Ingrese un número válido.")

    # Ingreso de columna (1 a 3)
    while True:
        col_str = input("  Ingrese número de COLUMNA (1, 2 o 3): ")
        try:
            col = int(col_str)
            if col < 1 or col > 3:
                print("La columna debe ser 1, 2 o 3.")
                continue
            col -= 1  # ajustar a índice interno 0-2
            break
        except ValueError:
            print("Entrada inválida. Ingrese un número válido.")

    # Verificar si la casilla está libre
    if tablero[fila][col] != "-":
        print("Casilla ocupada. Elija otra posición.")
        continue

    # Colocar la marca
    tablero[fila][col] = jugador
    jugadas_realizadas += 1

    # Mostrar tablero actualizado
    print("\nTablero actual:")
    i = 0
    while i < 3:
        j = 0
        fila_str = ""
        while j < 3:
            fila_str += " " + tablero[i][j] + " "
            if j < 2:
                fila_str += "|"
            j += 1
        print(fila_str)
        if i < 2:
            print("-----------")
        i += 1

    # Cambiar jugador
    jugador = "O" if jugador == "X" else "X"

print("\nFin del juego.")


# Ejercicio 10:
#se importa la librería random para generar números aleatorios
import random 

# Lista de productos
productos = ["Peras", "Naranjas", "Manzanas", "Bananas"]

# Crear matriz 4x7 con números aleatorios entre 0 y 20 (ventas por día)
ventas = []
i = 0
while i < len(productos):  # 4 productos
    fila = []
    j = 0
    while j < 7:  # 7 días
        fila.append(random.randint(0, 20))
        j += 1
    ventas.append(fila)
    i += 1

# Mostrar matriz completa (formato tabla)
print("\n--- Ventas diarias por producto ---")
print("             D1  D2  D3  D4  D5  D6  D7")
i = 0
while i < len(productos):
    fila_str = productos[i].ljust(10) + ": "
    j = 0
    while j < 7:
        num = str(ventas[i][j]).rjust(2)
        fila_str += " " + num + " "
        j += 1
    print(fila_str)
    i += 1
print("-------------------------------------")

# Calcular total por producto (suma por fila)
print("\n--- Total vendido por producto ---")
totales_prod = []
i = 0
while i < len(productos):
    suma = 0
    j = 0
    while j < 7:
        suma += ventas[i][j]
        j += 1
    totales_prod.append(suma)
    print(productos[i], "->", suma, "unidades vendidas en la semana")
    i += 1

# Calcular total por día (suma por columna)
print("\n--- Total vendido por día ---")
totales_dia = []
j = 0
while j < 7:
    suma = 0
    i = 0
    while i < len(productos):
        suma += ventas[i][j]
        i += 1
    totales_dia.append(suma)
    print("Día", j + 1, "->", suma, "unidades vendidas")
    j += 1

# Día con mayores ventas totales
mayor_total = totales_dia[0]
dia_max = 1
k = 1
while k < 7:
    if totales_dia[k] > mayor_total:
        mayor_total = totales_dia[k]
        dia_max = k + 1
    k += 1
print("\nDía con mayores ventas totales: Día", dia_max, "(Total:", mayor_total, "unidades)")

# Producto más vendido en la semana
max_prod_total = totales_prod[0]
prod_top = productos[0]
k = 1
while k < len(productos):
    if totales_prod[k] > max_prod_total:
        max_prod_total = totales_prod[k]
        prod_top = productos[k]
    k += 1
print("Producto más vendido en la semana:", prod_top, "(Total:", max_prod_total, "unidades)")

