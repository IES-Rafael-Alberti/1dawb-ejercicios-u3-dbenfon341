# Ejercicio 3.1.6
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine 
# de la lista las asignaturas aprobadas. 
# Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.


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
    for i in range(len(notas)):
        if notas[i] >= 5:
            print(f"En {materias[i]} has sacado {notas[i]}.")
        else:
            print(f"Debe repetir {[materias[i]]}.")


def main():
    materias = asignaturas()
    notas = dame_notas(materias)
    mostrar_notas(materias, notas)


if __name__ == "__main__":
    main()