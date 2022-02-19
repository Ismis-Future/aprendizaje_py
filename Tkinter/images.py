#como insertar una imagen

import tkinter as tk
from tkinter import *
from tkinter.constants import RIGHT

ventana = tk.Tk()
ventana.title('Holas')


image_tk = tk.PhotoImage(file='img/logo.png') #con PhotoImage podemos insertar una imagen, con file indicamos la direccion o la imagen que querramos poner


label = tk.Label(ventana, image=image_tk).pack()

#side es para mover a la derecha cuando le cambiamos de tamaño

mensaje = """
Hola a todos yo soy ismael y estoy 
aprendiendo tkinter
"""

lblMensaje3 = tk.Label(ventana, text=mensaje, image=image_tk, compound=tk.CENTER).pack()
#lblMensaje = tk.Label(ventana, image=image_tk).pack(side= 'right')

#lblMensaje2 = tk.Label(ventana, image=image_tk).pack(side= 'left')


ventana.mainloop()