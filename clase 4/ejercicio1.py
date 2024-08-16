nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

#Para saber el tipo de la variable
print (type(nombre))
print (type(edad))

#Conversión (en este caso la edad "cadena" se conviernte en int)
#edad = int(input("Ingrese su nombre: "))
"""
float() convierte a float
bool() convierte a boolean
str() convierte a string
int() convierte a int
"""
print(f"Hola, {nombre} tu edad es {edad}")
#Parametros
"""
mensaje = f"Hola, {nombre} tu edad es  {edad}"
print(mensaje)
print(type(nombre))
print(type(edad))
"""