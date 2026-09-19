print("--Asistente de Triaje")

nombre = input("Ingrese el nombre del paciente: ")
peso = float(input("Ingrese el peso en kg: "))
altura = float(input("Ingrese la altura en metros: "))
temperatura = float(input("ingrese la temperatura en °C: "))


imc = peso / (altura ** 2)

print(f"--Resultados del triaje para {nombre} -----")

print(f"IMC calculado: {imc:.2f}")

if imc >= 25.0:
    print("El paciente esta en sobrepeso")
else:
    print("Estado de peso dentro de lo normal")

if temperatura >= 38.0:
    print("El paciente esta con fiebre")
else:
    print("Temperatura normal")