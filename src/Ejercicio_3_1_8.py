# Ejercicio 3.1.8
# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.


def palindromo(palabra):
    palabrainvertida = palabra[::-1]
    if palabra == palabrainvertida:
        return "La palabra es palindromo."
    else:
        return "La palabra no es palindromo."


def main():
    palabra = input("Introduce una palabra y te diré si es palindromo: ")
    final = palindromo(palabra)
    print(final)


if __name__ == "__main__":
    main()