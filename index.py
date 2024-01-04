from flask import Flask, render_template
from x import lista_procesos

app = Flask(__name__)

#voy a indicar la ruta raiz
@app.route("/")
def principal():
    return render_template("index.html", procesos=lista_procesos) #buscara la vista y la mostrara

#definiendo otra ruta
@app.route("/contacto")
def contacto():
    return "Esta es la pagina de contacto"

if __name__ == "__main__":
    app.run(debug=True)