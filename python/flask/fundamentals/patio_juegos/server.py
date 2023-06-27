from flask import Flask, render_template

app = Flask(__name__,template_folder='.')    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return 'Hola Mundo!'  # Devuelve la cadena '¡Hola Mundo!' como respuesta
@app.route('/play')
def play():
    return render_template("index.html", num=3, color="cyan")

@app.route('/play/<int:num>')
def play_changes_num(num):
    return render_template("index.html", num=num, color="blue")

@app.route('/play/<int:num>/<string:color>')
def play_changes_num_color(num,color):
    return render_template("index.html", num=num, color=color)

@app.errorhandler(404)
def page_not_found(e):
    return "Lo Siento! No hay respuesta. intente otra vez."


if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración

# sentencias import, tal vez algunas otras rutas