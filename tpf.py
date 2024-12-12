
import pickle, sys, os, random

os.system("clear") #para limpiar depende la terminal que usen en sus sistema puede variar clear se utiliza en linux y cls creo que en windows

numero_random = random.randrange(1000, 9999) #con esto crean un numero random


"""
with open(guardar, "wb") as f:
        pickle.dump(ticket, f)
        
Con este comando van a generar y guardar el archivo
la palabra guardar es una variable que debe contener el nombre del archivo
la palabra ticket es una variable que contendra el diccionario (Objeto)

with open(abrir, "rb") as f:
        ticket = pickle.load(f)
        
similar a lo anterior, la palabra abrir contendra el nombre del archivo a abrir 
la palabra ticket es el diccionario donde se guardara ese objeto        
        
        """

"""  
os.path.isfile(ruta) # la palabra ruta obtendra el nombre del archivo y verificara que exista

sys.exit() #con este comando cierra la ejecucion del programa

"""
def menu_ticket():
    os.system("clear")
    print('    Hola bienvenido al sistema de Tickets ')
    print()
    print()
    print('1 - Generar un Nuevo Ticket')
    print('2 - Leer un Ticket')
    print('3 - Salir')
    print()
    opcion = int(input('Seleccione: '))
    print()
    return opcion


def ingreso_ticket():
    os.system("clear")
    print('Ingrese los datos para Generar un nuevo Ticket')
    nombre = input ('Ingrese su Nombre: ')
    sector = input ('Ingrese su Sector: ')
    asunto = input ('Ingrese Asunto: ')
    mensaje = input ('Ingrese un Mensaje: ')
    ticket = random.randrange(1000, 9999)
    diccionario_tickets = {
        'ticket': ticket,
        'nombre': nombre,
        'sector': sector,
        'asunto': asunto,
        'mensaje': mensaje
    }
    with open(str(ticket), "wb") as f:
        pickle.dump(diccionario_tickets, f)
    muestro_ticket(diccionario_tickets)


def muestro_ticket(diccionario_tickets):
    os.system("clear")
    print('=================================================')
    print('          Se genero el siguiente Ticket ')
    print('=================================================')
    print('    Su nombre: ', diccionario_tickets['nombre'], '    NºTicket: ', diccionario_tickets['ticket'])
    print('    Sector: ', diccionario_tickets['sector'])
    print('    Asunto: ', diccionario_tickets['asunto'])
    print()
    print('    Mensaje: ', diccionario_tickets['mensaje'])
    print()
    print('          Recordar su numero de Ticket ')
    print()


def regenerar():
    regenera = 'x'
    while regenera != 's' and regenera != 'n':
        opc = (input('Desea generar un nuevo Ticket? (s/n): '))
        regenera = opc.lower()
    return regenera


def leer_ticket():
    os.system("clear")
    numero_ticket = input('Ingrese ticket a consultar: ')
    with open(numero_ticket, "rb") as f:
        diccionario_tickets = pickle.load(f)
    muestro_ticket(diccionario_tickets)



opcion = menu_ticket()

while opcion != 3:
    if opcion == 1:
        ingreso_ticket()
        regenera = regenerar()
        if regenera == 'n':
            opcion = menu_ticket()
    if opcion == 2:
        leer_ticket()
        continuar = input('Dar enter para continuar')
        opcion = menu_ticket()
    if opcion == 3:
        confirma = 'x'
        while confirma != 's' and confirma != 'n':
            opc3 = input('El programa se cerrara, confirma? (s/n): ')
            confirma = opc3.lower()
            if confirma == 's':
              sys.exit()
            else:
                opcion = menu_ticket()
 
