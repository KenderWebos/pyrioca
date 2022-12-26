import time
import random
import os

cantJugadores = 2
cantCartasInicial = 6
    
mazo = []
#1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "j", "q", "k", "joker"

for j in range(10):
    mazo.append(str("p_"+ str(j+1)))
mazo.append("p_j")
mazo.append("p_q")
mazo.append("p_k")

for j in range(10):
    mazo.append(str("c_"+ str(j+1)))
mazo.append("c_j")
mazo.append("c_q")
mazo.append("c_k")

for j in range(10):
    mazo.append(str("t_"+ str(j+1)))
mazo.append("t_j")
mazo.append("t_q")
mazo.append("t_k")

for j in range(10):
    mazo.append(str("d_"+ str(j+1)))
mazo.append("d_j")
mazo.append("d_q")
mazo.append("d_k")

# for e in mazo:
#     mazo.append( e )

print(mazo)

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

