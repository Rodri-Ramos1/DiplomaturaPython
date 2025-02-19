import sqlite3 as db

def crear_bd(db_nombre):
    return db.connect(db_nombre)

def crear_tabla(conexion, sql):
    cursor = conexion.cursor()
    cursor.execute (sql)