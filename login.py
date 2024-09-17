from tkinter import *


#wb = Workbook()
#ws = wb.active
#ws.append(["Nombre", "Edad","Email", "Teléfono", "Dirección"])
#wb.save('datos.xlsx')

ventana_login = Tk()
ventana_login.title("Formulario de entrada de Datos")
ventana_login.config(bg='#4B6587')
ventana_login.geometry("400x400")

frame = Frame()

label_style = {"bg": "#4B6587", "fg": "white"}
entry_style = {"bg": "#D3D3D3", "fg": "black"} 

label_nombre = Label(ventana_login,text="Nombre", **label_style)
label_nombre.grid(row=0,column=0,padx=10,pady=5)
entry_nombre = Entry(ventana_login,**entry_style)
entry_nombre.grid(row=0,column=1,padx=10,pady=5)

label_edad = Label(ventana_login,text="Edad", **label_style)
label_edad.grid(row=1,column=0,padx=10,pady=5)
entry_edad = Entry(ventana_login,**entry_style)
entry_edad.grid(row=1,column=1,padx=10,pady=5)

label_email = Label(ventana_login,text="Email", **label_style)
label_email.grid(row=2,column=0,padx=10,pady=5)
entry_email = Entry(ventana_login,**entry_style)
entry_email.grid(row=2,column=1,padx=10,pady=5)

label_telefono = Label(ventana_login,text="Teléfono", **label_style)
label_telefono.grid(row=3,column=0,padx=10,pady=5)
entry_telefono = Entry(ventana_login,**entry_style)
entry_telefono.grid(row=3,column=1,padx=10,pady=5)

label_direccion = Label(ventana_login,text="Dirección", **label_style)

label_direccion.grid(row=4,column=0,padx=10,pady=5)
entry_direccion = Entry(ventana_login,**entry_style)
entry_direccion.grid(row=4,column=1,padx=10,pady=5)

boton_guardar = Button(ventana_login, text="Guardar",bg="#6D8299",fg="white")
boton_guardar.grid(row=5,column=0,columnspan=1,padx=10,pady=5)

boton_modificar = Button(ventana_login, text="Modificar",bg="#6D8299",fg="white")
boton_modificar.grid(row=5,column=1,columnspan=1,padx=10,pady=5)

boton_borrar = Button(ventana_login, text="Borrar",bg="#6D8299",fg="white")
boton_borrar.grid(row=5,column=2,columnspan=1,padx=10,pady=5)

ventana_login.mainloop()