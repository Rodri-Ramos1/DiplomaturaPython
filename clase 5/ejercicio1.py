#Declarar una lista vacia
lista = []

for i in range(5):
    numero = int(input("Ingrese el numero: "))
    lista.append(numero)


#Acumuladores - Contadores
suma_total = 0

for numero in lista:
    suma_total += numero

print(f"La suma de los elementos de la lista de numeros es:  {suma_total}")


#Funciones
def suma(lista):
    return sum(lista)

#Slince
lista2 =[1,2,3]
print(lista2[::-1])
print(suma(lista2))