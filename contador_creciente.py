from tkinter import *

ventana_raiz = Tk()
ventana_raiz.title("Contador Creciente")
ventana_raiz.geometry('400x300')
ventana_raiz.resizable(0,0)

frame = Frame()
#frame.pack(side="left",anchor="n")
frame.pack()
frame.pack(fill="both", expand="true")
frame.config(bg="orange")
frame.config(width="400",height="300")
frame.config(bd=30)
frame.config(relief="flat")
   
limite = 20
def contador_creciente(limite):
    contador = 0 
    while contador <= limite:
        print(f"Contador: {contador}")
        contador += 1

contador_creciente(limite)

ventana_raiz.mainloop()