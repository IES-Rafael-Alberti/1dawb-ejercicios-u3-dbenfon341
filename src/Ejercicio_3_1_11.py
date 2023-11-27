# Ejercicio 3.1.11
# Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.


def producto_escalar():

    vectores1 = (1,2,3)
    vectores2 = (-1,0,2)


    if len(vectores1) != len(vectores2):
        return None
    else:
        resultado = 0
        for i in range(len(vectores1)):
            resultado += vectores1[i] * vectores2[i]

        print(resultado)


def main():
    producto_escalar()

if __name__ == "_main__":
    main()