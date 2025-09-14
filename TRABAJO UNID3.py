#PUNTO1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad.")

#PUNTO2
nota=int(input("Por favor ingrese su nota:"))
if nota >= 6:
    print("aprobado")
else:
    print("desaprobado")

#PUNNTO3
numero_par = float(input("Ingrese un numero par: "))
if numero_par % 2 == 0: #cuando el modulo es 0 es par, si no es impar
    print(f"El numero {numero_par} es par")
else:
    print(f"El numero {numero_par} no es par")

#PUNTO4
edad = int(input("Por favor ingrese su edad: "))
if edad >= 30:
    print("usted es adulto/a")
elif edad >= 18:
    print ("usted es adulto/a joven")
elif edad >= 12:
    print("usted es adolecente")
else:
    print("usted es un niño/a")

#PUNTO5
password = input("Por favor ingrese una contraseña: ")
if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#PUNTO6
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

from statistics import mode, median, mean

# Calculamos media, mediana y moda
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

#determinamos el sesgo
if media > mediana and mediana > moda:
    sesgo = "Sesgo positivo o a la derecha"
elif media < mediana and mediana < moda:
    sesgo = "Sesgo negativo o a la izquierda"
elif media == mediana and mediana == moda:
    sesgo = "Sin sesgo"
else:
    sesgo = "sin sesgo definido"

print("Números:", numeros_aleatorios)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)
print("Resultado:", sesgo)

#PUNTO7
# Pedimos la frase al usuario
frase = input("Ingresa una frase o palabra: ")

# Revisamos si termina con vocal
if frase[-1] in "aeiouAEIOU":
    print (f"{frase}!")
else:
    print (frase)

#PUNTO8
nombre = input("Ingrese su nombre: ")
print(f"Hola, {nombre}! Si quiere su nombre en mayusculas, ingrese '1', si lo quiere en minusculas, ingrese '2', si quiere solo la primera letra en mayuscula, ingrese '3': ")
opcion = input("Ingrese su opción: ")
if opcion == '1':
    print(nombre.upper())
elif opcion == '2':
    print(nombre.lower())
elif opcion == '3':
    print(nombre.title())
else:
    print("Opción no válida")

#PUNTO9
magnitud = float(input("Ingrese la magnitud del sismo (1-10): "))
if magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala)")
elif magnitud >= 6:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud >= 5:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 4:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 3:
    print("Leve (ligeramente perceptible)")
else:
    print("Muy leve (imperceptible)")

#PUNTO10
# Pedimos los datos al usuario
hemisferio = input("Ingrese su hemisferio (N/S): ").strip().upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

# Hemisferio Norte
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes == 1 or mes == 2) or (mes == 3 and dia < 21):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes == 4 or mes == 5) or (mes == 6 and dia < 21):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes == 7 or mes == 8) or (mes == 9 and dia < 21):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes == 10 or mes == 11) or (mes == 12 and dia < 21):
        estacion = "Otoño"

# Hemisferio Sur
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes == 1 or mes == 2) or (mes == 3 and dia < 21):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes == 4 or mes == 5) or (mes == 6 and dia < 21):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes == 7 or mes == 8) or (mes == 9 and dia < 21):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes == 10 or mes == 11) or (mes == 12 and dia < 21):
        estacion = "Primavera"

else:
    estacion = "Hemisferio no válido"

# Imprimimos el resultado
print(f"Te encuentras en {estacion}.")              