from flask import Flask  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return 'Hola Cynthia!'  # Devuelve la cadena '¡Hola Mundo!' como respuesta

@app.route('/dojo')
def success():
    return "Dojo!"
    
# app.run(debug=True) debería ser la última sentencia 
@app.route('/say/<name>')
def hello(name):
    print(name)
    return "Hi " + name

@app.route('/users/<username>/<id>') # para una ruta '/users/____/____', dos parámetros en la url se pasan como nombre de usuario e id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración

# sentencias import, tal vez algunas otras rutas
    


