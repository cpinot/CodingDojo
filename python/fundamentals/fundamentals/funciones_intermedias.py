#1. Actualizar valores en diccionarios y listas
x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
x[1][0]=15
print(x)

#Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
estudiantes[0]['last_name']='Bryant'
print(estudiantes[0])

#En el directorio de deportes, cambia 'Messi' a 'Andres'
directorio_deportes['fútbol'][0]='Andres'
print(directorio_deportes['fútbol'])

#Cambia el valor 20 en z a 30
z[0]['y']=30
print(z)

#2. Itera a través de una lista de diccionarios
#Crea una función iterateDictionary(some_list)que, dada una lista de diccionarios, la función recorra cada diccionario de 
# la lista e imprime cada clave y el valor asociado. Por ejemplo, dada la siguiente lista:
estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(estudiantes):
    for i in range(len(estudiantes)):
        for key, value in estudiantes[i].items():
            print(f"{key} - {value} ", end=" ")
        print("")   

(iterateDictionary(estudiantes))



# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)
'''
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel
'''


#3 Obtener valores de una lista de diccionarios
#Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave,
#  la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo,
#  iterateDictionary2('name', estudiantes) debería generar:
'''
Michael
John
Mark
KB
'''
def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])

iterateDictionary2('first_name',estudiantes)
iterateDictionary2('last_name',estudiantes)

#4 Iterar a través de un diccionarios con valores de lista
# Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas, 
# imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores 
# asociados dentro de la lista de cada clave. Por ejemplo:
dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key, value in some_dict.items():
        print(f"{len(value)} {key.upper()}")
        for i in range(len(value)):
            print(value[i])
        print("")

printInfo(dojo)
# salida:
'''
7 UBICACIONES
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORES
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
'''