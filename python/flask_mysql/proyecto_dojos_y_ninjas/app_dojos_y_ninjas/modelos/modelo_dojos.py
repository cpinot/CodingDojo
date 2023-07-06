from app_dojos_y_ninjas.config.mysqlconnection import connectToMySQL 
from app_dojos_y_ninjas import BASE_DATOS
from app_dojos_y_ninjas.modelos.modelo_ninjas import Ninja
class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    @classmethod
    def crear_uno(cls, data):
        query="""INSERT INTO dojos (name)
                VALUES (%(name)s);"""
        resultado = connectToMySQL(BASE_DATOS).query_db(query, data)
        return resultado
    
    @classmethod
    def obtener_todos(cls):
        query=  """SELECT *
                FROM dojos;"""
        resultado = connectToMySQL(BASE_DATOS).query_db(query)
        lista_de_dojos = []
        for renglon in resultado:
            lista_de_dojos.append(Dojo(renglon))
        return lista_de_dojos
    @classmethod
    def obtener_uno_con_ninjas(cls, data):
        query=  """SELECT *
                FROM dojos 
                LEFT JOIN ninjas  ON dojos.id = ninjas.dojo_id
                WHERE dojos.id = %(id)s;"""
        
        resultado = connectToMySQL(BASE_DATOS).query_db(query, data)
        informacion_dojo = Dojo(resultado[0])

        for renglon in resultado:
            if renglon['ninjas.id'] != None:
                datos_ninja = {
                    'id': renglon['ninjas.id'],
                    'first_name': renglon['first_name'],
                    'last_name': renglon['last_name'],
                    'age': renglon['age'],
                    'dojo_id': renglon['dojo_id'],
                    'created_at': renglon['ninjas.created_at'],
                    'updated_at': renglon['ninjas.updated_at'],
                }
                print(datos_ninja)
                ninja_actual = Ninja(datos_ninja)
                informacion_dojo.ninjas.append(ninja_actual)
        return informacion_dojo
