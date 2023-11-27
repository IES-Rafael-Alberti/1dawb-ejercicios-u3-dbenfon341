# Ejercicio 3.2.4
# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.


def main():
    meses = [
    'enero', 'febrero', 'marzo', 'abril',
    'mayo', 'junio', 'julio', 'agosto',
    'septiembre', 'octubre', 'noviembre', 'diciembre'
    ]

    fecha_ingresada = input("Ingrese una fecha en formato dd/mm/aaaa: ")
    dia, mes, anio = map(int, fecha_ingresada.split('/'))
    nombre_mes = meses[mes - 1] if 1 <= mes <= 12 else 'mes inválido'

    print(f"La fecha en formato dd de {nombre_mes} de aaaa es: {dia} de {nombre_mes} de {anio}")
    

if __name__ == "__main__":
    main()