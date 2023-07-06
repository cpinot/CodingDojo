from flask import Flask, render_template,redirect,request
# importar la clase de user.py
from user import User
app = Flask(__name__)

@app.route("/")
def index():
    # llamar al método de clase get all para obtener todos los amigos
    users = User.get_all()
    return render_template("leer_todo.html", all_users = users)

@app.route("/formulario/nuevo", methods = ['GET'])
def desplegar():
    return render_template("crear.html")

@app.route( "/nuevo/usuario", methods = ['GET, POST'] )
def agregar_usuario():
    if request.form != None:
        print(request.form("nombre"))
    nuevo_usuario = {

            "first_name" : request.form("nombre"),
            "last_name" : request.form("apellido"),
            "email" :request.form("email")
        }
    User.crear_uno( nuevo_usuario )
    return redirect( "/" )
    
if __name__ == "__main__":
    app.run(debug=True)

