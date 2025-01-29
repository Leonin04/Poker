from Baraja import Baraja  
from Cartas import Carta
from Mano import Mano
from Funciones import ComprobarGanador, SeguirJugando, SetFichas

baraja = Baraja()
miMano = Mano()
manoCPU = Mano()
Mesa = Mano()
respuesta = ""

miMano.inicializar(baraja)
manoCPU.inicializar(baraja)
Mesa.inicializar(baraja,1)

while respuesta != "r":
    respuesta = SeguirJugando(Mesa,miMano, baraja)
    if respuesta == "a":
        miMano.aumentarApuesta()
print("\nLas cartas de la CPU son:")
print(manoCPU)
manoCPU.comprobarMano(Mesa)
print("La mano de la CPU es: ", manoCPU.getMano(),"\tPuntuación: ", manoCPU.getPuntuacion())

print("\n",ComprobarGanador(miMano,manoCPU))
