#Escribir un programa que analice un número, e indique si es positivo o negativo, y si es par o impar.
#En caso de ser cero, también indicarlo. Se debe usar la expresión if-elif-else, y no usar
#subcondiciones; en su lugar, usar condiciones anidadas.

numero = int(float(input("Hola, ingresa un número ")))

if numero == 0:
    print(f"El número", numero, "es cero.")
elif numero > 0 and numero %2 == 0 and numero != 0:
    print(f"El número", numero, "es positivo y par.")
elif numero < 0 and numero %2 == 0 and numero != 0:
    print(f"El número", numero, "es negativo y par.")
else: 
    print(f"El número", numero, "es negativo e impar.")

