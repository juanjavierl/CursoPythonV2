class Auto:
    color = ""
    ruedas = 0

    def crear_coche(self, ruedas_auto, color_auto):
        self.color = color_auto
        self.ruedas = ruedas_auto
        return f"Auto color: {self.color} ruedas: {self.ruedas}"

objeto = Auto()
print(objeto.crear_coche(4, "Rojo"))

objeto1 = Auto()

print(objeto1.crear_coche(6, "verde"))
print(objeto1.color)
