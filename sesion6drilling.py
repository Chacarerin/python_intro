#Se requiere contar con un programa que, dados 3 números diferentes, los evalúe y entregue el
#orden de mayor a menor

x = (float(input("Hola, ingresa un número ")))
y = (float(input("Ahora ingresa otro número ")))
z = (float(input("Finalmente, ingresa un tercer número ")))

numeros =[x,y,z]

for i in numeros:
    if x > y and x > z:
        if y > z:
            numeros2=[x,y,z]
        else:
            numeros2=[x,z,y]    
    elif y > x and y > z:
        if x > z:
            numeros2=[y,x,z]
        else:
            numeros2=[y,z,x]
    else:
        if x > y:
            numeros2=[z,x,y]
        else:
            numeros2=[z,y,x]
          
print("Evaluando la lista de números que ingresaste...")
print("La lista de números ingresada, ordenada de mayor a menor es:")
for i in numeros2:
    print(i)
