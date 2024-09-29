#CRUD - ABM
#Crear contactos
def crear_contacto():
    nombre = input("Inngrese el nombre: ")
    telefono = input ("Ingrese el telefono: ")
    email = input("Ingrese el email: ")

    contacto = {"nombre": nombre,
                "telefono": telefono, 
                "email": email}
    
    return contacto



#Buscar contactos
#Mostrrar cotactos
#Eliminar contactos