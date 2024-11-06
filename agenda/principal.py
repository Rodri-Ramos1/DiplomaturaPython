import util_db as db 
conexion = db.conectar_db('agenda.db')

db.crear_tabla(conexion)

#Insertar contactos
db.insertar_contacto(conexion, "Quispe", "Juan", "111111111", "juan@gmail.com")
db.insertar_contacto(conexion, "Tevez", "Pedro", "222222222", "Pedro@gmail.com")
db.insertar_contacto(conexion, "Messi", "Lionel", "333333333", "lionel@gmail.com")

#Consultar y mostrar todos los usuarios
contacto = db.consultar_todos_contactos(conexion)
for contacto in contacto:
    print(contacto)

db.cerrar_conexion(conexion)
