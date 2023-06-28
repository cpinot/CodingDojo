from flask import Flask, render_template

app = Flask(__name__,template_folder='.') 



@app.route('/')          
def lista():
    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
    return render_template("templates/index.html", users=users)

@app.errorhandler(404)
def page_not_found(e):
    return "Lo Siento! No hay respuesta. intente otra vez."


if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración