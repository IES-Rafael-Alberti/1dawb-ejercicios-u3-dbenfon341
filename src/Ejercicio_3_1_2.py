# Ejercicio 3.1.2
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, 
# donde <asignatura> sobre cada una de las asignaturas de la lista.


def asignaturas():
    materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    return materias


def main():
    materias = asignaturas()
    for materia in materias:
        print (f"Yo estudio {materia}.")


if __name__ == "__main__":
    main()