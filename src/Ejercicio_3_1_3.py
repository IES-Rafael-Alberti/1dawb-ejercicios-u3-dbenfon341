# Ejercicio 3.1.3
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, 
# y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.


def asignaturas():
    materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    return materias


def dame_notas(materias):
    notas = []
    for materia in materias:
        nota = float(input(f"Ingrese la nota de {materia}: "))
        notas.append(nota)
    return notas


def mostrar_notas(materias, notas):
    for i in range(len(materias)):
        print(f"En {materias[i]} has sacado {notas[i]}.")


def main():
    materias = asignaturas()
    notas = dame_notas(materias)
    mostrar_notas(materias, notas)


if __name__ == "__main__":
    main()