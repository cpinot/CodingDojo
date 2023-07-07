from flask import Flask, render_template,redirect,request
from app_usuarios import app
from app_usuarios.modelos.modelo_user import User

@app.route("/")
def index():
    # llamar al método de clase get all para obtener todos los amigos
    users = User.get_all()
    return render_template("leer_todo.html", all_users = users)

@app.route("/formulario/nuevo", methods = ['GET'])
def desplegar():
    return render_template("crear.html")

@app.route( "/nuevo/usuario", methods = ['POST'] )
def agregar_usuario():
    if request.form != None:
        print(request.form['first_name'])
        nuevo_usuario = {

                "first_name" : request.form['first_name'],
                "last_name" : request.form['last_name'],
                "email" :request.form['email']
            }
        User.crear_uno( nuevo_usuario )
        return redirect( "/" )

@app.route("/formulario/editar/<int:id>", methods = ['GET'])
def editar(id):
    
    buscar_usuario = {
        "id" : id
    }
    usuario = User.mostrar_uno(buscar_usuario)
    return render_template("editar_usuario.html", usuario = usuario)

@app.route("/editar/usuario", methods = ['POST'])
def editar_usuario():
    if request.form != None:
        editar_usuario = {
            "id" : request.form['id'],
            "first_name" : request.form['first_name'],
            "last_name" : request.form['last_name'],
            "email" :request.form['email']
        }
        User.editar_uno( editar_usuario )
        return redirect( "/" )
@app.route("/formulario/eliminar/<int:id>", methods = ['GET'])
def eliminar_usuario(id):
    buscar_usuario = {
        "id" : id
    }
    usuario = User.eliminar_uno(buscar_usuario)
    return redirect( "/" )
@app.route("/formulario/detalle/<int:id>", methods = ['GET'])
def detalle_usuario(id):
    buscar_usuario = {
        "id" : id
    }
    usuario = User.mostrar_uno(buscar_usuario)
    return render_template("mostrar_usuario.html", usuario = usuario)