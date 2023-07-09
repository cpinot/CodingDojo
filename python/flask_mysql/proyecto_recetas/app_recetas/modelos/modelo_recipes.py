from app_recetas.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
class Recipes:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.description=data['description']
        self.instructions=data['instructions']
        self.under_30_minutes=data['self.under_30_minutes']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.user_id=data['user_id']
    @classmethod
    def obtener_todas_las_recetas_con_usuarios(cls):
        query=  """SELECT recipes.id, recipes.name, recipes.description, recipes.under_30_minutes, users.first_name, user_id 
                FROM recipes
                JOIN users ON users.id=recipes.user_id;
                """
        resultado=connectToMySQL('recetas').query_db(query)
        print('Esto envia el query ',resultado)
        if len(resultado)<1:
            print('No hay resultados')
            return None
        else:
            print('Hay resultados')
            return resultado
        
    @classmethod
    def crear_una_receta(cls,data):
        query=  """INSERT INTO recipes (name,description,instructions,under_30_minutes,created_at, user_id)
                VALUES (%(name)s,%(description)s,%(instructions)s,%(under_30_minutes)s,%(created_at)s,%(user_id)s);
                """
        return connectToMySQL('recetas').query_db(query,data)
    @classmethod
    def obtener_todas_las_recetas(cls):
        query=  """SELECT * 
                FROM recipes;
                """
        resultado=connectToMySQL('recetas').query_db(query)
        print('Esto envia el query ',resultado)
        return resultado
    @staticmethod
    def validar_receta( data ):
        is_valid = True
        if len( data['name'] ) < 3:
            flash("El nombre debe tener al menos 3 caracteres")
            is_valid = False
        if len( data['description'] ) < 3:
            flash("La descripción debe tener al menos 3 caracteres")
            is_valid = False
        if len( data['instructions'] ) < 3:
            flash("Las instrucciones deben tener al menos 3 caracteres")
            is_valid = False
        return is_valid
    @classmethod
    def obtener_una_receta(cls,data):
        query=  """SELECT recipes.id, recipes.name, recipes.description, recipes.under_30_minutes, recipes.instructions, recipes.created_at, users.first_name, user_id 
                FROM recipes
                JOIN users ON users.id=recipes.user_id
                where recipes.id=%(id)s;
                """
        resultado=connectToMySQL('recetas').query_db(query,data)
        print('Esto envia el query ',resultado)
        return resultado
    @classmethod
    def editar_una_receta(cls,data):
        query=  """UPDATE recipes SET name=%(name)s,description=%(description)s,instructions=%(instructions)s,under_30_minutes=%(under_30_minutes)s,created_at=%(created_at)s
                WHERE id=%(id)s;
                """
        return connectToMySQL('recetas').query_db(query,data)
    @classmethod
    def eliminar_una_receta(cls,data):
        query=  """DELETE FROM recipes
                WHERE id=%(id)s;
                """
        return connectToMySQL('recetas').query_db(query,data)