from tkinter import *

ventana_raiz = Tk()

ventana_raiz.title("Ventana de Prueba")

ventana_raiz.resizable(1,1)

ventana_raiz.geometry("650x250")

ventana_raiz.config(bg="light blue")

miframe = Frame()

miframe.pack()#fill="both", expand="1"

miframe.config(bg="green")

miframe.config(width="200",height="150")

miframe.config(bd=20)

miframe.config(relief = "raised")

miframe.config(cursor = "hand2")

ventana_raiz.mainloop()