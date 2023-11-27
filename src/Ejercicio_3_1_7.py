# Ejercicio 3.1.7
# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

def lista_abecedario():
    lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    abecedarionumeros = [letra for index, letra in enumerate(lista) if (index + 1) % 3 != 0]
    return abecedarionumeros


def main():
    final = lista_abecedario()
    print(final)

if __name__ == "__main__":
    main()