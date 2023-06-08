print("funcion cuenta regresiva")
#crea una función que acepte un número como entrada. Devuelve una lista nueva que cuente de uno en uno, 
#desde el número (como elemento 0) hasta 0 (como último elemento). 
#Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0]
def cuenta_regresiva(num):
    lista=[]
    for i in range(num,-1,-1):
        lista.append(i)
    return lista
print(cuenta_regresiva(5))
print(cuenta_regresiva(10))
print(cuenta_regresiva(20))

print("funcion imprime y devuelve")
#crea una función que recibirá una lista con dos números. Imprime el primer valor y devuelve el segundo.
# Ejemplo: imprime_y_devuelve ([1,2]) debería imprimir 1 y devolver 2

def imprime_y_devuelve(lista):
    print(lista[0])#imprime el primer valor
    return lista[1]
imprime_y_devuelve([1,2])#imprime el valor 1 y el segundo valor lo devuelve en un retorno pero no lo imprime


print("funcion primero mas longitud")
#crea una función que acepta una lista y devuelve la suma del primer valor de la lista más la longitud de la lista.
# Ejemplo: primero_mas_logitud([1,2,3,4,5]) debería devolver 6 (primer valor: 1 + longitud: 5)

def primero_mas_longitud(lista):
    return lista[0]+len(lista)

print(primero_mas_longitud([1,2,3,4,5]))#imprime 6 ->toma el primer valor de la lista y le suma la longitud de la lista que es 5

print("funcion valores mayores que el segundo")
#Escribe una función que acepte una lista y crea una nueva lista que contenga solo los valores de la lista original
# que sean mayores que su segundo valor. Imprima cuántos valores son y luego devuelva la nueva lista.
# Si la lista tiene menos de 2 elementos, haga que la función devuelva False
# Ejemplo: valores_mayores_que_el_segundo ([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4]
# Ejemplo: valores_mayores_que_el_segundo ([3]) debería devolver False

def valores_mayores_que_el_segundo(lista):
    if len(lista)<2:
        return False
    else:
        lista_nueva=[]
        for i in range(len(lista)):
            if lista[i]>lista[1]:
                lista_nueva.append(lista[i])
        print(len(lista_nueva))
        return lista_nueva

print(valores_mayores_que_el_segundo([5,2,3,2,1,4])) #imprime 3 y devuelve [5,3,4]
print(valores_mayores_que_el_segundo([3])) #devuelve False

print("funcion esta longitud ese valor")
#Escribe una función que acepte dos enteros como parámetros: tamaño y valor.
# La función debe crear y devolver una lista cuya longitud es igual al tamaño dado y cuyos valores son todos los valores dados.
# Ejemplo: esta_longitud_ese_valor (4,7) debería devolver [7,7,7,7]
# Ejemplo: esta_longitud_ese_valor (6,2) debería devolver [2,2,2,2,2,2]

def esta_longitud_ese_valor(tamano,valor):
    lista=[]
    for i in range(tamano):
        lista.append(valor)
    return lista

print(esta_longitud_ese_valor(4,7)) #devuelve [7,7,7,7]
print(esta_longitud_ese_valor(6,2)) #devuelve [2,2,2,2,2,2]
print(esta_longitud_ese_valor(10,5)) #devuelve [5,5,5,5,5,5,5,5,5,5]

