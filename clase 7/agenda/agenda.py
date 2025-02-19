import sqlite3
#Ejercicio: 
#Crear un agenda de contactos con POO, errores y excepciones y utilizar una base de datos sqlite.

#Creando la clase 1: Contactos
class Contacto:
    def __init__(self, nombre, numero, correo):
        self.nombre = nombre
        self.numero = numero
        self.correo = correo

#Creando la clase 2: Agenda
class Agenda:
    def __init__(self, db_nombre="agenda.db"):
        self.db_nombre = db_nombre
        self.conectar_db()

    #Función para conectar con la BD
    def conectar_db(self):
        self.conn = sqlite3.connect(self.db_nombre)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS contactos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                numero TEXT,
                correo TEXT
            )''')
        self.conn.commit()
    
    #Función para crear contacto
    def agregar_contacto(self, contacto):
        try:
            self.cursor.execute("INSERT INTO contactos (nombre, numero, correo) VALUES (?, ?, ?)",
                                (contacto.nombre, contacto.numero, contacto.correo))
            self.conn.commit()
            print("Contacto agregado exitosamente.")
        except sqlite3.Error as e:
            print(f"Error al agregar el contacto: {e}")
        
    #Función para buscar contacto
    def buscar_contacto(self, nombre):
        self.cursor.execute("SELECT * FROM contactos WHERE nombre = ?", (nombre,))
        contacto = self.cursor.fetchone()
        if contacto:
            print(f"ID: {contacto[0]}, \nNombre: {contacto[1]}, \nNummero: {contacto[2]}, \nCorreo: {contacto[3]}")
        else:
            print("Contacto no encontrado")

    #Función para eliminar un contacto
    def eliminar_contacto(self, nombre):
        self.cursor.execute("DELETE FROM contactos WHERE nombre = ?", (nombre,))
        self.conn.commit()
        if self.cursor.rowcount > 0:
            print("Contacto eliminado exitosamente.")
        else:
            print("No se encontró un contacto con ese nombre.")

    #Función para mostrar todos los contactos
    def mostrar_contactos(self):
        self.cursor.execute("SELECT * FROM contactos")
        contactos = self.cursor.fetchall()
        if contactos:
            for contacto in contactos:
                print(f"ID: {contacto[0]}, \nNombre: {contacto[1]}, \nNumero: {contacto[2]}, \nCorreo: {contacto[3]}")
            else:
                print("No hay contactos registrados.")
            
    #Función para cerrar la conexión con la BD
    def cerrar_conexion(self):
        self.conn.close()

if __name__ == "__main__":
    agenda = Agenda()
    while True:
        print("AGENDA DE CONTACTOS")
        print("______________________")
        print("\n1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar todos los contactos")
        print("5. Salir")
        opcion = int(input("\nSeleccione una opción: "))

        #Opciones de las funciones
        if opcion == 1:
            nombre = input("Nombre: ")
            numero = input("Numero: ")
            correo = input("Correo: ")
            contacto = Contacto(nombre, numero, correo)
            agenda.agregar_contacto(contacto) 
        elif opcion == 2:
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            agenda.buscar_contacto(nombre)
        elif opcion == 3:
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            agenda.eliminar_contacto(nombre)
        elif opcion == 4:
            agenda.mostrar_contactos()
        elif opcion == 5:
            agenda.cerrar_conexion()
            break
        else:
            print("Opción no válida. Intente de nuevo.")
