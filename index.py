from flask import Flask, render_template, send_from_directory
import os
import subprocess

from x import lista_procesos
from fcfs import procesos, respuestas
#from gantt import mostrar

app = Flask(__name__)

#voy a indicar la ruta raiz
@app.route("/")
def principal():
    return render_template("index.html", procesos=lista_procesos, resultados=procesos, tiempos=respuestas) #buscara la vista y la mostrara

@app.route('/gantt_diagram', methods=['GET', 'POST'])
def gantt_diagram():
    # Aquí puedes ejecutar tu función o archivo de Python
    # Por ejemplo, para ejecutar un archivo:
    os.system('python gantt.py')
    # En este ejemplo, simplemente servimos un archivo de imagen estático como respuesta
    return render_template("gantt.html")





if __name__ == "__main__":
    app.run(debug=True)