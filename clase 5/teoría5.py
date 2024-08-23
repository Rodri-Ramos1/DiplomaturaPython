#Definir una lista 
listaVacia = []
lista = [1,2,3]

#Definir tuplas
tuplaVacia = ()
tupla = (1,2,3,4) #O también: tupla = 1,2,3,4

#Definir diccionarios
dicVacio = {}
diccionario = {"nombre": "Rodrigo",
               "edad": 32
               } 

#Condiconales
if lista[0] == 8:
    print(f"El primer elmento es un 8")
elif lista[1] == 8:
    print(f"El segundo elemneto es un 8")
else: 
    print(f"El primier elemento es un {lista[0]}")

#Bucles
#for
for i in range(len(lista)):
    print(i)
for elemento in lista:
    print(f"Elemento: {elemento}")

#While
contador = 0
while contador < 2: #si contador es menor a 2 vamos a suma/contarr.
    print(contador) 
    contador += 1


