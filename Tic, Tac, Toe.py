

#Comenzamos definiendo unas variables globales que nos ayudaran a lo largo de nuestro codigo

simbolo_jugador = "X"

Juego_En_Proceso = True

ganador = None

tablero = ['-', '-', '-',

'-', '-', '-',

'-', '-', '-']


#Creamos una funcion para mostrar el tablero, esta funcion en vez de quiarse por las coordenadas como (0,0),(0,1) y mas asi

#Esta creado para que eel tablero este dividido en 8 espacios (desde el 0 hasta el 8 porque esta escrito en python)


def Mostrar_tablero(tablero):

print(tablero[0] + " | " + tablero[1] + " | " + tablero[2])

print("-" * 9)

print(tablero[3] + " | " + tablero[4] + " | " + tablero[5])

print("-" * 9)

print(tablero[6] + " | " + tablero[7] + " | " + tablero[8])


#Dentro de esta funcion, modificaremos el tablero segun la posicion que el usuario introduzca

#Y tambien nos aseguramos que eliga bien una posicion del uno al nueve (del 0 al 8 en la funcion anterior)

#Y si introduce una jugada no valida o es una posicion en la que ya hay un jugador, el jugador podra intentar de nuevo 

def Movida_jugador(tablero):

mov = int(input("Introduzca un numero para colocar su jugada [1-9]: "))

if mov >= 1 and mov <= 9 and tablero[mov-1]== "-":

tablero[mov-1] = simbolo_jugador

else:

print("Esa jugada no es valida o ya hay un jugador en esa posicion, intente de nuevo")


#En esta funcion nos aseguramos que el programa lea si hay tres simbolos iguales en cada fila para definir un ganador

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


#En esta funcion nos aseguramos que el programa lea si hay tres simbolos iguales en cada columna para definir un ganador

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


#En esta funcion nos aseguramos que el programa lea si hay tres simbolos iguales en cada diagonal para definir un ganador

def GanarDiagonal(tablero):

global ganador

if tablero[0] == tablero[4] == tablero[8] and tablero[0] != "-":

ganador = tablero [0]

return True

elif tablero[2] == tablero[4] == tablero[6] and tablero[2] != "-":

ganador = tablero [2]

return True 


#Dentro de esta funcion podemos saber si el juego quedo en un empate

#Al no tener ninguna opcion para colocar mas simbolos, el programa indicara que es un empate y el juego en proceso sera culminado

def IdentificarEmpate(tablero):

global Juego_En_Proceso

if "-" not in tablero:

Mostrar_tablero(tablero)

print("Es un empate!, si que son malos jugando")

Juego_En_Proceso = False


#Dentro de esta funcion definimos el ganador utilizando un if

#Si el jugador gano en horizontal, vertical o diagonal, la variable global del juego en proceso pasa a ser falsa y el juego es terminado

#Y el programa indica cual fue la ficha ganadora

def IdentificarGanador():

if GanarHorizontal(tablero) or GanarVertical(tablero) or GanarDiagonal(tablero):

global Juego_En_Proceso

print("El ganador es: ", ganador)

Juego_En_Proceso = False


#Dentro de esta funcion se realiza el cambio de jugador en cada turno

def CambioDeJugador(): 

global simbolo_jugador

if simbolo_jugador == "X":

print("Es el turno de la O! ")

simbolo_jugador = "O"

else:

print("Es el turno de la X! ")

simbolo_jugador = "X"


#Este es el programa principal, el cual esta ordenado especificamente para que todo funcione correctamente

#Mientras el juego en proceso sea verdadero, todas las funciones seran aplicadas

#Comenzamos imprimiendo el tablero, despues se introduce la jugada del jugador en la posicion que coloco

#Posteriormente identificamos si la jugada que realizo el jugador conllevo a un juego ganado o a un empate

#Y por ultimo cambiamos de jugador despues de realizar la jugada

while Juego_En_Proceso:

print (Mostrar_tablero(tablero))

print (Movida_jugador(tablero))

IdentificarGanador()

IdentificarEmpate(tablero)

CambioDeJugador() 



