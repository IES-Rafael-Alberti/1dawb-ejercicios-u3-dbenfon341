# Ejercicio 3.1.5
# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.


def numeros_orden():
    lista = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    lista.reverse()
    numerosunidos = ', '.join(lista)
    return numerosunidos


def main():
    numeros = numeros_orden()
    print(numeros)


if __name__ == "__main__":
    main()