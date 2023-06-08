
#variable declarations
#Variables primitivas
#numerica entera
num1 = 42
#numerica flotante
num2 = 2.3
#boleana 
boolean = True
#string
string = 'Hello World'
#listas
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
#tuplas
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
#diccionarios
fruit = ('blueberry', 'strawberry', 'banana')
#imprime el tipo de dato
print(type(fruit))
#imprime el indice 1 de la lista
print(pizza_toppings[1])
#agrega un elemento a la lista
pizza_toppings.append('Mushrooms')
#imprime el diccionario
print(person['name'])
#modifica el diccionario
person['name'] = 'George'
person['eye_color'] = 'blue'
#imprime la tupla
print(fruit[2])

#condicionales if con else
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

#condicionales if con elif
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

#ciclo for con un parametro que va de 0 a 4
for x in range(5):
    print(x)
#ciclo for con un parametro que x parte en dos y va de 2 a 4
for x in range(2,5):


    print(x)
#ciclo for con un parametro que x parte en dos y va de 2 a 9 de 3 en 3 
for x in range(2,10,3):
    print(x)
x = 0
#ciclo while que imprime x mientras sea menor a 5
while(x < 5):
    print(x)
    x += 1

#elimina el ultimo elemento de la lista
pizza_toppings.pop()
#elimina el elemento en el indice 1 de la lista
pizza_toppings.pop(1)

#imprime el diccionario
print(person)
#elimina el elemento eye_color del diccionario
person.pop('eye_color')
#imprime el diccionario
print(person)

#imprime la lista a través de un ciclo for
for topping in pizza_toppings:
    #condicional if que pregunta si el elemento si es igual a Pepperoni si es así continua el ciclo
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    #condicional if que pregunta el elemento si es igual a Olives y si es así rompe el ciclo
    if topping == 'Olives':
        break

#ciclo for que imprime los Hello 10 veces
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

#llama a la función print_hello_ten_times
print_hello_ten_times()

#ciclo for que imprime los Hello x veces
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

#llama a la función print_hello_x_times
print_hello_x_times(4)

#ciclo for que imprime los Hello 10 veces
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')
#llama a la función print_hello_x_or_ten_times, como no trae parametros por defecto es x = 10
print_hello_x_or_ten_times()
#llama a la función print_hello_x_or_ten_times, como trae parametros por defecto es x = 4
print_hello_x_or_ten_times(4)


"""
Bonus section
"""
#imprime la variable num3 que no existe y genera error
#print(num3)
#num3 = 72

# Se intenta cambiar la tupla fruiten el indice 0 por cranberry esto genera error, las tuplas no pueden modificarse
#fruit[0] = 'cranberry'

#imprime el diccionario con una key que no existe
#print(person['favorite_team'])

#imprime el elemento en el indice 7 del diccionario pero no existe ese indice
#print(pizza_toppings[7])

#imprime el tipo de datos de boolean
print(boolean)

# agrega un elemento a la tupla fruit, pero las tuplas no pueden modificarse
#fruit.append('raspberry')
#elimina el elemento en el indice 1 de la tupla fruit pero las tuplas no pueden modificarse
#fruit.pop(1)


#imprime el nombre y apellido de un doctor
doctor ="agustin arancibia españa "
