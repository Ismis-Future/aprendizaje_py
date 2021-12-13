#como insertar una imagen

import tkinter as tk

ventana = tk.Tk()
ventana.title('Holas')


image_tk = tk.PhotoImage(file='Tkinter/logo_CV.png') #con PhotoImage podemos insertar una imagen, con file indicamos la direccion o la imagen que querramos poner


ventana.mainloop()