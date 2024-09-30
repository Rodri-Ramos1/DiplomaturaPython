import utilidades

contactos =[]

#Variable Global
running =  True

while running:
    respuesta = utilidades.opciones()

    if respuesta == 1:
        contacto = utilidades.crear_contacto()
        contactos.append(contacto)
    elif respuesta == 2:
        utilidades.mostrar_lista(contactos)
    elif respuesta == 3:
        utilidades.eliminar_contacto(contactos)
    elif respuesta == 4:
        try:
            contacto = utilidades.buscar_contacto(contactos)
        except TypeError:
            print("Falta argumento contactos")
        utilidades.mostrar_contacto(contacto)
    else:
        print("Saliendo del programa")
        running = False

