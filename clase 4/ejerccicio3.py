#Variables por defecto

a = 10
b = 30
c = 20

#while True: #while es un ciclo. No se como hizo para avanzar todo una línea.
#para hacerlo más complejo
print("Usuario elige la operación matematica")
print("1 - suma")
print("2 - resta") #ingresar el número 2 para hacer una resta
print("3 - producto")
print("4 - dividison")
opcion = int(input("Ingrese opcion: ")) #para que la persona eliga

if opcion == 1:
    suma = a + b + c
    print(f"Suma: {suma}")
if opcion == 2:
    resta = a - b - c
    print(f"Resta: {resta}")
if opcion == 3:
    producto = a * b * c
    print(f"Producto: {producto}")