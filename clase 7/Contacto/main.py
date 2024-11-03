import util_bd

conexion = util_bd.crear_base_datos("contacto.db")

util_bd.crear_tabla_contacto(conexion)

conexion.close()