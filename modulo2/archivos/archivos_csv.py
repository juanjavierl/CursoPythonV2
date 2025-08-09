import csv

def escribir_archivo():
    personas=[
        ["Nombre", "Edad"],
        ["Jose", 30],
        ["Ana", 16],
        ["Carlos", 20]
    ]

    with open("personas.csv","w" , newline='', encoding="utf-8") as file:
        escribir = csv.writer(file)
        for p in personas:
            escribir.writerow(p)
        return f"Los degistros se guardaron"

#print(escribir_archivo())
def determinar_mayor(edad):
    if int(edad) >=18:
        estado = "Mayor de Edad"
    else:
        estado = "Menor de Edad"
    return estado


def leer_datos():
    with open("personas.csv", newline="", encoding="utf-8") as file:
        leer = csv.reader(file)
        next(leer)
        registros = 0
        cont_mayores = 0
        cont_menores = 0
        for fila in leer:
            
            print(f"{fila[0]} Edad: {fila[1]} {determinar_mayor(fila[1])}")
            registros +=1
            if int(fila[1]) >=18:
                cont_mayores +=1
            else:
                cont_menores +=1
        print(f"Total registros: {registros}")
        print(f"Total Mayores: {cont_mayores}")
        print(f"Total Menores: {cont_menores}")
#leer_datos()


def buscar_persona():
    resultados = []
    texto_buscar = input("Ingrese un nombre:")
    with open("personas.csv", newline="", encoding="utf-8") as file:
        leer = csv.reader(file)
        next(leer)
        for fila in leer:
            if fila[0].lower().strip() == texto_buscar.lower().strip():
                resultados.append(fila)
        if resultados:
            print(f"Total Coinsidentes: {len(resultados)} encontrados")
            for dato in resultados:
                print(" ".join(dato))
        else:
            print("No hay resultados")
    return resultados

buscar_persona()

