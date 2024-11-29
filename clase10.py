
print()
print('***********************************************************************************')
print('    Crea una tupla con los meses del año, pide números al usuario, si el numero    ')
print('    esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa     ')
print('    posición sino muestra un mensaje de error. El programa termina cuando el       ')
print('    usuario introduce un cero.                                                     ')
print('***********************************************************************************')
print()

meses_año = ('Enero', 'Febrero', 'Marzo', 'Abril', ' Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
print(len(meses_año))
mes = int(input('Ingrese Mes a Consultar: '))
while mes != 0:    
    if mes > len(meses_año):
        print(f'Debe ingresar un numero <=', len(meses_año))
    else:
        posicion = mes -1
        print(f'mes:', mes, meses_año[posicion])
    mes = int(input('Ingrese Mes a Consultar: '))
print(f'Se terminaron las consultas...')

print()
print('***********************************************************************************')
print('    Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos  ')
print('    de insertar. Por último, muestra los números ordenados de menor a mayor.       ')
print('***********************************************************************************')
print()

numero = int(input('Ingrese Número: '))
lista_numeros = []
while numero != 0:
    lista_numeros.append(numero)
    numero = int(input('Ingrese Número: '))
lista_numeros.sort()
print(lista_numeros)

print()
print('*******************************************************************************')
print('    Crea una tupla con números, pide un numero por teclado e indica cuantas    ')
print('    veces se repite.                                                           ')
print('*******************************************************************************')
print()

tupla = (1300,300,450,1,2,3,3,6,99,300)
print(tupla)
numero = int(input('Ingrese Número: '))
print(f'El numero', numero, 'se repite', tupla.count(numero),'veces')


print()
print('*********************************************************************************')
print('    Vamos a crear un programa en python donde vamos a declarar un diccionario    ')
print('    para guardar los precios de las distintas frutas. El programa pedirá el      ')
print('    nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio  ')
print('    final de la fruta a partir de los datos guardados en el diccionario.         ')
print('*********************************************************************************')
print()

catalogo_frutas = {
    'manzanas':2500.5,
    'peras':1765.55,
    'bananas':1999.99
}
print(catalogo_frutas.items())
valor = 0
fruta = input ('Ingrese Fruta: ')
cantidad = int(input('Ingrese Cantidad: '))
for i, x in catalogo_frutas.items():
    if i == fruta:
        print(i,x)
        valor = x * cantidad
        print(f'Por', cantidad, 'kg de', i, 'Usted Pagará: $', valor)
if valor == 0:
    print(f'No Existe Fruta', fruta, 'en el Catalogo')
