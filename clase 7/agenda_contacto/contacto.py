class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    
    def __str__(self):
        return f"""
        nombe : {self.nombre}
        telefono : {self.telefono}
        email : {self.email}
                """

if __name__ == "__main__":
    contacto = Contacto ("Rodrigo","111111","email@gmail.com")
    print(contacto)