import sqlite3

def get_connection():
    return sqlite3.connect('tienda.db')

def insert_cliente(nombre, direccion, telefono, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(""""
        INSERT INTO clientes (nombre, direccion, telefono, email)
        VALUES (?, ?, ?, ?)
    """, (nombre, direccion, telefono, email))
    conn.commit()
    conn.close()
    
def insert_producto(nombre, descripcion, precio, stock):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute ("""
        INSERT INTO productos (nombre, descripcion, precio, stock)
        VALUES (?, ?, ?, ?)
    """, (nombre, descripcion, precio, stock))
    conn.commit()
    conn.close()

def insert_venta(id_cliente, fecha_venta, total):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO ventas (id_cliente, fecha_venta, total)
        VALUES (?, ?, ?)
    """, (id_cliente, fecha_venta, total))
    conn.commit()
    conn.close()

def insert_detalle_venta(id_venta, id_producto, cantidad, precio_unitario, subtotal):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                   INSERT INTO detalle_venta (id_venta, id_producto, cantidad, precio_unitario, subtotal)
                   VALUES (?, ?, ?, ?, ?)
    """, (id_venta, id_producto, cantidad, precio_unitario, subtotal))
    conn.commit()
    conn.close()


#Me falta muchos por completar..

def get_cliente():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes')
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_productos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM productos')
    rows = cursor.fetchall()
    conn.close()
    return rows