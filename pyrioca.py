import time
import random
import os

cantJugadores = 2
cantCartasInicial = 6

mazo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "j", "q", "k", "joker"]
mazoDescarte = []
random.shuffle(mazo)

mazoJ1 = []
mazoJ2 = []

def sacarCartaDelMazo(mazoPrincipal, mazoSecundario):
    mazoSecundario.append(mazoPrincipal.pop(random.randint(0, len(mazoPrincipal)-1)))

def repartirCartas():
    print("revolviendo cartas...")
    for i in range(cantCartasInicial):
        sacarCartaDelMazo(mazo, mazoJ1)
        sacarCartaDelMazo(mazo, mazoJ2)

    sacarCartaDelMazo(mazo, mazoDescarte)
    print("agregando carta inicial...")
    print("cartas revueltas, iniciando juego")
    print(f"---------------------------------" )

def printUI(player):
    if player == 0:
        print(f"BIENVENIDOS AL JUEGO DE CARIOCA!!" )
        print(f"---------------------------------" )

    elif player == 1:
        print(f"MazoDescarte:{mazoDescarte}" )
        print(f"MazoJ1: {mazoJ1}" )
    elif player == 2:
        print(f"MazoDescarte:{mazoDescarte}" )
        print(f"MazoJ2: {mazoJ2}" )

def printData(player):
    if player == 0:
        print(f"MazoPrincipal:{mazo}" )
        print(f"MazoDescarte:{mazoDescarte}" )
        print(f"MazoJ1: {mazoJ1}" )
        print(f"MazoJ2: {mazoJ2}" )
    elif player == 1:
        print(f"MazoDescarte:{mazoDescarte}" )
        print(f"MazoJ1: {mazoJ1}" )
    elif player == 2:
        print(f"MazoDescarte:{mazoDescarte}" )
        print(f"MazoJ2: {mazoJ2}" )

printUI(0)
repartirCartas()
printData(0)


