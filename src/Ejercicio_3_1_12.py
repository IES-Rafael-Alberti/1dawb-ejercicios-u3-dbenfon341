# Ejercicio 3.1.12
# Escribir un programa que almacene las matrices A=(123456) y B=(−100111) en una lista y muestre por pantalla su producto. 
# Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
# A:
#   1 2
#   3 4
#   5 6
# B:
#   -1 0
#   0 1
#   1 1



def pintar_matriz(matriz:list) -> str
res = "
for vector in matriz:
    res += f"{vector[0]}, vector"


def main():

    matriz_1 = ((1, 2), (3, 4), (5, 6))
    matriz_2 = ((-1, 0), (0, 1), (1, 1))

    matriz_3 = [] #Lista vacía

    for fila in range(3):
        matriz_3.append(list())
        for columna in range(2):
            matriz_3[fila].append(
                matriz_1[fila][columna] *
                matriz_2[fila][columna])
            
    print


if __name__ == "__main__":
    main()