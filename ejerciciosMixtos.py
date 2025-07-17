# tam = int(input("Tamanio: "))
# for fila in range(0, tam, 1):
#     for cols in range(0, tam, 1):
#         print("*", end=" ")
#     print()


""" tam = int(input("Tamanio: "))
for fila in range(0, tam, 1):
    for cols in range(0, tam, 1):
        if fila == cols:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print() """

for i in range(1,6,1):
    if i == 3:
        break
    print(i)


x = 5
while x > 0:
    x -= 1
    if x == 3:
        pass
    print(x)	#Salida: 4, 2, 1, 0
