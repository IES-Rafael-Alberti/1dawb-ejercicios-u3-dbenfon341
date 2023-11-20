# Ejercicio 3.2.6
# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) 
# que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.


def add_datos():
    datos = {}

    nombre = input("Introduce tu nombre: ")
    datos["nombre"] = nombre
    print ("Tu nombre es: " + (datos["nombre"]))

    edad = input("Introduce tu edad: ")
    datos["edad"] = edad
    print ("Tu nombre es: " + (datos["nombre"]) + "tu edad es " + (datos["edad"]))

    direccion = input("Introduce tu dirección: ")
    datos["direccion"] = direccion
    print ("Tu nombre es: " + (datos["nombre"]) + "tu edad es " + (datos["edad"]) + "tu dirección es" + (datos["direccion"]))

    telefono = input("Introduce tu número de teléfono: ")
    datos["telefono"] = telefono
    print ("Tu nombre es: " + (datos["nombre"]) + "tu edad es " + (datos["edad"]) + "tu dirección es" + (datos["direccion"]) + "tu telefono es" + (datos["telefono"]))

    return datos


def main():
    add_datos()


if __name__ == "__main__":
    main()