"""
Ejercicio 1: Sumar elementos de una lista. 
Crea una lista con 5 números enteros. Luego, recorre la lista con un ciclo for y suma todos los elementos. Finalmente, muestra el resultado usando un print
"""

#Declarar una lista vacia
lista = []

for i in range(5):
    numero = int(input("Ingrese el numero: "))
    lista.append(numero)

#Forma más rapida
"""
for i in range(5):
    lista.append(int(input("Ingrese el numero: ")))
print(lista)
"""
#Acumuladores - Contadores
suma_total = 0

for numero in lista:
    suma_total += numero

print(f"La suma de los elementos de la lista de numeros es:  {suma_total}")
#Funcion built in
"""
print(f"La suma de los elementos de la lista de numeros es:  {sum(lista)}")
"""

#Funciones
def suma(lista):
    return sum(lista)

#Slince
lista2 =[1,2,3]
print(lista2[::-1])
print(suma(lista2))