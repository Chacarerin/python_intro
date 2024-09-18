#Requerimos calcular el factorial de un número, asignarlo a una variable, y luego imprimirla.
#sabiendo que el factorial es el resultado de la multiplicación de todos los enteros positivos que hay
#entre un número y uno. Ejemplo: Factorial de 4 es 4 * 3 * 2 * 1.

numero = int(float(input("ingresa un número ")))

factorial=1 #debo iniciar en 1

for i in range(1, numero+1): 
    factorial *= i

print(f"El factorial de {numero} es {factorial}")