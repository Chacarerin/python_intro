#Dada la siguiente lista de nombres:

#Y sabiendo que Harry Houdini, David Blaine y Teller son magos. Y también que Newton, Hawking y
#Einstein son científicos. Debemos separar los nombres en tres grupos: magos, científicos y otros; y
#escribir una función llamada hacer_grandioso(), que modifique la lista de magos añadiendo la
#frase ‘El gran‘ antes del nombre de cada mago.
#Crear una función llamada imprimir_nombres(), que imprime el nombre de cada persona de la
#lista.
#Finalmente, imprimir en pantalla la lista completa de nombres antes de ser modificados; luego
#imprimir los nombres de los magos grandiosos, los nombres de los científicos, y los restantes.

def imprimir_nombres(lista):
    for item in lista:
        print(item)

def hacer_grandioso(lista):
    grandiosos = [f"{"El gran "}{item}" for item in lista]
    for item in grandiosos:
        print(item)

nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

magos = ["Harry Houdini", "David Blane", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]
otros = []

imprimir_nombres(nombres)

hacer_grandioso(magos)

imprimir_nombres(cientificos)

for item in nombres:
    if item not in magos and item not in cientificos:
        otros.append(item)

imprimir_nombres(otros)

