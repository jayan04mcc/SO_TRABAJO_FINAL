from flask import Flask, render_template, send_from_directory
import os
import subprocess

from x import obtener_procesos
from fcfs import initProcess, fcfs
from gantt import mostrarGrafico

app = Flask(__name__)

#variables globales para el FCFS
inicio=[]
duracion=[]
p=[]


#voy a indicar la ruta raiz
@app.route("/")
def principal():
    #lista_procesos=obtener_procesos()
    
    lista_procesos=[
        ("p1","Word",0,10),
        ("p2","Excel",0,1),
        ("p3","VSCode",0,2),
        ("p4","Python",0,1),
        ("p5","Google",0,5),
    ]
    
    procesos=initProcess(lista_procesos)
    global p #para el grafico
    p=procesos#para el grafico
    rpta=fcfs(procesos)
    respuestas= rpta[0]
    global inicio, duracion
    inicio = rpta[1]
    duracion=rpta[2]
    return render_template("index.html", procesos=lista_procesos, resultados=procesos, tiempos=respuestas) #buscara la vista y la mostrara

@app.route('/mostrar_gantt')
def mostrar_gantt():
    print("inicio: " , inicio)
    # Aquí puedes ejecutar tu función o archivo de Python
    # Por ejemplo, para ejecutar un archivo:
    #os.system('python gantt.py')
    # En este ejemplo, simplemente servimos un archivo de imagen estático como respuesta
    #return render_template('index.html')  # O redirige a otra página si lo prefieres
    mostrarGrafico(p, inicio, duracion)
    return "OK"


if __name__ == "__main__":
    app.run(debug=True)