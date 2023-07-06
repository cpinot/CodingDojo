from app_recetas.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
import re
class Usuario:
    def __init__(self,data):
        self.id=data['id']
        self.nombre=data['nombre']
        self.apellido=data['apellido']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    @classmethod
    def obtener_uno_con_email(cls,data):
        query=  """SELECT * 
                FROM usuarios
                WHERE email=%(email)s;
                """
        resultado=connectToMySQL('recetas').query_db(query,data)
        if len(resultado)==0:
            return None
    @staticmethod
    def validar_registro( data , usuario_existe ):
        is_valid = True
        if len( data['nombre'] ) < 2:
            flash("El nombre debe tener al menos 2 caracteres")
            is_valid = False
        if len( data['apellido'] ) < 2:
            flash("El apellido debe tener al menos 2 caracteres")
            is_valid = False
        if len( data['email'] ) < 2:
            flash("El email debe tener al menos 2 caracteres")
            is_valid = False
        if len( data['password'] ) < 8:
            flash("La contraseña debe tener al menos 8 caracteres")
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash("Las contraseñas no coinciden")
            is_valid = False
        if usuario_existe != None:
            flash("El email ya está registrado")
            is_valid = False
        return is_valid