import tkinter as tk

# Función para incrementar el contador y mostrarlo en la interfaz
def incrementar_contador():
    global contador, limite
    if contador <= limite:
        label_contador.config(text=f"Contador: {contador}")
        contador += 1
    else:
        button_incrementar.config(state=tk.DISABLED)  # Desactiva el botón cuando el límite es alcanzado

# Función para inicializar el contador y tomar el límite desde el input del usuario
def iniciar_contador():
    global contador, limite
    try:
        limite = int(entry_limite.get())  # Obtén el límite desde el campo de entrada
        contador = 0
        button_incrementar.config(state=tk.NORMAL)  # Activa el botón de incremento
        incrementar_contador()  # Inicia el contador
    except ValueError:
        label_contador.config(text="Por favor, ingrese un número válido.")

# Crear la ventana principal
root = tk.Tk()
root.title("Contador Creciente")

# Variables globales
contador = 0
limite = 0

# Etiquetas, botones y campos de entrada
label_instrucciones = tk.Label(root, text="Introduce el límite del contador:")
label_instrucciones.pack()

entry_limite = tk.Entry(root)
entry_limite.pack()

button_iniciar = tk.Button(root, text="Iniciar", command=iniciar_contador)
button_iniciar.pack()

label_contador = tk.Label(root, text="Contador: 0")
label_contador.pack()

button_incrementar = tk.Button(root, text="Incrementar", state=tk.DISABLED, command=incrementar_contador)
button_incrementar.pack()

# Iniciar el loop de la aplicación
root.mainloop()
