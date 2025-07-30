# Solicitar al usuario el número de la tabla de multiplicar
numero = int(input("Ingrese el número de la tabla de multiplicar que desea mostrar: "))

# Mostrar la tabla de multiplicar usando un for
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")