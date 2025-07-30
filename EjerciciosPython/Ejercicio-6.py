# Solicitar al usuario el número para la tabla de multiplicar
numero = int(input("Ingrese el número para la tabla de multiplicar: "))

# Inicializar el contador
i = 1

# Ciclo while para mostrar la tabla de multiplicar del número ingresado
while i <= 10:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    i += 1

