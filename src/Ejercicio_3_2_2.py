# Ejercicio 3.2.2
# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
# Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.


def add_datos():
    datos = {}

    nombre = input("Introduce tu nombre: ")
    datos["nombre"] = nombre
    edad = input("Introduce tu edad: ")
    datos["edad"] = edad
    direccion = input("Introduce tu dirección: ")
    datos["direccion"] = direccion
    telefono = input("Introduce tu número de teléfono: ")
    datos["telefono"] = telefono
    
    return datos


def main():
    informacion = add_datos()
    print ("Tu nombre es: " + (informacion["nombre"]) + ", tu edad es: " + (informacion["edad"]) + ", tu dirección es: " + (informacion["direccion"]) + ", tu teléfono es: " + (informacion["telefono"]),  )


if __name__ == "__main__":
    main()