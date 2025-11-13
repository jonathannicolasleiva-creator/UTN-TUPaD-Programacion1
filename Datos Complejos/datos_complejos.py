precios_frutas = {
    "Banana": 1200,
    "Ananá": 2500,
    "Melón": 3000,
    "Uva": 1450
}

# Punto 1: Agregar frutas
precios_frutas["Naranja"] = 1200 
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

# Punto 2: Actualizar precios
precios_frutas["Banana"] = 1330 
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

# Punto 3: Lista con las frutas
lista_frutas = list(precios_frutas.keys())

print(precios_frutas) # Mostrar el diccionario con los precios actualizados
print(lista_frutas) # Mostrar la lista de frutas

# Punto 4:

contactos = {}

# Cargar 5 contactos
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    contactos[nombre] = numero

# Consultar contacto
consulta = input("Ingresá el nombre que querés consultar: ")

if consulta in contactos:
    print(f"El número de {consulta} es: {contactos[consulta]}")
else:
    print("Ese contacto no existe.")

# Punto 5:

frase = input("Ingresá una frase: ")

# Separar las palabras
palabras = frase.split()

# Palabras únicas usando set
palabras_unicas = set(palabras)

# Contador de palabras usando diccionario
recuento = {}

for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

# Mostrar resultados
print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)

# Punto 6:

alumnos = {} # crear diccionario vacío

# Cargar datos de 3 alumnos
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")

    print("Ingresá las 3 notas separadas por espacio (por ej: 10 8 9): ")
    n1, n2, n3 = map(int, input().split()) # leer y convertir a enteros 

    alumnos[nombre] = (n1, n2, n3)

# Mostrar promedios
print("\nPromedios:")
for nombre, notas in alumnos.items(): # recorrer diccionario
    promedio = sum(notas) / len(notas) # calcular promedio
    print(f"{nombre}: {promedio:.2f}")

# Punto 7:

# Sets de estudiantes que aprobaron cada parcial
parcial1 = {1, 2, 3, 5, 8}
parcial2 = {3, 4, 5, 6}

# Aprobados en ambos parciales (intersección)
aprobados_ambos = parcial1.intersection(parcial2)

# Aprobados solo en uno (diferencia + unión)
solo_parcial1 = parcial1.difference(parcial2)
solo_parcial2 = parcial2.difference(parcial1)
aprobados_solo_uno = solo_parcial1.union(solo_parcial2)

# Aprobados al menos un parcial (unión)
aprobados_al_menos_uno = parcial1.union(parcial2)

# Mostrar resultados
print("Aprobaron ambos parciales:", aprobados_ambos)
print("Aprobaron solo uno:", aprobados_solo_uno)
print("Aprobaron al menos un parcial:", aprobados_al_menos_uno)

# Punto 8:

stock = {
    "manzanas": 10,
    "bananas": 5,
    "naranjas": 3
}
# Pedimos al usuario el nombre del producto que quiere consultar
producto = input("Ingresá un producto: ")

if producto in stock: #verificamos si el producto existe en el diccionario
    print(f"Stock actual de {producto}: {stock[producto]}") #consultar stock
    
    agregar = input("¿Querés agregar unidades? (s/n): ")
    if agregar.lower() == "s": #pasar a minúsculas y verificar
        cantidad = int(input("¿Cuántas unidades querés agregar?: "))
        stock[producto] += cantidad #sumar cantidad al stock existente
        print(f"Nuevo stock de {producto}: {stock[producto]}")
else:
    print("Ese producto no existe.") #si el producto no existe, avisamos el usuario
    agregar_nuevo = input("¿Querés agregarlo al stock? (s/n): ")
    if agregar_nuevo.lower() == "s":
        cantidad = int(input("Ingresá la cantidad inicial: "))
        stock[producto] = cantidad
        print(f"Producto agregado: {producto} → {cantidad} unidades.") #confirmamos

print("\nStock final:", stock)

# Punto 9:

agenda = {}

# Cargar 3 eventos
for i in range(3):
    dia = input(f"Ingresá el día del evento {i+1}: ")
    hora = input("Ingresá la hora (ej: 10:00): ")
    evento = input("Ingresá el nombre del evento: ")

    agenda[(dia, hora)] = evento

# Mostrar eventos cargados
print("\nAgenda completa:")
for clave, evento in agenda.items():
    dia, hora = clave
    print(f"{dia} a las {hora}: {evento}")

# Punto 10:

#diccionario con paises y capitales
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Perú": "Lima"
}

invertido = {} # diccionario vacío para invertir

for pais, capital in original.items(): # recorrer diccionario
    invertido[capital] = pais

print("Diccionario invertido:")
print(invertido)
