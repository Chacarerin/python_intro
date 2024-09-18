def es_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

estudiantes = [
 {'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]},
 {'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]},
 {'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]},
 {'nombre': 'Ana', 'edad': 13, 'calificaciones': [90, 92, 87]},
 {'nombre': 'Luis', 'edad': 20, 'calificaciones': [88, 85, 92]},
]

for x in estudiantes:
    promedio=sum(x['calificaciones']) / len(x['calificaciones'])

    if x['edad'] > 18 and promedio >= 85:
        print(f"{x['nombre']} es mayor de 18 años y tiene un promedio de calificaciones mayor a 85.")
    if es_primo(x['edad']) and x['edad'] > 18:
        print(f"{x['nombre']} como es mayor de 18 años y tiene una edad primo, se calcula su promedio de calificaciones; obteniendo un valor de {promedio:.2f}")