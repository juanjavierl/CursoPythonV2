#import saludos as s
""" from saludos import *
print(saludar("Jose"))

print(contar_letras("Jose")) """

#paquetes
from paquete.saludo import saludar

s = saludar("Maria")
print(s)

#subPaquete

from paquete.subpaquete.funciones import sumar

print(sumar(10,5))