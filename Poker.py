from Baraja import Baraja  
from Cartas import Carta
from Mano import Mano
from Funciones import ComprobarGanador, SeguirJugando

FICHAS = input("Introduce el número de fichas con las que quieres comenzar: ")
ronda=0

baraja = Baraja()
miMano = Mano(FICHAS)
manoCPU = Mano(FICHAS)
Mesa = Mano()
respuesta=["s",0]

miMano.inicializar(baraja)
manoCPU.inicializar(baraja)
Mesa.inicializar(baraja,1)

while respuesta[0] != "r" and len(Mesa.getCartas()) < 5:
    respuesta = SeguirJugando(Mesa,miMano, baraja,ronda)
    if respuesta[0] == "a":
        miMano.aumentarApuesta(respuesta[1])

ronda += 1

print("\nLas cartas de la CPU son:")
print(manoCPU)
manoCPU.comprobarMano(Mesa)
print("La mano de la CPU es: ", manoCPU.getMano(),"\tPuntuación: ", manoCPU.getPuntuacion())

print("\n",ComprobarGanador(miMano,manoCPU))
