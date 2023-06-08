print("----1------")
#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#retorna 5
print("----3------")

#2
#def number_of_military_branches():
#    return 5
#print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# Retorna error porque la funcion no esta definida aún, aunque abajo se defina, el orden de ejecucion es de arriba hacia abajo.
#dejaré comentado el codigo para que no me de error en la ejecucion de los demas ejercicios, y copiaré este
#codigo en el ejercicio 9 para que se ejecute correctamente.

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#retorna 5, el otro return no se ejecuta porque el primero ya retorna un valor y termina la funcion.
print("----4------")

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#retorna 5, el print(10) no se ejecuta porque el return 5 ya retorna un valor y termina la funcion.
print("----5------")
#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#retorna 5 y None, porque la funcion no tiene un return, solo un print, por lo que no retorna un valor
# y el print(x) imprime el valor de x, que es None.
print("---6-------")
#6
def add(b,c):
    return(b+c)
print(add(1,2) + add(2,3))
#retorna 3, 5 y error, porque la funcion add no tiene un return, solo un print,
#por lo que no retorna un valor
#para corregirlo, se debe agregar un return b+c en la funcion add, para que retorne
# el valor de la suma de b y c.
print("----7------")
#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#retorna 25, porque la funcion retorna un string de la concatenacion de b y c, 
# que son 2 y 5, por lo que retorna 25, que es un string.
print("----8------")
#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#retorna 100 y 10, porque la funcion retorna 10, ya que b es mayor a 10, por lo que
# no se ejecuta el return 5, y el print(b) imprime el valor de b, que es 100.
# el return 7 no se ejecuta porque el return 10 ya retorna un valor y termina la funcion.
print("----9------")
#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#retorna 7, 14 y 21, porque la funcion retorna 7, ya que b es menor a c, por lo que
# no se ejecuta el return 14, y el print(b) imprime el valor de b, que es 7.
# el return 3 no se ejecuta porque el return 7 ya retorna un valor y termina la funcion.
# el segundo print retorna 14, porque b es mayor a c, por lo que no se ejecuta el return 7,
# y el print(b) imprime el valor de b, que es 14.
# el tercer print retorna 21, porque la suma de los dos prints anteriores es 21.
print("----2------")

#2 ejecicio 2 que no se ejecutó por error en el ejercicio 2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_military_branches())
#retorna error porque la funcion number_of_days_in_a_week_silicon_or_triangle_sides() tiene dos parametros
# y no se le estan pasando los parametros, por lo que retorna error. le pondré dos parametros
#a la funcion para que se ejecute correctamente.

#10
print("----10------")
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#retorna 8, porque la funcion retorna la suma de b y c, que son 3 y 5, por lo que retorna 8. Además,
# el return 10 no se ejecuta porque el return b+c ya retorna un valor y termina la funcion.
print("----11------")

#11
b = 500
print(b)#1
def foobar():
    b = 300
    print(b)#3
print(b)#2
foobar()
print(b)#4
#retorna 500, 500, 300 y 500, porque el primer print(b) imprime el valor de b, que es 500.
# el segundo print(b) imprime el valor de b, que es 500.
# el tercer print(b) imprime el valor de b, que es 300.
# el cuarto print(b) imprime el valor de b, que es 500.
print("----12------")
#12
b = 500
print(b) #1
def foobar():
    b = 300
    print(b)#3
    return b
print(b) #2
foobar()
print(b)#4
#retorna 500, 500, 300 y 500, porque el primer print(b) imprime el valor de b, que es 500.
# el segundo print(b) imprime el valor de b, que es 500.
# el tercer print(b) imprime el valor de b, que es 300.
# el cuarto print(b) imprime el valor de b, que es 500.
# el quinto print(b) imprime el valor de b, que es 500.
# retorna b la funcion foobar, pero no se guarda en ninguna variable, por lo que no se imprime.
print("----13------") 

#13
b = 500
print(b)#1
def foobar():
    b = 300
    print(b)#3
    return b
print(b)#2
b=foobar()#(b=300)
print(b)#4
#retorna 500, 500, 300 y 300, porque el primer print(b) imprime el valor de b, que es 500.
# el segundo print(b) imprime el valor de b, que es 500.
# el tercer print(b) imprime el valor de b, que es 300.
# el cuarto print(b) imprime el valor de b, que es 300.
# retorna b la funcion foobar, y se guarda en la variable b, por lo que se imprime el valor de b, que es 300.
print("----14------")

#14
def foo():
    print(1)#1->Se imprime 1
    bar()#Se llama la funcion bar
    print(2)#3->Se imprime 2

def bar():
    print(3)#2->Se imprime 3

foo()# 1 Se llama la funcion foo
#retorna 1, 3 y 2, porque la funcion foo imprime 1, luego llama a la funcion bar, que imprime 3,
# y luego la funcion foo imprime 2.

print("---15-------")

#15
def foo():
    print(1)#1->Se imprime 1
    x = bar()#Se llama la funcion bar y se guarda el valor de retorno en la variable x
    print(x)#3->Se imprime 5
    return 10#Se retorna 10 a la variable y de la funcion foo
def bar():
    print(3)#2->Se imprime 3
    return 5#Se retorna 5 que se guarda en la variable x de la funcion foo
y = foo()#Se llama la funcion foo
print(y)#4->Se imprime 10
#retorna 1, 3 y 10, porque la funcion foo imprime 1, luego llama a la funcion bar, que imprime 3,