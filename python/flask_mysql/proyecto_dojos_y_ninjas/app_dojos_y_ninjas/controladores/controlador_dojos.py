from flask import render_template,redirect,request,session,flash
from app_dojos_y_ninjas import app
from app_dojos_y_ninjas.modelos.modelo_dojos import Dojo
from app_dojos_y_ninjas.modelos.modelo_ninjas import Ninja

@app.route('/dojos', methods = ['GET'])
def obtener_dojos():
    lista_dojos = Dojo.obtener_todos()
    return render_template('dojos.html', lista_dojos = lista_dojos)

@app.route('/nuevo/dojo', methods = ['POST'])
def crear_dojo():
    print(request.form)
    nuevo_dojo ={
        'name': request.form['nombre'],
    }
    Dojo.crear_uno(nuevo_dojo)
    return redirect('/dojos')

@app.route('/dojo/<int:id>', methods = ['GET'])
def obtener_dojo(id):
    data = {
        'id': id
    }
    informacion_dojo = Dojo.obtener_uno_con_ninjas(data)
    return render_template('dojo.html', informacion_dojo = informacion_dojo)
