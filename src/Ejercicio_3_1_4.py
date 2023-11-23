# Ejercicio 3.1.4
# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.


def numeros_loteria():
    loteria = []
    for _ in range(6):
        while True:
            try:
                numero = int(input("Ingresa un número de la lotería: "))
                if 1 <= numero <= 49:
                    loteria.append(numero)
                    break
                else:
                    print("Numero incorrecto. Debe estar en el rango 1-49.")
            except ValueError:
                print("Numero equivocado.")
    loteria.sort()
    numerosunidos = ', '.join(map(str, loteria))
    return numerosunidos


def main():
    loteria = numeros_loteria()
    print(f"Los números de su lotería son: {loteria}")


if __name__ == "__main__":
    main()