""" cadena = "hola como estas"

#print(cadena[0:6])
longitud = len(cadena)

for indice in range(0, longitud, 1):
    print(cadena[indice], end=" ")

for letra in cadena:
    print(letra, end=" ") """



texto = input("Ingresa una cadena de texto: ")
caracter = input("Ingrese la letra que deseas contar: ")

# Validar que ingresó exactamente una letra
if len(caracter) == 1:
    contador = 0
    for letra in texto:
        if letra.lower() == caracter.lower():
            contador += 1
    print("La letra:", caracter, "se repite:", contador)
else:
    print("Error: Debes ingresar exactamente una sola letra.")
