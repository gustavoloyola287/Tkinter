from tkinter import *

ventana_raiz = Tk()
ventana_raiz.title("Contador Creciente")
ventana_raiz.geometry('400x300')
ventana_raiz.resizable(0,0)
   
limite = 20
def contador_creciente(limite):
    contador = 0
    while contador <= limite:
        print(f"Contador: {contador}")
        contador += 1

contador_creciente(limite)

ventana_raiz.mainloop()