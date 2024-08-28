import tkinter as tk
ventana = tk.Tk()
ventana.title("Contador Creciente")
ventana.geometry('600x600')
# Programa de contador creciente

def contador_creciente(limite):
    contador = 0
    while contador <= limite:
        print(f"Contador: {contador}")
        contador += 1

# Llamada a la función con un límite definido
#
#limite = int(input("Introduce el valor límite del contador: "))
limite = 20
contador_creciente(limite)
ventana.mainloop()