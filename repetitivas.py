#1)
for i in range(0, 101):
    print(i)

#2)
num = int(input("Ingrese un numero entero: "))
cantidad_digitos = len(str(abs(num))) # abs() para manejar numeros negativos
print("La cantidad de digitos es:", cantidad_digitos)

#3)
num1 = int(input("Ingrese el primer numero entero: "))
num2 = int(input("Ingrese el segundo numero entero: "))
inicio = min(num1, num2) + 1 #para no incluir el numero de inicio
fin = max(num1, num2) #ya no lo incluye por definicion de range
suma = 0

for i in range(inicio, fin):
    suma += i # suma = suma + i
print ("La suma de los numeros entre", num1, "y", num2, "es:", suma)

#4)
suma_total = 0

while True: 
    num = int(input("Ingrese un numero entero (0 para terminar): "))
    if num == 0:
        break
    suma_total += num # suma_total = suma_total + num
print("La suma total de los numeros ingresados es:", suma_total)

#5)
import random
num_aleatorio = random.randint(0, 9) # Genera un numero aleatorio entre 0 y 9
intentos = 0 # Contador de intentos

while True:
    intentos += 1
    num_usuario = int(input("Adivine el numero (entre 0 y 9): "))
    if num_usuario == num_aleatorio:
        print(f"¡Felicidades! Adivinaste el numero en {intentos} intentos.")
        break
    else:
        print("Numero incorrecto. Intenta de nuevo.")

#6)
for i in range(100,-1,-1):# Cuenta regresiva de 100 a 0
    if i % 2 == 0: # Verifica si el numero es par
        print(i)

#7)
num = int(input("Ingrese un numero entero positivo: "))
suma = 0
for i in range(0, num + 1):
    suma += i # suma = suma + i
print(f"La suma de los numeros desde 0 hasta {num} es: {suma}")

#8)
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(100):
    num = int(input(f"Ingrese el numero {i+1}: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print(f"Cantidad de numeros pares: {pares}")
print(f"Cantidad de numeros impares: {impares}")
print(f"Cantidad de numeros positivos: {positivos}")
print(f"Cantidad de numeros negativos: {negativos}")

#9)
suma = 0

for i in range(100):
    num = int(input(f"Ingrese el numero {i+1}: ")) 
    suma += num # suma = suma + num

media = suma / 100 
print(f"La media de los 100 numeros ingresados es: {media}")

#10)
num = input("Ingrese un numero: ")
num_invertido = ""

for digito in num:
    num_invertido = digito + num_invertido
print("El numero invertido es:", num_invertido)