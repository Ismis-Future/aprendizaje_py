import tkinter as tk

ventana = tk.Tk() #craer la ventana
lbl_message = tk.Label(ventana, text="hola a todos") #Crear texto
lbl_message.pack() #la ventana se acopla al tamaño de la etiqueta

ventana.mainloop() #desplegar la ventana