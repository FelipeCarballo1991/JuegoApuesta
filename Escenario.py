from Clases import Carta,Baraja,Jugador,Pozo
from module import cleaning


barajaEspañola = Baraja([1,2,3,4,5,6,7,10,11,12],["ORO","COPA","ESPADA","BASTO"])
pozo = Pozo()
cleaning()


jugador1= Jugador(pozo,100)
jugador2= Jugador(pozo,100)

jugador1.ingresarPozoBase(pozo)
jugador2.ingresarPozoBase(pozo)

print(f"El Pozo inicial es: {pozo.pozo}")

jugador1.ingresarApuesta(pozo)
jugador2.ingresarApuesta(pozo)