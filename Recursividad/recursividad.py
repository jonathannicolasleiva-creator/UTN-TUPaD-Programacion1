# Punto 1

def factorial(n):
    # Caso base: factorial de 0 es 1
    if n == 0:
        return 1
    else:
        # Caso recursivo: n! = n * (n-1)!
        return n * factorial(n - 1)

# Pedido de número al usuario
num = int(input("Ingrese un número: "))

print("Factoriales desde 1 hasta", num)
for i in range(1, num + 1):
    # Se muestra el factorial de cada número de 1 a N
    print(f"{i}! = {factorial(i)}")

# Punto 2

def fibonacci(pos):
    # Casos base:
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        # Caso recursivo: F(n) = F(n-1) + F(n-2)
        return fibonacci(pos - 1) + fibonacci(pos - 2)

num = int(input("Ingrese la posición máxima de Fibonacci: "))

print("Serie de Fibonacci:")
for i in range(num + 1):
    # Se imprime cada valor de la serie desde 0 hasta N
    print(fibonacci(i), end=" ")

# Punto 3

def potencia(n, m):
    # Caso base: cualquier número elevado a 0 es 1
    if m == 0:
        return 1
    else:
        # Caso recursivo: n^m = n * n^(m-1)
        return n * potencia(n, m - 1)

base = int(input("Base: "))
expo = int(input("Exponente: "))

print(f"{base}^{expo} =", potencia(base, expo))

# Punto 4

def decimal_a_binario(n):
    # Caso base: cuando n llega a 0, se deja de dividir
    if n == 0:
        return ""
    else:
        # Convertimos el número dividiéndolo por 2
        # El binario se forma concatenando los restos
        return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("Ingrese un número decimal: "))

binario = decimal_a_binario(num)

# Si el número era 0, la función devuelve cadena vacía
print(f"El número binario es: {binario if binario != '' else '0'}")

# Punto 5

def es_palindromo(palabra):
    # Caso base: palabra vacía o de 1 letra siempre es palíndromo
    if len(palabra) <= 1:
        return True

    # Si la primera y última letra son distintas → no es palíndromo
    if palabra[0] != palabra[-1]:
        return False

    # Caso recursivo: comparar el resto de la palabra (sin extremos)
    return es_palindromo(palabra[1:-1])

pal = input("Ingrese una palabra sin espacios ni tildes: ").lower()

print("¿Es palíndromo?:", es_palindromo(pal))

# Punto 6
    
def suma_digitos(n):
    # Caso base: si n es un solo dígito, lo devolvemos
    if n < 10:
        return n
    else:
        # Tomamos el último dígito con % 10
        # Y el resto del número con // 10
        return (n % 10) + suma_digitos(n // 10)

num = int(input("Ingrese un número: "))
print("Suma de dígitos:", suma_digitos(num))

# Punto 7

def contar_bloques(n):
    # Caso base: si solo hay 1 nivel, hay 1 bloque
    if n == 1:
        return 1
    else:
        # Caso recursivo:
        # Total = bloques del nivel actual + bloques restantes
        return n + contar_bloques(n - 1)

niveles = int(input("Bloques en el nivel inferior: "))
print("Total de bloques necesarios:", contar_bloques(niveles))

# Punto 8

def contar_digito(numero, digito):
    # Caso base: cuando el número llega a 0 terminamos
    if numero == 0:
        return 0

    # Tomamos el último dígito del número
    ultimo = numero % 10

    # Si coincide con el dígito buscado, contamos 1
    if ultimo == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        # Si no coincide, solo seguimos con los demás dígitos
        return contar_digito(numero // 10, digito)

num = int(input("Ingrese un número: "))
dig = int(input("Dígito a buscar: "))

print("Aparece:", contar_digito(num, dig), "veces")
   