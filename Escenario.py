import random
from Clases import Carta,Baraja,Jugador,Pozo
from module import cleaning

barajaEspañola = Baraja([1,2,3,4,5,6,7,10,11,12],["ORO","COPA","ESPADA","BASTO"])
barajaEspañola.mezclarBaraja()
barajaEspañola.mezclarBaraja()
barajaEspañola.mezclarBaraja()
print(f"Cartas: {barajaEspañola.baraja}")
pozo = Pozo()
cleaning()

# JUGADORES Y POZO INICIAL
jugador1= Jugador(pozo,100,"Pepe")
jugador2= Jugador(pozo,100,"Cacho")

jugador1.ingresarPozoBase(pozo)
#jugador2.ingresarPozoBase(pozo)

print(f"El Pozo inicial es: {pozo.pozo}")

#El primer jugador inicia la partida
jugador1.tomarCartas(4,barajaEspañola)
print(f"Mano del jugador1: {jugador1.cartas}")

jugador1.ingresarApuesta(pozo)
cartaRival = random.choice(barajaEspañola.baraja)
print(cartaRival)
print(jugador1.resultado(cartaRival,pozo))
print(f"Creditos del jugador1: {jugador1.credito}")
print(f"En el pozo queda: {pozo.pozo}")
jugador1.tirarCartas(barajaEspañola)
print(f"Mano del jugador1: {jugador1.cartas}")

print(f"Cartas descartadas: {barajaEspañola.descarte}")

print(f"Cartas que quedan para repartir en la proxima ronda: {barajaEspañola.baraja}")

