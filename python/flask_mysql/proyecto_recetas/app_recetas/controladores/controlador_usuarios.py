from flask import render_template, request,session
from app_recetas import app
from app_recetas.modelos.modelo_usuario import Usuario


@app.route('/', methods=['GET'])
def desplegar_login_registro():
    return render_template('index.html')

@app.route('/crear/usuario', methods=['POST'])
def nuevo_usuario():
    print("Llegó la información del formulario")
    print(request.form)
    data = {
        **request.form
    }
    usuario_existe = Usuario.obtener_uno_con_email(data)
    if Usuario.validar_registro(data, usuario_existe):
        return
        flash("Usuario registrado correctamente")
        return redirect('/')
    return render_template('index.html')
