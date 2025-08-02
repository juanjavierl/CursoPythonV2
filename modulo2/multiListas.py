""" 
lista = [
            [2,4,6,8],
            [0,1,0,1],
            [7,11,12,17],
        ]
lista.append([0,1,14,1])
lista[2][2] = 10
print(lista) """

import random
def multi_lista(fila, columna):
    multi_lista = [] #inicializamos una lista vacía
    for f in range(0, fila,1):
        lista = []
        for c in range(0, columna, 1):
            #print("Ingrese valor en el indice:",f," : ",c)
            #valor = int(input())
            lista.append(random.randint(0,9))  
        multi_lista.append(lista)
    return multi_lista

def sumarFila(multiLista):
    suma = []
    for fila in multiLista:
        suma.append(sum(fila))
    return suma

def busqueda(multiLista):
    pass

def main():
    try:
        fila = int(input("Ingrese el num. de filas: "))#ingresamos un número de filas
        columna = int(input("Ingrese el num. de Columnas: "))#número de columnas
        mul_lista = multi_lista(fila, columna)#llamada a la función
        print("lista::: ",mul_lista)
        print("Suma de cada Fila: ",sumarFila(mul_lista))
    except ValueError:
        print("Error en los datos")
        main()

main()