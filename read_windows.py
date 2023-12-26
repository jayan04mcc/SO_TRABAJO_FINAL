import tkinter as tk
# Abre el archivo en modo lectura
with open('tu_archivo.txt', 'r') as archivo_entrada:
    # Lee todas las líneas del archivo
    lineas = archivo_entrada.readlines()

# Elimina los espacios en blanco al inicio de cada línea y sobrescribe el archivo original
with open('tu_archivo.txt', 'w') as archivo_salida:
    for linea in lineas:
        linea_sin_espacios = linea.lstrip()  # Elimina espacios en blanco al inicio
        archivo_salida.write(linea_sin_espacios)

tercera_columna = []
lista_total=[]
# Lee el contenido del archivo modificado
with open('tu_archivo.txt', 'r') as archivo_modificado:
    for linea in archivo_modificado:
        if not linea.strip():
            continue  # Ignorar líneas vacías
        
        palabras = linea.split()  # Ajustar según el delimitador correcto
        if len(palabras) >= 3:
            tercera_columna.append(palabras[2].strip())
        lista_total.append(palabras)

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
listbox_datos = tk.Listbox(ventana, width=40, height=10)
listbox_datos.pack(pady=10)


# Crear un botón para mostrar el primer vector
boton_mostrar1 = tk.Button(ventana, text="Mostrar Vector 1", command=lambda: mostrar_vector(tercera_columna))
boton_mostrar1.pack(pady=5)

# Crear un botón para mostrar el segundo vector
boton_mostrar2 = tk.Button(ventana, text="Mostrar Vector 2", command=lambda: mostrar_vector(lista_total))
boton_mostrar2.pack(pady=5)

boton_RoundRobin = tk.Button(ventana,text ="ALGORITMO ROUND ROBIN")
boton_RoundRobin.pack(side="right", anchor="se", padx=5, pady=5)
boton_FCFS = tk.Button(ventana,text="ALGORITMO FCFS")
boton_FCFS.pack(side="right", anchor="se", padx=5, pady=5)
boton_SJF = tk.Button(ventana,text="ALGORITMO SJF")
boton_SJF.pack(side="right", anchor="se", padx=5, pady=5)
# Iniciar el bucle principal
ventana.mainloop()

with open('tu_archivo.txt', 'r') as archivo_entrada:
    # Lee todas las líneas del archivo
    lineas = archivo_entrada.readlines()

# Elimina los espacios en blanco al inicio de cada línea y sobrescribe el archivo original
with open('tu_archivo.txt', 'w') as archivo_salida:
    for linea in lineas:
        linea_sin_espacios = linea.lstrip()  # Elimina espacios en blanco al inicio
        archivo_salida.write(linea_sin_espacios)

tercera_columna = []
lista_total=[]
# Lee el contenido del archivo modificado
with open('tu_archivo.txt', 'r') as archivo_modificado:
    for linea in archivo_modificado:
        if not linea.strip():
            continue  # Ignorar líneas vacías
        
        palabras = linea.split()  # Ajustar según el delimitador correcto
        if len(palabras) >= 3:
            tercera_columna.append(palabras[2].strip())
        lista_total.append(palabras)

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
listbox_datos = tk.Listbox(ventana, width=40, height=10)
listbox_datos.pack(pady=10)


# Crear un botón para mostrar el primer vector
boton_mostrar1 = tk.Button(ventana, text="Mostrar Vector 1", command=lambda: mostrar_vector(tercera_columna))
boton_mostrar1.pack(pady=5)

# Crear un botón para mostrar el segundo vector
boton_mostrar2 = tk.Button(ventana, text="Mostrar Vector 2", command=lambda: mostrar_vector(lista_total))
boton_mostrar2.pack(pady=5)

boton_RoundRobin = tk.Button(ventana,text ="ALGORITMO ROUND ROBIN")
boton_RoundRobin.pack(side="right", anchor="se", padx=5, pady=5)
boton_FCFS = tk.Button(ventana,text="ALGORITMO FCFS")
boton_FCFS.pack(side="right", anchor="se", padx=5, pady=5)
boton_SJF = tk.Button(ventana,text="ALGORITMO SJF")
boton_SJF.pack(side="right", anchor="se", padx=5, pady=5)
# Iniciar el bucle principal
ventana.mainloop()
