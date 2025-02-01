import funciones

running = True
while running:
    respuesta = funciones.opciones()

    if respuesta == 1:
        resultado = funciones.suma()
        print(f"El resultado de la suma es {resultado}")
    elif respuesta == 2:
        resultado = funciones.resta()
        print(f"El resultado de la resta es {resultado}")
    elif respuesta == 3:
        resultado = funciones.multiplicar()
        print(f"El resultado de la multiplicación es {resultado}")
    elif respuesta == 4:
        resultado = funciones.division()
        print(f"El resultado de la división es {resultado}")
    elif respuesta == 5:
        resultado = funciones.potencia()
        print(f"La potencia es {resultado}")
    elif respuesta == 6:
        resultado = funciones.raizCuadrada()
        print(f"La raiz cuadrada es {resultado}")
    elif respuesta == 7:
        resultado = funciones.seno()
        print(f"El seno es {resultado}")