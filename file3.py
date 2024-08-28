import tkinter

ventana = tkinter.Tk()
ventana.geometry("200x300")
etiqueta = tkinter.Label(ventana, text = "Hola Mundo", background="green")

#muestra la etiqueta al medio y arriba
#etiqueta.pack()

#muestra la etiqueta a la derecha right. izq abajo
#etiqueta.pack(side = tkinter.RIGHT)


etiqueta.pack(fill  = tkinter.Y, expand = True)

boton1 = 


ventana.mainloop()
