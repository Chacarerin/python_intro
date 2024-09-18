lista=[11,24,3,45,5,6,0,8,9,10] #se crea la lista de números

for x in lista: #se revisa la lista número por número
    if x % 2 == 0 and x != 0: #expresión para indicar si número es par pero excluir al cero
        print(f"El número {x} es par") 
    elif x == 0: #para identificar al 0
        print(f"El número {x} es cero")
    elif x % 2 != 0: #expresión para indicar si es impar
        print(f"El número {x} es impar")