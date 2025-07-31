""" mi_lista = [10, 20, 30, "Hola", True]

mi_lista[0] = 9
print("1er valor: ",mi_lista[0])

for i in range(0, len(mi_lista),1):
    print(mi_lista[i]) """

import random
""" def generar_lista(tamanio):
    lista = []
    for i in range(0, tamanio, 1):
        #lista.append(random.randint(0,20))
        valor = int(input("Ingrese un valor: "))
        if valor %3 == 0:
            lista.append(valor)
    return lista

def main():
    tamanio = int(input("Ingrese el tamanio de la lista: "))
    lista_generada = generar_lista(tamanio)
    print(lista_generada)

main() """

def generar_lista(tamanio):
    lista = []
    #for i in range(0, tamanio, 1):
    while len(lista) <= tamanio-1:
        valor = int(input("Ingrese un valor: "))
        if valor %3 == 0:
            lista.append(valor)
    return lista

def sumar_lista(lista):
    suma = 0
    for valor in lista:
        suma = valor + suma
    return suma

def ordenar_lista(lista):
    lista.sort()
    return lista

def main():
    try:
        tamanio = int(input("Ingrese el tamanio de la lista: "))
        lista_generada = generar_lista(tamanio)
        print(lista_generada)
        print("La suma de sus valores es: ",sum(lista_generada))
        print("Lista ordenada: ", ordenar_lista(lista_generada))
    except ValueError:
        print("Error del valor")
        main()
main()