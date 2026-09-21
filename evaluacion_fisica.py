print("ASISTENTE DE EVALUACIÓN FÍSICA")

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
peso = float(input("Ingrese su peso en kg: "))
horas_ejercicio = float(input("Ingrese sus horas de ejercicio a la semana: "))

calorias = horas_ejercicio * 350

if edad < 18:
    categoria = "Juvenil"
else:
    categoria = "Adulto"

if horas_ejercicio >= 3:
    estado = "Físicamente Activo"
else:
    estado = "Requiere mayor actividad física"

print(f"\nRESUMEN DE EVALUACIÓN FÍSICA")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Peso: {peso:.2f} kg")
print(f"Calorías quemadas estimadas por semana: {calorias:.2f}")
print(f"Categoría: {categoria}")
print(f"Estado: {estado}")
