#Crear una función que acepte dos parámetros (base y altura) y calcule el área de un rectángulo. Validar que ambos sean números positivos.

def arearec(base, altura):
    area = base * altura
    return area

b = float(input("Ingrese el valor de la base: "))
a = float(input("Ingrese el valor de la altura: "))

while b <= 0: #uso <= para que también invalide el 0.
    if b <= 0:
        b = float(input("Por favor, ingrese un valor positivo para la base: "))
while a <= 0:
    if a <= 0:
        a = float(input("Por favor, ingrese un valor positivo para la altura: "))

r = arearec(b, a)

print("El área del rectángulo es de:", r)
