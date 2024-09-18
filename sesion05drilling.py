#Requerimos eliminar todas las vocales de la palabra “paralelepípedo”, e imprimir en pantalla las
#consonantes restantes y su posición dentro de dicha palabra.

palabra = "paralelepípedo"
vocal = "aeiou"

for index, character in enumerate(palabra):
    if character not in vocal:
        print(f"consonante: {character}, posición: {index}")