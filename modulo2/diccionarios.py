datos = {
            "nombre":"Juan Carlos",
            "edad":25,
            "estado": True,
            8:"Agosto"
        }

datos["Apellido"] = "Martinez"
#iterar un diccionario

""" for dato in datos:
    print(dato, datos[dato]) """
for clave, valor in datos.items():
    print(clave, " : ", valor)

#print(len(datos))
#print(f"{datos["nombre"]}  -  {datos["edad"]} Mes: {datos[8]}")
