import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Treeview con Tamaño Específico")
root.geometry("800x300")
# Crear un Treeview widget
treeview = ttk.Treeview(root, height=5)  # Define la altura inicial (en número de filas)

# Definir las columnas
treeview['columns'] = ("Columna 1", "Columna 2")
treeview.column("#0", width=50, minwidth=50)  # Columna del ítem (generalmente para el título del nodo)
treeview.column("Columna 1", width=20, minwidth=5)
treeview.column("Columna 2", width=20, minwidth=5)

# Agregar datos al Treeview como ejemplo
treeview.insert('', 'end', text="Item 1", values=("Valor 1A", "Valor 1B"))
treeview.insert('', 'end', text="Item 2", values=("Valor 2A", "Valor 2B"))
treeview.insert('', 'end', text="Item 2", values=("Valor 2A", "Valor 2B"))
treeview.insert('', 'end', text="Item 2", values=("Valor 2A", "Valor 2B"))
treeview.insert('', 'end', text="Item 2", values=("Valor 2A", "Valor 2B"))
treeview.insert('', 'end', text="Item 2", values=("Valor 2A", "Valor 2B"))
treeview.insert('', 'end', text="Item 2", values=("Valor 2A", "Valor 2B"))
treeview.insert('', 'end', text="Item 2", values=("Valor 2A", "Valor 2B"))
treeview.insert('', 'end', text="Item 2", values=("Valor 2A", "Valor 2B"))
treeview.insert('', 'end', text="Item 2", values=("Valor 2A", "Valor 2B"))
treeview.insert('', 'end', text="Item 2", values=("Valor 2A", "Valor 2B"))
treeview.insert('', 'end', text="Item 2", values=("Valor 2A", "Valor 2B"))
treeview.insert('', 'end', text="Item 2", values=("Valor 2A", "Valor jajajajjaja"))
treeview.insert('', 'end', text="Item 2", values=("Valor 2A", "Valor jajajajjaja"))
treeview.insert('', 'end', text="Item 2", values=("Valor 2A", "Valor jajajajjaja"))
treeview.insert('', 'end', text="Item 2", values=("Valor 2A", "Valor jajajajjaja"))
treeview.insert('', 'end', text="Item 2", values=("Valor 2A", "Valor jajaja"))
treeview.insert('', 'end', text="Item 2", values=("Valor 2A", "Valor jajajajjaja"))
treeview.insert('', 'end', text="Item 2", values=("Valor 2A", "Valor jajajajjaja"))
treeview.insert('', 'end', text="Item 2", values=("Valor 2A", "Valor jajajajjaja"))
# Colocar el Treeview en la ventana
treeview.pack(fill='both', expand=True)  # Ajustar al tamaño de la ventana
# Crear el primer Listbox con un tamaño específico
listbox1 = tk.Listbox(root, width=20, height=10)  # 20 caracteres de ancho, 10 líneas de alto
listbox1.insert(1, "Opción 1 en Listbox 1")
listbox1.insert(2, "Opción 2 en Listbox 1")
listbox1.pack(side="left")

# Crear el segundo Listbox con un tamaño diferente
listbox2 = tk.Listbox(root, width=30, height=5)  # 30 caracteres de ancho, 5 líneas de alto
listbox2.insert(1, "Opción 1 en Listbox 2")
listbox2.insert(2, "Opción 2 en Listbox 2")
listbox2.pack(side="left")
# Ejecutar el bucle principal
root.mainloop()

 