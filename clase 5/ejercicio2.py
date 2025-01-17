#Declarando una lista
lista = [1,2,3,4,5,6,7,8,9,10]

#Solicitar un número
numeroIngresado = int(input("Ingrese un número: "))

#Variable verdadero o falso
encontrado = False

#Bucle for
for num in lista:
    if num == numeroIngresado:
        encontrado = True
        break

#Condicional if - else
if encontrado:
    print(f"El número {numeroIngresado} se encunetra en la lista")
else:
    print(f"El número {numeroIngresado} no está en la lista")