"""
La instrucción else complementa la instrucción if.
La palabra clave elif es la abreviatura de "else if".
"""

x = 28

if x < 0:
    print('x < 0')
elif x == 0:
    print('x is zero')
elif x == 1:
    print('x == 1')
else:
    print('Ninguno fue True')

name = "John"

if name == 'John':
    print(True)
else:
    print(False)
"""
TAREA modificar elif x else if identandolo
"""

x = 28

if x < 0:
    print('x < 0')
else:
    if x == 0:
        print('x is zero')
    else:
        if x == 1:
            print('x == 1')
        else:
            print('Ninguno fue True')

name = "John"

if name == 'John':
    print(True)
else:
    print(False)