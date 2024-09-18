#excersice 1 y 2

x = -3
if x > 0 :
    print(x, "sin duda es positivo")
else :
    print(x, "sin duda es negativo")


#excercise 3

y = 0
if y > 0 :
    print(x, "sin duda es positivo")
elif y == 0 :
    print(y, "sin duda es igual a 0")
else :
    print(y, "sin duda es negativo")

#excercise 4

numeros = [6, 5, 3, 8, 4, 2, 5, 4, 11]
suma = 0

for x in numeros:
    suma = suma + x

    print("la suma es", suma)

#excercise 5

digitos = [0, 1, 5]
for i in digitos:
    print(i)
else: 
    print("no quedan elementos en la lista.")

#excercise 6
suma = 0
i = 1

while i <= 10:
    suma = suma + i
    i = i + 1
    print("la suma es", suma)
