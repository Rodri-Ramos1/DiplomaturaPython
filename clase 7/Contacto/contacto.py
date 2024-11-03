class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    
    def __str__(self):
        return f"Nombre : {contacto.nombre} Telefono : {contacto.telefono}"
    
    def cambiar_telefono(self,telefono):
        self.telefono = telefono




if __name__ == "__main__":
    try:
        contacto = Contacto("Rodrigo","351444444","rodri.13@gmail.com") #Intanciando objetos
    except TypeError:
        print("Faltan parametros")
    print(f"Contacto : {contacto}")
    """print(f" Nombre: {contacto.nombre}")
    print(f" Telefono: {contacto.telefono}")
    print(f" Email: {contacto.email}")"""
    contacto.cambiar_telefono("351666666")
    print(contacto)
    