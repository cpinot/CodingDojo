from flask import render_template,redirect,request,session,flash
from app_dojos_y_ninjas import app
from app_dojos_y_ninjas.modelos.modelo_dojos import Dojo
from app_dojos_y_ninjas.modelos.modelo_ninjas import Ninja

@app.route('/formulario/ninja', methods = ['GET'])
def desplegar_formulario_ninja():
    lista_dojos = Dojo.obtener_todos()
    return render_template('formulario_ninja.html', lista_dojos = lista_dojos)

@app.route('/nuevo/ninja', methods = ['POST'])
def crear_ninja():
    print(request.form)
    nuevo_ninja = {
        'first_name': request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age':request.form['age'],
        'dojo_id':request.form['dojo']
    }
    Ninja.crear_uno(nuevo_ninja)
    return redirect('/dojos')