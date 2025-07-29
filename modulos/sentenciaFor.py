""" for(int i = 30, i>=3, i-=3){

} """

""" para incrementar
for i in range(0, 31, 3):
    print(i) """

""" for i in range(30, 0, -3):
    print(i) """
pares = 0
for i in range(1, 10, 1):
    if i%2==0:
        pares +=1
    print(i)
print("Total de numeros Pares: ", pares)


""" multiplicador=int(input("multiplicador: "))
for i in range(1, multiplicador):  # límite hasta el número dado
    for j in range(1, 11):  # Multiplicador (1 al 10)
        print(i, " x " ,j, " = ",i * j) # muestra la tabla
    print() # para cuando termine el segundo for hago un salto """

