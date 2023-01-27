from tkinter import *
from tkinter import filedialog as FileDialog
from io import open
from tkinter import messagebox as mb

ruta = "" 

def nuevo():
    global ruta
    mensaje.set("Nuevo fichero")
    question = mb.askquestion("Nuevo fichero","Se borrara todo el contenido, quiere crear un nuevo fichero?")
    if question == 'yes':
        ruta= ""
        """ borra desde el primer caracter hasta el final"""
        texto.delete(1.0, END) 
    
    
    
def abrir():
    global ruta
    mensaje.set("Abrir fichero")
    ruta = FileDialog.askopenfilename(initialdir='.',filetype=(("Ficheros de texto","*.txt"),), title="Abrir un fichero de texto")
    if ruta != "":
        fichero = open(ruta,'r')
        contenido = fichero.read()
        texto.delete(1.0,'end')
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + "- EdiText")
    
    
    
def guardar():
    global ruta
    mensaje.set("Guardar fichero")
    """Fichero previamente exitente"""
    if ruta != "":
        contenido = texto.get(1.0, 'end-1c')#guarda todo menos el ultimo caracter que es un salto de linea
        fichero = open(ruta,'w+')
        fichero.write(contenido)
        fichero.close()
        mb.showinfo("","Se guardo correctamente")
    else:
        guardar_como()
        mb.showinfo("","Se guardo correctamente")
    
def guardar_como():
    global ruta
    mensaje.set("Guardar fichero como")
    fichero = FileDialog.asksaveasfile(title="guardar fichero", mode="w", defaultextension=".txt")
    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mb.showinfo("","Se guardo correctamente")
    else:
        mb.showinfo("","Guardado cancelado")
        ruta = ""

def salir():
    question = mb.askquestion("Salir", "Esta seguro de que quiere cerrar el programa")
    if question == "yes" :
        root.quit()
#configuración de la raíz
root = Tk()
root.title("EdiText")
root.iconbitmap("hola.ico")
#menu superior
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nuevo", command=nuevo)
file_menu.add_command(label="Abrir", command=abrir)
file_menu.add_command(label="Guardar", command=guardar)
file_menu.add_command(label="Guardar como", command=guardar_como)
file_menu.add_separator()
file_menu.add_command(label="salir", command=salir)
menu_bar.add_cascade(menu=file_menu, label="Archivo")

#caja central
texto = Text(root)
texto.pack(fill="both",expand=1)
texto.config(bd=0, padx=6, pady=4, font=("consolas",12))

#pantalla inferior
mensaje = StringVar()
mensaje.set("Bienvenido a EdiText")
monitor = Label(root, textvar=mensaje, justify='left')
monitor.pack(side="left")
root.config(menu=menu_bar)
#bucle de la aplicación
root.mainloop()