print("############################################")
print("############## Calculadora #################")
datoUno =  int(input("Introduce el primer dato: "))
datoDos =  int(input("Introduce el segundo dato: ")) 
print("########## Seleccione la Operacion ##########")
print("##########  1 Suma  ###############")
print("##########  2 Resta ###############")
print("##########  3 Multiplicacion ######")
print("##########  4 Division  ###########")
op = int(input("Seleccione la operacion: "))
print("############################################")

if op == 1:
    resultado = datoUno + datoDos
    print("El resultado de la operacion suma:",resultado)
elif op == 2:
    resultado = datoUno - datoDos
    print("El resultado de la operacion resta:",resultado)
elif op == 3:
    resultado = datoUno * datoDos
    print("El resultado de la operacion multiplicacion:",resultado) 
elif op == 4:
    if datoDos != 0:
        resultado = datoUno / datoDos
        print("El resultado de la operacion division:",resultado)
    else:
        print("Error: Division por cero no permitida.")
else:
    print("Operacion no valida. Por favor, seleccione una operacion del 1 al 4.")