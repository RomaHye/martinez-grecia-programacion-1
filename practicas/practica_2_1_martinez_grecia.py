# Ejercicio 1 - Datos personales

nombre = "Grecia"
edad = 25
ciudad = "Guadalajara"

print(nombre, edad, ciudad)
# Ejercicio 2 - Actualizar un contador

contador = 0
contador = contador + 1
print(contador)
contador = contador + 1
print(contador)

contador = contador + 1
print(contador)
# Ejercicio 3 - Constante de conversión

PULGADAS_A_CM = 2.54
pulgadas = 10
centimetros = pulgadas * PULGADAS_A_CM
print(centimetros)
# Ejercicio 4 - Área de un rectángulo

base = 5
altura = 9
area = base * altura
print(area)
print("El área es:", area)
# Ejercicio 5 - Total con IVA

IVA = 0.16
precio = 200
total = precio + precio * IVA
print("El total con IVA es:", total)
# Ejercicio 6 - Intercambio de valores

a = 10
b = 20

print("Antes del intercambio:", a, b)
temp = a
a = b
b = temp
print("Después del intercambio:", a, b)
# Ejercicio 7 - Tipos básicos

numero_entero = 25
numero_decimal = 1.68
texto = "Grecia"
booleano = True
print(type(numero_entero))
print(type(numero_decimal))
print(type(texto))
print(type(booleano))
# Ejercicio 8 - Convertir tipos

texto_numero = "25"
numero = int(texto_numero)
print(numero, type(numero))
numero_entero_2 = 50
numero_texto = str(numero_entero_2)
print(numero_texto, type(numero_texto))

# Ejercicio 9 - Booleanos y comparaciones

a = 8
b = 3
mayor = a > b
print(mayor, type(mayor))



