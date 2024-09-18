#Crear una función que sume dos números, otra que reste dos números, otra que multiplique dos
#números, y otra que divida dos números. Adicionalmente, crear una función que acepte dos
#números como parámetros y regrese el resultado en forma de tupla de su suma, resta,
#multiplicación y división.
#Los resultados se deben almacenar en un diccionario, cuyas claves serán: Suma, Resta,
#Multiplicación y División, y los valores de cada clave serán los resultados obtenidos con la función
#creada anteriormente.

x = float(input("ingrese un número "))
y = float(input("ingresa ahora otro número "))

def suma(x,y):
    suma = x + y
    return suma

def resta(x,y):
    resta = x - y
    return resta

def producto(x,y):
    producto = x * y
    return producto

def division(x,y):
    division = x / y
    return division

a = suma(x,y)
b = resta(x,y)
c = producto(x,y)
d = division(x,y)
    
tupla1 = (("Suma", a),("Resta", b),("Multiplicación", c),("División", d))

diccionario = dict(tupla1)

print(diccionario)

