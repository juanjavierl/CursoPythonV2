import json
import random
import math

class Auto:
    def __init__(self, ruedas_auto, color_auto, placa):
        self.color = color_auto
        self.ruedas = ruedas_auto
        self.__placa = placa
        
    def __getattr__(self):
        return self.ruedas
    
    def __str__(self):
        return f"Auto con: {self.ruedas} ruedas y es de color {self.color}"

    def __setattr__(self, color, newColor):
        super().__setattr__(color, newColor)

    def datos_json(self):
        datos = {'ruedas ':self.ruedas,'color ':self.color}
        return json.dumps(datos)
    
    def mostrar_placa(self):
        return self.__placa
    
    def __calentar(sel): 
        return "El motor se está calentando"
    
    def encender(self):
        return self.__calentar()

class AutoElectrico(Auto):
    def __init__(self, ruedas_auto, color_auto, placa, energia):
        super().__init__(ruedas_auto, color_auto, placa)
        self.energia = energia

autoElec = AutoElectrico(4,"Azul", "xyz-321", "Alto")
print(autoElec.mostrar_placa())



class Persona:
    def __init__(self, nombre, apellido, ci):
        self.nombre = nombre
        self.apellido = apellido
        self.__ci = ci

    def __str__(self):
        return f"Nombre: {self.nombre} Apellido {self.apellido}"
    
    def conducir(self, auto):
        return auto.encender()
    
    def mostrar_color(self, auto):
        return auto.color

# auto1 = Auto(8, "Blanco", "ABC-123")
# print(auto1)

# persona = Persona("Jose", "Martinez", 12345)
# print("Llamada al metodo del auto: ", persona.conducir(auto1))
# print(f"La persona: {persona.nombre} tiene el auto color: {persona.mostrar_color(auto1)}")


# auto1.ruedas = 4
# print(auto1)
# print(auto1.datos_json())

# print("Placa: ", auto1.encender())