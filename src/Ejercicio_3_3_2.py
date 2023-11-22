# Ejercicio 3.3.2
# Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de una escuela, 
# finalizando cuando se introduzca “x”. A continuación, solicitar que introduzca los nombres de los alumnos de secundaria, finalizando al introducir “x”.
# 
# Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
# Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
# Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
# Mostrar si todos los nombres de primaria están incluidos en secundaria.


def main():
    nombres_primaria = set()
    nombres_secundaria = set()
    while True:
        nombre_primaria = input("Introduce el nombre de un alumno de primaria (introduce x para salir): ").title()
        nombres_primaria.add(nombre_primaria)
        if nombre_primaria == "X":
            break
    while True:
        nombre_secundaria = input("Introduce el nombre de un alumno de secundaria (introduce x para salir): ").title()
        nombres_secundaria.add(nombre_secundaria)
        if nombre_secundaria == "X":
             break
    nombres_secundaria.remove("X")
    nombres_primaria.remove("X")

    nombres_unidos = nombres_primaria | nombres_secundaria
    nombres_repetidos = nombres_primaria & nombres_secundaria
    nombres_no_repetidos_secundaria = nombres_primaria - nombres_secundaria
    nombres_no_repetidos_primaria = nombres_secundaria - nombres_primaria

    print (f"Los nombres unidos son: {nombres_unidos}")
    print (f"Los nombres que se repiten entre los alumnos de primaria y secundaria son: {nombres_repetidos}")
    print (f"Los nombres que no se repiten en los de nivel secundaria son: {nombres_no_repetidos_secundaria}")
    print (f"Los nombres que no se repiten en los de nivel primaria son: {nombres_no_repetidos_primaria}")


if __name__ == "__main__":
    main()