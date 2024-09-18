mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 20, 15]

#1. Eliminar los elementos duplicados.
#2. Ordenar la lista resultante en orden ascendente.

for i in mi_lista:
    contador=0
    for x,y in enumerate(mi_lista):
        if i==y:
            contador+=1
            if contador>1:
                del mi_lista[x]
            
print(sorted(mi_lista))