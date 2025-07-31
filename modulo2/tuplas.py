# t = ('a', 'b', 'c', 'd', 'e', (1,2,3,4,5))

# print("Cantidad de elementos: ",len(t))
# print(t[0].upper())
# print(t[2:4+1])
# print(t[5][3])

# print("x" in t)

# a = 10
# b = 20
# c = 30
# mi_tupla = a, b, c
# print(mi_tupla)

# x, y, z = mi_tupla

# print(x)
# print(y)
# print(z)


""" mi_tabla = (10, 20, 30, 40)

for i in range(0, len(mi_tabla), 1):
    print(mi_tabla[i])

x = 20
for valor in mi_tabla:
    if x == valor:
        print("encontrado") """


""" def mis_datos():
    alumnos = (
        ('Perico', 'Los Palotes', '201199001-5', 'Civil'),
        ('Fulano', 'De Tal',      '201199002-6', 'Electrica'),
        ('Beymar', 'De Tal',      '201199003-7', 'Mecanica'),
    )

    for nombre, _, _, carrera in alumnos:
        print(nombre, 'estudia', carrera) 
    
    for i in alumnos:
        print(i[0], "estudia: ",i[3])

mis_datos() """




def esta_ordenado(tupla):
    for i in range(len(tupla)-1):
        if tupla[i] > tupla[i+1]:
            return False
    return True


mi_tupla = (1,2,3,4,5)
print(esta_ordenado(mi_tupla))