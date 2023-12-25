import tkinter as tk

def mostrar_vector(vector):
    # Limpiar la Listbox
    listbox_datos.delete(0, tk.END)

    # Mostrar cada elemento en la Listbox
    for dato in vector:
        listbox_datos.insert(tk.END, dato)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mostrar Vectores")
ventana.geometry("500x500")
# Crear una Listbox para mostrar los datos
listbox_datos = tk.Listbox(ventana, width=20, height=5)
listbox_datos.pack(pady=10)

# Ejemplo de vectores
vector1 = [1, 2, 3, 4, 5]
vector2 = [10, 20, 30, 40, 50]

# Crear un botón para mostrar el primer vector
boton_mostrar1 = tk.Button(ventana, text="Mostrar Vector 1", command=lambda: mostrar_vector(vector1))
boton_mostrar1.pack(pady=5)

# Crear un botón para mostrar el segundo vector
boton_mostrar2 = tk.Button(ventana, text="Mostrar Vector 2", command=lambda: mostrar_vector(vector2))
boton_mostrar2.pack(pady=5)

# Iniciar el bucle principal
ventana.mainloop()
