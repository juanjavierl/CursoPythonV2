""" import math

num = int(input("Ingrese un numero: "))
print(int(math.sqrt(num)))
print(math.pow(2,3))
print(math.factorial(num))
#entrada 5! proceso 1*2*3*4*5 salida: 120

import os
print(os.getcwd())#Devuelve la ruta completa

archivos = os.listdir(".")
print(archivos) """


from datetime import datetime, timedelta, time

print("Fecha y hora actual: ",datetime.today())
print("Hola actual: ",datetime.today().time())
print(datetime.now().date())

print(datetime.now().strftime("%d-%B-%Y, %H:%M:%S %p"))

fecha_str = "2025-06-02 14:30:00"
fecha = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")

print(fecha.year)
print(fecha.month)
print(fecha.day)

print(fecha + timedelta(days=6))

fecha1 = datetime(2024, 6, 2, 14, 1)
fecha2 = datetime(2030, 6, 2, 14, 0)
if fecha1 > fecha2:
    print("fecha 1 es mayor ")
else:
    print("fecha 2 es mayor")
