def mis_datos(diccionario):
    diccionario['nombre'] = input("Ingrese su nombre: ")
    diccionario['edad'] = int(input("Ingrese su edad: "))
    diccionario['carrera'] = input("Ingrese su carrera: ")
    diccionario['estatura'] = input("Ingrese su estatura: ")

    for clave, valor in diccionario.items():
        print(clave, " : ", valor)

diccionario = {}
#mis_datos(diccionario)



# Diccionario de alumnos con sus notas

# Recorrer cada alumno y mostrar su información
""" for alumno_id in alumnos:
    alumno = alumnos[alumno_id]
    nombre = alumno['nombre']
    notas = alumno['notas']
    total = sum(notas)
    promedio = total // len(notas)
    
    if promedio >= 61:
        estado = "Aprobado"
    else:
        estado = "Reprobado"
    
    # Mostrar información
    print(f"{nombre} Notas: {notas}  Total: {total} Promedio: {promedio} {estado}")
 """

def mi_diccionario(alumnos):
    resultado = ""
    for alumno in alumnos.values():
        nombre = alumno['nombre']
        notas = alumno['notas']
        total = sum(notas)
        promedio = total // len(notas)
        estado = "Aprobado" if promedio >=61 else "Reprobado"
        resultado += f"{nombre} Notas: {notas} promedio: {promedio} {estado}\n"

    return resultado

def mejor_estudiante(alumnos):
    mejor_promedio = 1
    nombre_estudiante = ""
    for alumno in alumnos.values():
        nombre = alumno['nombre']
        notas = alumno['notas']
        promedio = sum(notas) // len(notas)
        if promedio > mejor_promedio:
            mejor_promedio = promedio
            nombre_estudiante = nombre
    return nombre_estudiante, mejor_promedio

def main():
    alumnos = {
        0: {'nombre': "Juan David", 'notas': [60, 55, 75]},
        1: {'nombre': "Rodrigo", 'notas': [50, 30, 45]},
        2: {'nombre': "David", 'notas': [70, 55, 75]},
        3: {'nombre': "Jhannet", 'notas': [60, 65, 85]},
        4: {'nombre': "Beto", 'notas': [25, 50, 35]}
    }
    print(mi_diccionario(alumnos))
    #(jannet, 70)
    estudiante, promedio = mejor_estudiante(alumnos)
    print(f"El estudiante: {estudiante} tiene le mejor pro: {promedio}")

main()