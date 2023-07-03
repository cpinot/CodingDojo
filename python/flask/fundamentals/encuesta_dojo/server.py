from flask import Flask, render_template, request, redirect, session
from datetime import datetime
import random

app = Flask(__name__)  
app.secret_key = 'JSaafE54!@#$%$#%^&*()_+'

@app.route('/')      
def index():
        print("ingreso a la pagina")
        return render_template("index.html")

@app.route('/resultado', methods=['POST'])
def resultado():
        print("recibiendo info del formulario")
        print(request.form)
        nombre = session['Nombre'] = request.form['nombre']
        print(nombre)
        ubicacion = session['Ubicacion'] = request.form['dojo']
        print(ubicacion)
        lenguaje =session['Lenguaje'] = request.form['favorito']
        print(lenguaje)
        comentarios =session['Comentarios'] = request.form['comentarios']
        print(comentarios)

        return render_template("resultado.html", nombre=nombre, ubicacion=ubicacion, lenguaje=lenguaje, comentarios=comentarios)
@app.route('/clear', methods=['POST'])
def clear():
        session.clear()
        return redirect('/')
if __name__=="__main__":   
    app.run(debug=True)