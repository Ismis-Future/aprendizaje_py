from tkinter import *
import tkinter as tk

root = tk.Tk()

miTexto = 'Hola a todos, me da gusto que esteoy aprendiendo tkinter'

#mgsMessage = tk.Message(root, text=miTexto).pack()

#con with se cambia el tamaño del texto
mgsMessage2 = tk.Message(root, text=miTexto, width=380).pack()

root.mainloop()