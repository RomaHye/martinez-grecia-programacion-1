# lab_U3_L1_martinez_grecia.py

# ==========================================
# Ejercicio 1: Clasificación por edad
# ==========================================
print("--- Ejercicio 1: Clasificación por edad ---")
edad = int(input("Ingresa tu edad: "))

if edad < 13:
  print("Clasificación: niño")
elif 13 <= edad <= 17:  # O simplemente 'elif edad <= 17:'
  print("Clasificación: adolescente")
else:
  print("Clasificación: adulto")


# ==========================================
# Ejercicio 2: Validar acceso (usuario y contraseña)
# ==========================================
print("\n--- Ejercicio 2: Validar acceso ---")
usuario_correcto = "admin123"
pass_correcta = "secreto"

usuario_ingresado = input("Ingresa el usuario: ")
pass_ingresada = input("Ingresa la contraseña: ")

if usuario_ingresado == usuario_correcto and pass_ingresada == pass_correcta:
  print("acceso concedido")
elif usuario_ingresado == usuario_correcto and pass_ingresada != pass_correcta:
  print("contraseña incorrecta")
else:
  print("usuario no encontrado")


# ==========================================
# Ejercicio 3: Calculadora de envío
# ==========================================
print("\n--- Ejercicio 3: Calculadora de envío ---")
peso = float(input("Ingresa el peso del paquete en kg: "))

if peso <= 1:
  costo = 50.0
elif peso <= 5:  # Cubre más de 1 y hasta 5
  costo = 90.0
else:
  costo = 150.0

# Descuento adicional del 10% si pesa más de 10 kg
if peso > 10:
  costo = costo * 0.90
  print("¡Se aplicó un 10% de descuento por peso mayor a 10 kg!")

print(f"El costo total de envío es: ${costo:.2f}")


# ==========================================
# Ejercicio 4: Clasificar la temperatura
# ==========================================
print("\n--- Ejercicio 4: Clasificar la temperatura ---")
temperatura = float(input("Ingresa la temperatura en grados: "))

if temperatura < 10:
  print("Clasificación: frío")
elif 10 <= temperatura <= 24:
  print("Clasificación: templado")
else:
  print("Clasificación: calor")


# ==========================================
# Ejercicio 5: Calificación con letras
# ==========================================
print("\n--- Ejercicio 5: Calificación con letras ---")
calificacion = float(input("Ingresa una calificación de 0 a 100: "))

if calificacion >= 90:
  print("Calificación en letra: A")
elif calificacion >= 80:
  print("Calificación en letra: B")
elif calificacion >= 70:
  print("Calificación en letra: C")
elif calificacion >= 60:
  print("Calificación en letra: D")
else:
  print("Calificación en letra: F")


# ==========================================
# Ejercicio 6: Descuento por monto de compra
# ==========================================
print("\n--- Ejercicio 6: Descuento por monto de compra ---")
monto = float(input("Ingresa el monto de la compra: $"))

if monto > 500:
  descuento_porcentaje = 20
elif monto > 200:
  descuento_porcentaje = 10
else:
  descuento_porcentaje = 0

monto_final = monto * (1 - descuento_porcentaje / 100)
print(f"Porcentaje de descuento: {descuento_porcentaje}%")
print(f"Monto final a pagar: ${monto_final:.2f}")


# ==========================================
# Ejercicio 7: Validar un rango con comparación encadenada
# ==========================================
print("\n--- Ejercicio 7: Validar rango ---")
numero = int(input("Ingresa un número entero: "))

if 1 <= numero <= 100:
  print(f"El número {numero} sí está en el rango de 1 a 100.")
else:
  print(f"El número {numero} no está en el rango de 1 a 100.")


# ==========================================
# Ejercicio 8: Clasificar el IMC
# ==========================================
print("\n--- Ejercicio 8: Clasificar el IMC ---")
peso_imc = float(input("Ingresa tu peso en kg: "))
estatura_imc = float(input("Ingresa tu estatura en metros (ej. 1.75): "))

imc = peso_imc / (estatura_imc**2)
print(f"Tu IMC calculado es: {imc:.2f}")

if imc < 18.5:
  print("Clasificación IMC: bajo peso")
elif 18.5 <= imc <= 24.9:
  print("Clasificación IMC: normal")
elif 25 <= imc <= 29.9:
  print("Clasificación IMC: sobrepeso")
else:
  print("Clasificación IMC: obesidad")


# ==========================================
# Ejercicio 9: Tarifas de electricidad
# ==========================================
print("\n--- Ejercicio 9: Tarifas de electricidad ---")
consumo = float(input("Ingresa el consumo mensual en kWh: "))

if consumo <= 150:
  costo_total = consumo * 1.20
elif consumo <= 300:
  # Primeros 150 a $1.20, el resto a $1.80
  costo_total = (150 * 1.20) + ((consumo - 150) * 1.80)
else:
  # Primeros 150 a $1.20, siguientes 150 a $1.80, y el excedente a $2.50
  costo_total = (150 * 1.20) + (150 * 1.80) + ((consumo - 300) * 2.50)

print(f"Consumo: {consumo} kWh")
print(f"Costo total: ${costo_total:.1f}")
