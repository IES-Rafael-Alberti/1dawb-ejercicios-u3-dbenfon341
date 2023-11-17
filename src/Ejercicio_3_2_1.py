# Ejercicio 3.2.1
# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

def moneditas():
    monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    return monedas


def main():
    moneda = input("Introduce la divisa: ")
    monedas = moneditas()
    print(monedas.get(moneda.title(), "Esa divisa no está en la lista.."))


if __name__ == "__main__":
    main()