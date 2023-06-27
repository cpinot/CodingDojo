from flask import Flask  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return 'Hola Mundo!'  # Devuelve la cadena '¡Hola Mundo!' como respuesta

@app.route('/dojo')
def success():
    return "Dojo!"
    
# app.run(debug=True) debería ser la última sentencia 
@app.route('/say/<name>')
def hello(name):
    print(name)
    return "Hello " + name.capitalize()

@app.route('/repeat/<int:num>/<string:word>')
def repeat_nombre(num, word):
    imprime = ""
    for i in range(num):
        imprime += "Hola " + word.capitalize() + "<br>"
    return imprime

@app.errorhandler(404)
def page_not_found(e):
    return "Lo Siento! No hay respuesta. intente otra vez."


if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración

# sentencias import, tal vez algunas otras rutas
    