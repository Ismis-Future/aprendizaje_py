import tkinter as tk
from tkinter.constants import W
from typing import Text


ventana = tk.Tk()
lblMensaje = tk.Label(ventana)
lblMensaje.pack()
seleccion = tk.IntVar()

def Mostrar():
    if seleccion.get()==1:
        mensaje = "has seleccionado Python"
    if seleccion.get()==2:
        mensaje = "has seleccionado c#"
    if seleccion.get()==3:
        mensaje = "has seleccionado c++"
    lblMensaje.config(text=mensaje)



rbnPython = tk.Radiobutton(ventana, text="Python", variable=seleccion, value=1,command=Mostrar()).pack(anchor=tk.W)

rbnCsharp = tk.Radiobutton(ventana, text="c#", variable=seleccion, value=2,command=Mostrar()).pack(anchor=tk.W)

rbnCpluplus = tk.Radiobutton(ventana, text="c++", variable=seleccion, value=3,command=Mostrar()).pack(anchor=tk.W)



ventana.mainloop()
        