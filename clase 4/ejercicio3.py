#Variables por defecto
a = 10
b = 30
c = 20

#Opciones matemáticas
print("Usuario elige la operación matematica")
print("1 - suma")
print("2 - resta") 
print("3 - producto")
print("4 - division")
opcion = int(input("Ingrese opcion: ")) 

#Condicional IF
if opcion == 1:
    suma = a + b + c
    print(f"Suma: {suma}")
if opcion == 2:
    resta = a - b - c
    print(f"Resta: {resta}")
if opcion == 3:
    producto = a * b * c
    print(f"Producto: {producto}")
if opcion == 4:
    division = a / b / c 
    print(f"division: {division}")