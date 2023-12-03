simbolo_jugador = "X"

Juego_En_Proceso = True

ganador = None

tablero = ['-', '-', '-',

'-', '-', '-',

'-', '-', '-']


def Mostrar_tablero(tablero):

print(tablero[0] + " | " + tablero[1] + " | " + tablero[2])

print("-" * 9)

print(tablero[3] + " | " + tablero[4] + " | " + tablero[5])

print("-" * 9)

print(tablero[6] + " | " + tablero[7] + " | " + tablero[8])

def Movida_jugador(tablero):

mov = int(input("Introduzca un numero para colocar su jugada [1-9]: "))

if mov >= 1 and mov <= 9 and tablero[mov-1]== "-":

tablero[mov-1] = simbolo_jugador

else:

print("Esa jugada no es valida o ya hay un jugador en esa posicion, intente de nuevo")


def GanarHorizontal(tablero):

global ganador

if tablero[0] == tablero[1] == tablero[2] and tablero[0] != "-":

ganador = tablero[0]

return True

elif tablero[3] == tablero[4] == tablero[5] and tablero[3] != "-":

ganador = tablero[3]

return True

elif tablero[6] == tablero[7] == tablero[8] and tablero[6] != "-":

ganador = tablero[6]

return True


def GanarVertical(tablero):

global ganador

if tablero[0] == tablero[3] == tablero[6] and tablero[0] != "-":

ganador = tablero[0]

return True

elif tablero[1] == tablero[4] == tablero[7] and tablero[1] != "-":

ganador = tablero[1]

return True

elif tablero[2] == tablero[5] == tablero[8] and tablero[2] != "-":

ganador = tablero[2]

return True


def GanarDiagonal(tablero):

global ganador

if tablero[0] == tablero[4] == tablero[8] and tablero[0] != "-":

ganador = tablero [0]

return True

elif tablero[2] == tablero[4] == tablero[6] and tablero[2] != "-":

ganador = tablero [2]

return True 


def IdentificarEmpate(tablero):

global Juego_En_Proceso

if "-" not in tablero:

Mostrar_tablero(tablero)

print("Es un empate!, si que son malos jugando")

Juego_En_Proceso = False


def IdentificarGanador():

if GanarHorizontal(tablero) or GanarVertical(tablero) or GanarDiagonal(tablero):

global Juego_En_Proceso

print("El ganador es: ", ganador)

Juego_En_Proceso = False


def CambioDeJugador(): 

global simbolo_jugador

if simbolo_jugador == "X":

print("Es el turno de la O! ")

simbolo_jugador = "O"

else:

print("Es el turno de la X! ")

simbolo_jugador = "X"



while Juego_En_Proceso:

print (Mostrar_tablero(tablero))

print (Movida_jugador(tablero))

IdentificarGanador()

IdentificarEmpate(tablero)

CambioDeJugador() 


