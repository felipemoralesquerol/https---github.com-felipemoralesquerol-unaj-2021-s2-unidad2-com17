datos = []
datos.append("hola")
datos = datos + ["estudiantes"] + [123, 123, 123]
datos[0] = "Hola"
datos[1] = "Estudiantes"
datos.remove(123)
del datos[0]

print(datos)
