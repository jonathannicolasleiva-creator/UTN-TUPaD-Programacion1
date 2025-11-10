#EJERICIO 1
def imprimir_hola_mundo(): #defino la funcion
    print(f"Hola, Mundo!") #imprimo el mensaje

imprimir_hola_mundo() #llamo a la funcion   

#EJERCICIO 2
def saludar_usuario(nombre): #defino la funcion
    return (f"Hola, {nombre}!") #retorno el saludo con el nombre

nombre = input("Ingrese su nombre: ") #pido al usuario que ingrese su nombre

saludo = saludar_usuario(nombre) #llamo a la funcion y guardo el resultado en una variable

print(saludo) #imprimo el saludo

#EJERCICIO 3
def informacion_personal(nombre, apellido, edad, residencia): #defino la funcion con cuatro parametros
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.") #imprimo la informacion personal

# Pido los datos al usuario
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia) #llamo a la funcion con los datos ingresados

#EJERCICIO 4
import math #importo la libreria math para usar pi

def calcular_area(radio): #defino la funcion que calcula el area que recibe el radio
    return math.pi * radio ** 2

def calcular_perimetro(radio):#: #defino la funcion que calcula el perimetro que recibe el radio
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del circulo: ")) #pido al usuario que ingrese el radio

resultado_area = calcular_area(radio) #llamo a la funcion que calcula el area y guardo el resultado en una variable
resultado_perimetro = calcular_perimetro(radio) #llamo a la funcion que calcula el perimetro y guardo el resultado en una variable

print(f"El area del circulo es: {resultado_area}") #imprimo el area

print(f"El perimetro del circulo es: {resultado_perimetro}")#imprimo el perimetro

#EJERCICIO 5
def segundos_a_horas(segundos):#definimos la funcion y colocamos el parametro segundos
    return segundos / 3600 #retornamos el resultado de dividir los segundos por 3600

seg = int(input("Ingrese la cantidad de segundos: ")) 

horas = segundos_a_horas(seg) #llamamos a la funcion y guardamos el resultado en una variable

print(f"{seg} segundos son {horas:.2f} horas.") #imprimimos el resultado

#EJERCICIO 6
def tabla_de_multiplicar(numero): #defino la funcion que recibe un numero
    for i in range(1, 11): #bucle que va del 1 al 10
        print(f"{numero} x {i} = {numero * i}") #imprimo la tabla de multiplicar

num = int(input("Ingrese un numero para ver su tabla de multiplicar: ")) 

tabla_de_multiplicar(num) #llamo a la funcion con el numero ingresado

#EJERCICIO 7
def operaciones_basicas(a, b): #defino la funcion con dos parametros
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = None  # Para evitar división por cero

    return suma, resta, multiplicacion, division

num1 = input("Ingresa el primer número: ")
num2 = input("Ingresa el segundo número: ")

# convierto las entradas a float
a = float(num1) 
b = float(num2)
suma, resta, multiplicacion, division = operaciones_basicas(a, b) #llamo a la funcion y guardo los resultados en variables

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")

if division is not None:
    print(f"División: {division}")
else:
    print("División: no se puede dividir por cero.")

#EJERCICIO 8
def calcular_imc(peso, altura): #defino la funcion con los parametros peso y altura
    return peso / (altura ** 2) #retorna el resultado de dividir el peso por la altura al cuadrado

peso = float(input("Ingrese su peso en kilogramos: ")) 
altura = float(input("Ingrese su altura en metros (por ejemplo 1.75): "))

imc = calcular_imc(peso, altura) #llamamos a la funcion y guardamos el resultado en una variable

print(f"Su IMC es: {imc:.2f}") #imprimimos el resultado con dos decimales

#EJERCICIO 9
def celsius_a_fahrenheit(celsius): #defino la funcion con el parametro celsius
    return (celsius * 9/5) + 32 #retorna la conversion de grados celsius a fahrenheit

celsius = float(input("Ingrese la temperatura en grados Celsius: "))

fahrenheit = celsius_a_fahrenheit(celsius) #llamamos a la funcion y guardamos el resultado en una variable

print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F") #imprimimos el resultado con dos decimales

#EJERCICIO 10
def calcular_promedio(a, b, c): #definimos la funcion con tres parametros numericos
    return (a + b + c) / 3 #retornamos el promedio de los tres numeros

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

promedio = calcular_promedio(num1, num2, num3) #llamamos a la funcion y guardamos el resultado en una variable

print(f"El promedio de {num1}, {num2} y {num3} es: {promedio:.2f}") #imprimimos el resultado con dos decimales

