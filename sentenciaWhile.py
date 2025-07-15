""" contador = 11
while contador >= 1:
    print(contador, end=" ")
    contador = contador - 1 """


""" 
suma=0
n=int(input("Número positivo:"))
while n!=0:
    digito=n%10
    suma+=digito
    n=n//10
print("Suma de los dígitos:", suma) """

"""
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
....




2 * 10 = 20
"""
""" numero = int(input("Ingrese un numero: "))
i = 1
while i <= 10:
    #resultado = numero * i
    print(f"{numero} * {i} es igual a: {numero * i}")
    #print(numero, " * ", i, " = ", numero * i)
    i = i + 1
    #i +=1 """


""" limite = int(input("Ingrese un numero: "))
numero = 1
while numero <= limite:
    i = 1
    while i <= 10:
        print(f"{numero} * {i} = {numero * i}")
        i = i + 1
    print()
    numero+=1 """


numero = 1
contador = 0
par = 0
while numero > 0:
    numero = int(input("valor: "))
    contador+=1
    if numero % 2 == 0:
        par = par+1
print("Total de numeros: ", contador)
print("Total de numeros pares: ", par)


