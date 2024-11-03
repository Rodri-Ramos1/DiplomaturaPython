import sqlite3

def crear_base_datos(nombre_db):
    try:
        conexion = sqlite3.connect(nombre_db)
        return conexion
    except Exception:
        print("No se pudo crea la base de datos")

def crear_tabla_contacto(conexion):
    cursor = conexion.cursor()
    try:
        cursor.execute("""CREATE TABLE contacto (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre VARCHAR(50),
                            telefono VARCHAR(20),
                            email VARCHAR(50),
                    )""")
    except sqlite3.OperationalError:
        print ("Ya existe la tabla")
    #cursor.commit()
def cerrar_conexion(conexion):
    conexion.close()
