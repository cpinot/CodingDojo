# importar la función que devolverá una instancia de una conexión
from app_usuarios.config.mysqlconnection import connectToMySQL

# modelar la clase después de la tabla friend de nuestra base de datos
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
# ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
    # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('user').query_db(query)
    # crear una lista vacía para agregar nuestras instancias de friends
        users = []
    # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for user in results:
            users.append( cls(user) )
        return users
            
    @classmethod
    def crear_uno(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
        # data es un diccionario que se pasará a la función save (se refiere a la variable data en la función save)
        return connectToMySQL('user').query_db( query, data )
    @classmethod
    def editar_uno(cls, data ):
        query = "UPDATE users SET first_name = %(first_name)s , last_name = %(last_name)s , email = %(email)s , updated_at = NOW() WHERE id = %(id)s;"
        # data es un diccionario que se pasará a la función save (se refiere a la variable data en la función save)
        return connectToMySQL('user').query_db( query, data )
    @classmethod
    def eliminar_uno(cls, data ):
        query = "DELETE FROM users WHERE id = %(id)s;"
        # data es un diccionario que se pasará a la función save (se refiere a la variable data en la función save)
        return connectToMySQL('user').query_db( query, data )
    @classmethod
    def mostrar_uno(cls, data ):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        # data es un diccionario que se pasará a la función save (se refiere a la variable data en la función save)
        results = connectToMySQL('user').query_db( query, data )
        return cls( results[0] )
    
