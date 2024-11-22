print()
print('************************************************************')
print('    Crear una funcion que calcule el promedio de N notas    ')
print('************************************************************')
print()
suma = 0
i = 1
n = int(input('Ingrese Cantidad de Notas: '))
while i <= n:
    nota = float(input('Ingrese Nota: '))
    suma += nota
    i += 1
print (f'Sumatoria: ', suma, ' / Cantidad Notas: ', n)

def promedio(suma,n):
    prom = suma/n
    return prom

promedio_notas = promedio(suma, n)

print (f'El promedio de Notas es: ', promedio_notas)

print()
print('******************************************************************************************')
print('    Crear una funcion que determine si un color es primario o no, se debe imprimir por    ')
print('    pantalla la leyenda “el color X es primero “ o “el color X no es primario”            ')
print('******************************************************************************************')
print()

def es_primario(color):
    colores_primarios = {'ROJO', 'AMARILLO', 'AZUL'}
    return color.upper() in colores_primarios

color = input ('Ingrese Color: ')
color_upper = color.upper()

if es_primario(color):
    print(f'El color', color_upper, 'es PRIMARIO')
else:
    print(f'El color', color_upper, 'NO es PRIMARIO') 


print()
print('*************************************************************************************')
print('    Crear una funcion que determine que numero de una serie de N numeros es mayor    ')
print('*************************************************************************************')
print()

def es_mayor():
    n = int(input('Ingrese Cantidad de Numeros: '))
    if n <= 0:
        print(f'La cantidad de numeros debe ser mayor a 0')
        return              
    numeros = []
    for i in range(n):
      num = int(input(f'Ingrese {i + 1}: '))
      numeros.append(num)   #guarda el numero ingresado a una lista
    mayor = max(numeros)    #devuelve el numero mayor de la lista y lo deja en mayor
    print(f'El numero Mayor es: {mayor}')
    return mayor

es_mayor()


print()
print('************************************************************************************')
print('    Crear una funcion que dibuje un rectangulo de X filas y X columnas determinadas ')
print('    por el usuario                                                                  ')
print('************************************************************************************')
print()


def dibujar_un_rectangulo():
    filas = int(input('Ingrese Cantidad de Filas: '))
    columnas = int(input('Ingrese Cantidad de Columnas: '))
    lista = str('|' * columnas)
    ultima = columnas-4
    espacios = str(' ' * ultima)
    for i in range(filas):
        if i == 0 or i == filas-1:
            print('-' * columnas)
        else:
            print(lista[0],espacios,lista[columnas-1])

dibujar_un_rectangulo()


print()
print('*******************************************************************************')
print('    Crear una funcion que calcule el Factorial de un numero entero positivo    ')
print('*******************************************************************************')
print()

def factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial = factorial * i
    return factorial

numero = int(input('Ingrese Numeros: '))

print(f'El factorial de', numero, 'es igual a', factorial(numero))
