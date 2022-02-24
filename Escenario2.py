import random
from Clases import Carta,Baraja,Jugador,Pozo,Partida
from module import cleaning

barajaEspañola = Baraja([1,2,3,4,5,6,7,10,11,12],["ORO","COPA","ESPADA","BASTO"])
pozo = Pozo()
partida = Partida(2,barajaEspañola,pozo,["Pepe","Cacho"])

#print(partida.baraja)

listajugadores = partida.setearJugadores(pozo,100)

print(listajugadores)