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


""" def factorial(num):
    if num > 1:
        num = num * factorial(num -1)
    return num

print(factorial(5)) """

def despedida(nombre):
    print("Fue un gusto ayudarte: ", nombre)

def saludar(nombre):
    print("Buenas noches", nombre)
    despedida(nombre)


def principal():
    nombre = input("Ingrese su nombre: ")
    saludar(nombre)

#principal()



def factorial(num):
    if num > 1:
        num = num * factorial(num -1)
    return num
#C = n! / (r! * (n-r)!)
def calcular(n, r):
    valor_n = factorial(n)
    valor_r = factorial(r)
    valor_n_r = factorial(n-r)
    c = valor_n // (valor_r * (valor_n_r))
    return c

def principal():
    n = int(input("Valor de N: "))
    r = int(input("Valor R: "))
    print(calcular(n,r))

#principal()

suma = lambda x, y: x + y

#print(suma(10, 5))

""" def sumar(x, y):
    return x+y
print(sumar(1, 5)) """
""" 
determinar_num = lambda num: num>0

print(determinar_num(-5)) """

def saludar(nombre):
    print("Ejecutar tareas antes de a funcion")

    def funcion_interna():
        print(f"Hola {nombre} desde mi funcion interna")

    funcion_interna()
    print("Ejecutar tareas despues de a funcion")

#saludar("Jose")


def calcular_fac(num):
    print("Num original: ", num)
    num = num-1
    def factorial(num):
        if num > 1:
            num = num * factorial(num -1)
        return num
    res = factorial(num)
    print("resultado: ",res)
    if res > 0:
        return "Positivo"
    else:
        return "Ngativo"
    #return factorial(num)

#print(calcular_fac(5))



def evaluar_alumno(nombre, nota):
    def obtener_desempeño():
        if nota >= 9:
            return "muy bueno"
        elif nota >= 7:
            return "bueno"
        elif nota >= 5:
            return "regular"
        else:
            return "malo"
    
    desempeño = obtener_desempeño()
    return f"El alumno {nombre.capitalize()} tiene un desempeño {desempeño} con nota {nota}."
# Pruebas
#print(evaluar_alumno("ana", 9.5))   # muy bueno


#c -> a(b)

""" def funcion_a(funcion_b):
    def funcion_c():
        print("Antes de la ejecucion")
        funcion_b()
        print("Despues de la ejecucion")
    return funcion_c

@funcion_a
def funcion_b():
    print("Hola desde la funcion Original") """

#funcion_b()

import time
def medir_tiempo(func):
    def medir(*arg, **kwarg):
        inicio = time.time()
        resultado = func(*arg, **kwarg)
        fin = time.time()
        print(f"tienpo de ejecucion: {fin - inicio:4f} segundos")
        return resultado
    return medir

@medir_tiempo
def factorial_num(num):
    fac = 1
    for i in range(1, num+1, 1):
        fac = fac *i
    return fac

factorial_num(1545)

@medir_tiempo
def mi_funcion():
    pares = 0
    for i in range(1, 10, 1):
        if i%2==0:
            pares +=1
    print("Total de numeros Pares: ", pares)

mi_funcion()