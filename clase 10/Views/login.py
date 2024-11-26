from tkinter import *
from tkinter import messagebox

def verificar_login(ventana_login,usuario,password):
    #usuario_bd = selesctUsuario()
    if usuario == "admin" and password == "1234":
        abrir_ventana_principal(ventana_login)
        #messagebox.showwarning("Exito", "Incio de Sesion correcta")
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrecta")
    
def abrir_ventana_principal(ventana_login):
    ventana_login.destroy()

    ventana_principal = Tk()
    ventana_principal.title("Incio")
    ventana_principal.geometry("500x600")

    label_bievenida = Label(ventana_principal, text="Bienvenido a la aplicacion...")
    label_bievenida.pack(pady=30)

    boton_salir = Button(ventana_principal, text="salir", command=ventana_principal.quit)
    boton_salir.pack(pady=20)

    return ventana_principal

def inicio_sesion():
    ventana_login = Tk()
    ventana_login.title("Inicio de Sesion")
    ventana_login.geometry("300x200")

    #Crear las etiquetas y los entrys
    label_usuario = Label(ventana_login, text = "Usuario: ")
    label_usuario.pack(pady=5)
    entry_usuario = Entry(ventana_login)
    entry_usuario.pack(pady=5)

    label_password = Label (ventana_login, text = "Contraseña")
    label_password.pack(pady=5)
    entry_password = Entry(ventana_login, show="*")
    entry_password.pack(pady=5)
    
    boton_login = Button(ventana_login, text="Iniciar Sesion", command = lambda: verificar_login(ventana_login,entry_usuario.get(),entry_password.get()))
    boton_login.pack(pady=5)
    
    ventana_login.mainloop()
