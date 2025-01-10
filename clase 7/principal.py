import base_dato

base = base_dato.crear_bd("PrimeraBase.db")
base_dato.crear_tabla(base,"""CREATE TABLE contacto(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(50),
                telefono VARCHAR(20),
                email VARCHAR(50)
                );
                """)
base.close()