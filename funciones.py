""" public void saludar(){
} """


""" def saludar(nombre, edad, direccion="Av. Civica"):
    #todo mi codigo
    print("Buenas noches:", nombre, "tu edad es: ", edad)
    print("Dir: ",direccion)
    saludo = f"Buenas noches: {nombre} tu edad es: {edad}"
    saludar(n, 26, "Calle Sanjinez")
    return saludo

n = input("Ingrese su nombre: ")
resultado = saludar(n, 26, "Calle Sanjinez")
print(resultado.upper()) """


def factorial(num):
    if num > 1:
        print(num)
        num = num * factorial(num -1)
    return num

print(factorial(5))
