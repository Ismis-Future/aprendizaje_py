import tkinter as tk
class Test():
    def __init__(self):
            
        self.ventana = tk.Tk()
        #Para poder cambiar el texto deuna variible de usa StringVar ppara poder cambiar el texto de un widget
        self.texto =tk.StringVar()
        #Le damos un valor inicial con la funcion set
        self.texto.set('Hola a todos')

        #creaos una etiqueta
        #con textvariable indicamos cual es la variable que tendra el texto del boton
        lblEtiqueta= tk.Label(self.ventana, textvariable=self.texto, font='arial 24')

        #crear boton

        btnMiBoton = tk.Button(self.ventana, text="Haz mensaje", font='arial 24', command=self.changeText).pack()


        self.ventana.mainloop()

        def changeText(self):
            self.texto.set("nuevo mensaje")
app = Test()
