import tkinter as tk
from tkinter import font
from tkinter.constants import CENTER

ventana = tk.Tk() #craer la ventana
mensaje = """
Hola a todos yo soy ismael y estoy 
aprendiendo tkinter
"""

#con justify podemos justificar el texto
#se puede usar LEFT, RIGHT, CENTER
#fg se usa para definir un color
#font se usa para definir una fuente y su tamaño or ejemplo: font= Sans serif 10 bold
#bg es para indicar el fondo del texto
label_message = tk.Label(ventana, text= mensaje, justify=CENTER, fg='blue', font= 'Helvetica 10 bold' ).pack()

ventana.mainloop() #desplegar la ventana