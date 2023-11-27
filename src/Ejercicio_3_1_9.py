# Ejercicio 3.1.9
# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.


def contar_vocales(palabra):
    numero_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for letra in palabra:
        if letra.lower() in 'aeiou':
            numero_vocales[letra.lower()] += 1
    return numero_vocales


def main():
    palabra_usuario = input('Ingrese una palabra: ')
    resultado = contar_vocales(palabra_usuario)


    for vocal, numero in resultado.items():
        print(f'La vocal {vocal} aparece {numero} veces.')


if __name__ == "__main__":
    main()