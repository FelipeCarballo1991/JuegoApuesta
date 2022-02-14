import random
from turtle import position

class Jugador:

    def __init__(self,puntos):
        self.cartas = []
        self.puntos = puntos
        self.apuesta = 0

    def cantidadCartasEnLaMano(self):
        return len(self.cartas)
    
    def ingresarApuesta(self):
        apuesta = int(input  ("Ingrese su apuesta:"))

        while apuesta >self.puntos or type(apuesta) != int:
            apuesta = int(input (f"ERROR: Tu dinero es {self.puntos} "))

        self.apuesta = apuesta

        #print(apuesta)
        #carta = random.choice(unMazo.baraja)
        #unMazo.quitarCarta(carta)
        #print(carta)       
    
    def puntosDisponibles(self):
        print (self.puntos)
    
    def mostrarMano(self):
        print (self.cartas)
    

    def tomarCarta(self,unMazo):
        carta = random.choice(unMazo.baraja)
        self.cartas.append(carta)
        unMazo.quitarCarta(carta)

    
    """
    def tirarCarta(self,unMazo,indice):
        if self.cantidadCartasEnLaMano() > 0:
           carta = self.cartas[indice]
           self.cartas.remove(carta)
           unMazo.descarte.append(carta)
        else:
            return "NO TENGO MAS CARTAS"
    """

    def tirarCarta(self,unMazo,indice):
        
        try:
           carta = self.cartas[indice]
           self.cartas.remove(carta)
           unMazo.descarte.append(carta)        
         
        except IndexError:
            return "NO TENGO MAS CARTAS"
    
    def resultado(self,unaCartaRival):
        resultado = ""
    
        self.cartas #LAS DEL JUGADOR
        #unaCartaRival
        listaAuxiliar= []
        for carta in self.cartas:
                
                #print (carta.palo)
                if (carta.palo == unaCartaRival.palo):
                     listaAuxiliar.append(carta)
                
        if len(listaAuxiliar) == 0:
            resultado = "PERDI"
        
        else:
            for carta in listaAuxiliar:
                if (carta.valor == 1):
                    resultado = "GANE"
                elif (unaCartaRival.valor == 1) or (carta.valor < unaCartaRival.valor): 
                    resultado = "PERDI"
                else:
                     resultado = "GANE"

        
        return resultado

class Carta:

    def __init__(self,valor,palo):
        self.valor = valor
        self.palo = palo
        self.carta = (self.valor,self.palo)
        #self.id = str(valor)+palo
        self.imagen ="imagenes/"+str(valor)+str(palo)+".png"

    def __repr__(self) -> tuple:
        return repr(self.carta) 


class Baraja:

    def __init__(self,valores,palos):
        self.valores = valores #tupla
        self.palos = palos #tupla
        self.baraja = [Carta(v,p) for p in self.palos for v in self.valores]
        self.descarte = []

    def __repr__(self) -> list:
        """
        Al realizar un print de este objeto retorna el mazo completo

        """        
        return repr(self.baraja)


    def cantCartasDescarte(self):
        return len(self.descarte)


    def mostrarBaraja(self):

        print((self.baraja))
        #print(len(self.baraja))
    
   
    def quitarCarta(self,unaCarta):
        self.baraja.remove(unaCarta)
        

    def mezclarBaraja(self):
        random.shuffle(self.baraja)


    def agregarComodines(self):
        self.baraja.append(((0,"Comodin1")))
        self.baraja.append((0,"Comodin2"))
    


        



#INSTANCIO EL MAZO
barajaEspañola = Baraja([1,2,3,4,5,6,7,10,11,12],["ORO","COPA","ESPADA","BASTO"])
barajaEspañola.mezclarBaraja()

#INSTANCIO EL JUGADOR
cacho = Jugador(100)
cacho.ingresarApuesta()

for i in range(4):
    cacho.tomarCarta(barajaEspañola)
#print(cacho.apuesta)

print(f"MANO DEL JUGADOR: {cacho.cartas}")

cartaRival = random.choice(barajaEspañola.baraja)
barajaEspañola.quitarCarta(cartaRival)

#PARA DEBUGGEAR
#print("BARAJA",barajaEspañola.baraja)


print(f"CARTA RIVAL: {cartaRival}")

print(cacho.resultado(cartaRival))





