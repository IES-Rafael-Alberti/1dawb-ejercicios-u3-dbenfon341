# Ejercicio 3.3.6
# Dado el conjunto de letras:
# 
# vocales = {'a', 'e', 'i', 'o', 'u'}
# Crea un conjunto consonantes que contenga las letras del alfabeto que no son vocales.
# Crea un conjunto letras_comunes que contenga las letras que están tanto en el conjunto vocales como en el conjunto consonantes.


def main():
    consonantes = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
    vocales = {'a', 'e', 'i', 'o', 'u'}
    letras_comunes = consonantes | vocales
    print (letras_comunes)


if __name__ == "__main__":
    main()