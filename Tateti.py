
tablero = [' ']*9
final = False
turno_x = True

def print_tablero(tablero):
     for i in range(0,7,3):
          print(tablero[i] + '|' + tablero[i+1] + '|' + tablero[i+2])

while not final:
    jugada = False
    while not jugada:
        try:
            print()
            if turno_x:
                posicion = int(input('Turno Jugador 1 (1-9): '))
            else:
                posicion = int(input('Turno Jugador 2 (1-9): '))
            if tablero[posicion - 1] == ' ':
                 jugada = True
            else:
                 print('Jugada ya Ingresada, Reintente')
        except:
            print('Ingreso un Valor Erroneo, Reintente')
    
    if turno_x:
        tablero[posicion - 1] = 'X'
    else:
        tablero[posicion - 1] = 'O'
    
    print_tablero(tablero)

    if (tablero[0] == tablero[1] == tablero[2] == tablero[0] != ' ' or
        tablero[3] == tablero[4] == tablero[5] == tablero[3] != ' ' or
        tablero[6] == tablero[7] == tablero[8] == tablero[6] != ' ' or
        tablero[0] == tablero[3] == tablero[6] == tablero[0] != ' ' or
        tablero[1] == tablero[4] == tablero[7] == tablero[1] != ' ' or
        tablero[2] == tablero[5] == tablero[8] == tablero[2] != ' ' or
        tablero[0] == tablero[4] == tablero[8] == tablero[0] != ' ' or
        tablero[2] == tablero[4] == tablero[6] == tablero[2] != ' '):
         print()
         if turno_x:
            print('***** El ganador es el Jugador 1')
         else:
            print('***** El ganador es el Jugador 2')
         final = True
    else:
        if ' ' not in tablero:
            print('***** No Hubo Ganador... Fue Empate!!')
            final = True
        else:
            if turno_x:
                turno_x = False
            else:
                turno_x = True

    