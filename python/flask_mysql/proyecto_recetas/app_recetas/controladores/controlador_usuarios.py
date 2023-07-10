from flask import render_template, request,session,redirect,flash,get_flashed_messages
from app_recetas import app
from app_recetas.modelos.modelo_usuario import Usuario
from flask_bcrypt import Bcrypt

@app.route('/', methods=['GET'])
def desplegar_index():
    return render_template('login.html')

@app.route('/login', methods=['GET'])
def desplegar_login_registro():
    if 'usuario_id' in session:
        session['usuario_id'] = None
    return render_template('login.html')

@app.route('/login/usuario', methods=['POST'])
def login_usuario():
    if 'usuario_id' in session:
        session['usuario_id'] = None

    print("Llegó la información del formulario")
    data = {
        "email": request.form['email'],
        "password": request.form['password']
    }
    usuario_existe = Usuario.obtener_uno_con_email(data)
    validar_usuario= Usuario.validar_login(data, usuario_existe)
    print(validar_usuario)
    if validar_usuario == True:
            print("el usuario existe")
            session['usuario_id'] = usuario_existe.id
            session['usuario_nombre'] = usuario_existe.nombre
            session['usuario_apellido'] = usuario_existe.apellido
            return redirect('/recetas' )
    else:
            print("el usuario no existe")
            return redirect('/login')
@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect('/login')


@app.route('/register', methods=['GET'])
def desplegar_registro_usuario():
    return render_template('register.html')

@app.route('/crear/usuario', methods=['POST'])
def nuevo_usuario():
    if 'usuario_id' in session:
        session['usuario_id'] = None

    print("Llegó la información del formulario")
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": request.form['password'],
        "validar_password": request.form['validar_password']
    }
    usuario_existe = Usuario.obtener_uno_con_email(data)
    validar_usuario= Usuario.validar_registro(data, usuario_existe)
    print(validar_usuario)
    if validar_usuario == True:
            data['password'] = Bcrypt().generate_password_hash(data['password'])
            Nuevo_usuario= Usuario.crear_un_usuario(data)
            print(Nuevo_usuario)
            session['usuario_id'] = Nuevo_usuario
            return redirect('/login' )
    else:
            return redirect('/register')

