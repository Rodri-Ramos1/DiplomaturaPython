import sqlite3

conexion = sqlite3.connect("tienda.db")

cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(100),
    direccion VARCHAR(255),
    telefono VARCHAR(20),
    email VARCHAR(100)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(100),
    descripcion TEXT,
    precio DECIMAL(10, 2),
    stock INTEGER
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ventas(
    id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER,
    fecha_venta DATE,
    total DECIMAL(10, 2)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS detalle_venta(
    id_cetalle INTEGER PRIMARY KEY AUTOINCREMENT,
    id_venta INTEGER,
    id_producto INTEGER,
    cantidad INTEGER,
    precio_unitario DECIMAL(10, 2),
    subtotal DECIMAL(10, 2)
);
""")


conexion.commit()
conexion.close()