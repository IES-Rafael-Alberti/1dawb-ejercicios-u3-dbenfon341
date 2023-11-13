# Ejercicio 3.1.1
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.


def asignaturas():
    materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    for materia in materias:
        materia_print = print(materia)
    return materia_print


def main():
    asignaturas()


if __name__ == "__main__":
    main()