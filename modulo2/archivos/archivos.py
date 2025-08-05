""" archivo = open("lista.txt", "w")  # "r" = read (leer)
contenido = archivo.write("Curso de Python")
archivo.close() """
#Modo escritura
with open("lista.txt", "w") as archivo:
    archivo.write("Hola mundo\n")
    archivo.write("Segunda línea")

#Modo Escritura al final
with open("lista.txt", "a") as archivo:
    archivo.write("\nNueva línea agregada")

#Iterar el contenido del archivo
with open("lista.txt", "r") as archivo:
    #print(archivo.readline())
    contador = 0
    for linea in archivo:
        contador +=1
        print(linea.strip())
    print("total Lineas leidas",contador)

    
