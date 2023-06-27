from flask import Flask, render_template

app = Flask(__name__,template_folder='.') 

@app.route('/')          
def tablero_ajedrez():
    return render_template("templates/index.html", num=8, num2=8, color1="black", color2="whitesmoke")

@app.route('/<int:num>')
def tablero_ajedrez2(num):
    return render_template("templates/index.html", num=num, num2=num, color1="black", color2="red")

@app.route('/<int:num>/<int:num2>')
def tablero_ajedrez3(num,num2):
    return render_template("templates/index.html", num=num, num2=num2, color1="brow", color2="yellow")

@app.route('/<int:num>/<int:num2>/<color1>/<color2>')
def tablero_ajedrez4(num,num2, color1, color2):
    return render_template("templates/index.html", num=num,num2=num2, color1=color1, color2=color2)

@app.errorhandler(404)
def page_not_found(e):
    return "Lo Siento! No hay respuesta. intente otra vez."


if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración