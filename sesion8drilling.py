data = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]

for item in data:
    if item[0] == 0:
        continue
    else:
        sublista = []
        for elem in item:
            if elem !=0:
                sublista.append(elem)
        print(sublista)


claves = ['A','B','C','D']

mi_dict = {}

for i in range(len(data)):
    mi_dict[claves[i]] = data[i]

print(mi_dict)