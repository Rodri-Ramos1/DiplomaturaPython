
def opciones():
    print("1-  Crear contacto")
    print("2- Mostrar contacto")
    print("3-  Eliminar contacto")
    print("4- Buscar contacto")
    opcion =int(input("Ingrese la opcion: "))
    return opcion

#CRUD - ABM
#Crear contactos
def crear_contacto():
    nombre = input("Inngrese el nombre: ")
    telefono = input ("Ingrese el telefono: ")
    email = input("Ingrese el email: ")

    contacto = {"nombre": nombre,
                "telefono": telefono, 
                "email": email
                }
    
    return contacto

#Buscar contactos
def buscar_contacto(contactos):
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    for contacto in contactos:
        if contacto[nombre] == nombre:
            return contacto

#Mostrar Lista de contactos
def mostrar_lista(contactos):
    for contacto in contactos:
        mostrar_contacto(contacto)

#Mostrrar cotactos
def mostrar_contacto(contacto):
    print(f"Nombre: {contacto["nombre"]}")
    print(f"Telefono: {contacto["telefono"]}")
    print(f"email: {contacto["email"]}")

#Eliminar contactos
def elimanr_contacto(contactos):
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    for contacto in contactos:
        if contacto[nombre] == nombre:
            contactos.remove(contacto)
