from Baraja import Baraja  
from Cartas import Carta
from Mano import Mano
from Funciones import ComprobarGanador
import os

baraja = Baraja()
miMano = Mano()
manoCPU = Mano()
Mesa = Mano()
miMano.inicializar(baraja)
manoCPU.inicializar(baraja)
Mesa.inicializar(baraja,1)

respuesta = 's'
while respuesta == 's' and len(Mesa.cartas) < 5: 
    os.system('cls' if os.name == 'nt' else 'clear')
    Mesa.pedirCarta(baraja)
    print("Tus cartas son:")
    print(miMano)
    print("Las cartas de la mesa son:")
    print(Mesa)
    miMano.comprobarMano(Mesa)
    print("Tu mano es: ", miMano.getMano(), "\tPuntuación: ", miMano.getPuntuacion())
    respuesta = input("¿Quieres otra carta? (s/n): ")

print("\nLas cartas de la CPU son:")
print(manoCPU)
manoCPU.comprobarMano(Mesa)
print("La mano de la CPU es: ", manoCPU.getMano(),"\tPuntuación: ", manoCPU.getPuntuacion())

print("\n",ComprobarGanador(miMano,manoCPU))
