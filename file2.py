import tkinter

ventana = tkinter.Tk()
ventana.geometry("300x200")
ventana.title("holanda")

boton1 = tkinter.Button(ventana)
boton2 = tkinter.Button(ventana)
boton3 = tkinter.Button(ventana)

boton1.grid(row=0,column=0)
boton2.grid(row=1,column=2)
boton3.grid(row=9,column=2)

ventana.mainloop()