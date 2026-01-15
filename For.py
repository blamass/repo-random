# For

# 1. Mostrar los números ascendentes desde el 1 al 10

for num in range (1,10):
    print(num)

# 2. Mostrar los números descendentes desde el 10 al 1

for num in range (10,0,-1):
    print(num)

# 3. Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.

num = int(input("Ingrese un número: "))

for num in range (0, num + 1):
    print(num)

# 4. Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:

# 	5 x 0 = 0
# 	5 x 1  = 5
# 	5 x 2 = 10
# 	5 x 3  = 15 …

num = int(input("Ingrese un número: "))

for i in range (0, 11):
    tabla = num * i
    print (f"{num} x {i} = {tabla}")


# 5. Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.

suma = 0
contador = 0

for i in range (0,11):
    num = int(input("Ingrese un número: "))
    suma += num
    contador += 1
    if num == 0:
        break

promedio = suma / contador

print(f"La suma de los números es: {suma}")
print(f"El promedio de los números es: {promedio}")

# 6. Imprimir los números múltiplos de 3 entre el 1 y el 10.

print("Múltiplos de 3 entre el 1 y el 10: ")
for i in range (1,11):
    if i % 3 == 0:
        print(i)

# 7. Mostrar los números pares que hay desde la unidad hasta el número 50.

print("Números pares desde la unidad hasta el número 50: ")
for i in range (1,51):
    if i % 2 == 0:
        print(i)

# 8. Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:

# 1
# 12
# 123
# 1234
# 12345

numero = int(input("Ingrese un número: "))

for i in range (1,numero + 1):
    for j in range (1, i + 1):
        print(j, end = "")
    print()

# 9. Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.

numero = int(input("Ingrese un número: "))

print(f"Los divisores de {numero} son:")
for i in range(1,numero + 1):
    if numero % i == 0:
        print(i)

# 10. Ingresar un número. Determinar si el número es primo o no.

numero = int(input("Ingrese un número: "))
contador = 0

for i in range(2,numero + 1):
    if numero % i == 0:
        contador += 1
    
if numero > 1 and contador == 1:
    print("El numero es primo.")
else:
    print("El numero no es primo.")

# 11. Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.

numero = int(input("Ingrese un número: "))
contador_primos = 0

for i in range(1,numero + 1):
    contador = 0
    for j in range (1, i + 1):
        if i % j == 0:
            contador += 1
    if contador == 2:
        print(i)
        contador_primos += 1

print(f"Numeros primos encontrados: {contador_primos}")