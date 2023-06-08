# imprimir los numeros del 1 al 150
for x in range(1,151):
    print(x)

#imprimir separador
print("--------------------------------------------------") 

#imprimir los multiplos de 5 del 5 al 1000
for x in range(5,1001,5):
    print(x)

#imprimir separador
print("--------------------------------------------------")

#imprimir los enteros del 1 al 100. Si es divisible por 5, imprimir "Coding" en su lugar. Si es divisible por 10, imprimir "Coding Dojo".
for x in range(1,101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

#imprimir separador
print("--------------------------------------------------")

#agregar los numeros impares del 0 al 500,000 e imprimir la suma final.
suma = 0
for x in range(1,500001,2):
    suma += x
print(suma)

#imprimir separador
print("--------------------------------------------------")

#imprimir todos los valores del 2018 al 0 de 4 en 4.
for x in range(2018,0,-4): 
    print(x)

#imprimir separador
print("--------------------------------------------------")

# Establece tres variables: lowNum, highNum, mult. 
# Comenzando en lowNum y pasando por highNum,
#  imprime solo los enteros que sean múltiplos de mult. 
# Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas). 
lowNum = 2
highNum = 9
mult = 3
for x in range(lowNum,highNum+1):
    if x % mult == 0:
        print(x)

#imprimir separador
x=[5,24,10,1,5]
x+=[2]
print(x)

if ( not x):
    print("no hay nada")
else:
    print("hay algo")