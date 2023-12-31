# Ejercicio 3.2.3
# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, 
# un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
# 
# Fruta	Precio
# Plátano	1.35
# Manzana	0.80
# Pera	0.85
# Naranja	0.70


def main():
    frutas = {"Plátano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}


    fruta = input("Introduce una fruta: ").title()
    while frutas.get(fruta) == None:
        print("La fruta es incorrrecta.")
        fruta = input("Introduce una fruta: ").title()
    else:
        kilos = float(input("Introduce el peso de la fruta: "))
        precio = frutas[fruta]*kilos
        print(f"El precio de la fruta es: {precio}")


if __name__ == "__main__":
    main()