from app_recetas.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
class Usuario:
    def __init__(self,data):
        self.id=data['id']
        self.nombre=data['first_name']
        self.apellido=data['last_name']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def obtener_uno_con_email(cls,data):
        query=  """SELECT * 
                FROM users
                WHERE email=%(email)s;
                """
        resultado=connectToMySQL('recetas').query_db(query,data)
        print('Esto envia el query ',resultado)
        if len(resultado)<1:
            print('No hay resultados')
            return None
        else:
            print('Hay resultados')
            return cls(resultado[0])
    @classmethod
    def crear_un_usuario(cls,data):
        query=  """INSERT INTO users (first_name,last_name,email,password)
                VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);
                """
        return connectToMySQL('recetas').query_db(query,data)

    @staticmethod
    def validar_registro( data , usuario_existe ):
        is_valid = True
        if len( data['first_name'] ) < 2:
            flash("El nombre debe tener al menos 2 caracteres")
            is_valid = False
        if len( data['last_name'] ) < 2:
            flash("El apellido debe tener al menos 2 caracteres")
            is_valid = False
        if len( data['email'] ) < 2:
            flash("El email debe tener al menos 2 caracteres")
            is_valid = False
        if len( data['password'] ) < 8:
            flash("La contraseña debe tener al menos 8 caracteres")
            is_valid = False
        if data['password'] != data['validar_password']:
            flash("Las contraseñas no coinciden")
            is_valid = False
        if usuario_existe != None:
            flash("El email ya está registrado")
            is_valid = False
        return is_valid
    @staticmethod
    def validar_login( data , usuario_existe ):
        is_valid = True
        if len( data['email'] ) < 2:
            flash("El email debe tener al menos 2 caracteres")
            is_valid = False
        if len( data['password'] ) < 8:
            flash("La contraseña debe tener al menos 8 caracteres")
            is_valid = False
        if usuario_existe == None:
            flash("El email no está registrado")
            is_valid = False
        else:
                pw_hash = Bcrypt().generate_password_hash(data['password'])
                chequear_pass=Bcrypt().check_password_hash(usuario_existe.password, pw_hash)
                print('valor de formulario',chequear_pass)
                print('valor de base de datos',usuario_existe.password)
                if not Bcrypt().check_password_hash(usuario_existe.password, data['password']):
                    flash("Contraseña incorrecta")
                    is_valid = False
                return is_valid

