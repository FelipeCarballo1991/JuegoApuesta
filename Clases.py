import random
#from turtle import position

from module import cleaning,animacionMazo

class Pozo:

    def __init__(self):
        self.pozo = 0

    #def valorPozo(self):
    #    return self.pozo


class Jugador:

    def __init__(self,unPozo,credito):
        self.cartas = []
        self.puntos = unPozo.pozo
        self.credito = credito
        self.apuesta = 0


    def cantidadCartasEnLaMano(self):
        return len(self.cartas)
    
    def ingresarApuesta(self,unPozo):
        apuesta = int(input  ("Ingrese su apuesta:"))

        while apuesta >unPozo.pozo or type(apuesta) != int:
            apuesta = int(input (f"ERROR: El pozo es {unPozo.pozo} "))

        self.apuesta = apuesta
        #unPozo.pozo -= self.apuesta

        
    def ingresarPozoBase(self,unPozo):
        #pozoJugador = int(input  ("Ingrese un valor inicial en el pozo:"))

        #while pozoJugador <=0:
        #    pozoJugador = int(input (f"ERROR:Se debe ingresar un valor positivo "))

        unPozo.pozo += self.credito
            
    
    def puntosDisponibles(self):
        print (self.puntos)
    
    def mostrarMano(self):
        print (self.cartas)
    

    def tomarCarta(self,unMazo):
        carta = random.choice(unMazo.baraja)
        self.cartas.append(carta)
        unMazo.quitarCarta(carta)

    def tomarCartas(self,unNumero,unMazo):
        for i in range(unNumero):
            self.tomarCarta(unMazo)


    def tirarCarta(self,unMazo,indice):
        
        try:
           carta = self.cartas[indice]
           self.cartas.remove(carta)
           unMazo.descarte.append(carta)        
         
        except IndexError:
            return "NO TENGO MAS CARTAS"
    
    def tirarCartas(self,unMazo):
        for carta in self.cartas:            
            unMazo.descarte.append(carta)  
        
        self.cartas = []

    def resultado(self,unaCartaRival,unPozo):
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
            self.credito-= self.apuesta
            unPozo.pozo += self.apuesta
        
        else:
            for carta in listaAuxiliar:
                if (carta.valor == 1):
                    resultado = "GANE"
                    self.credito+= self.apuesta
                    unPozo.pozo -= self.apuesta
                elif (unaCartaRival.valor == 1) or (carta.valor < unaCartaRival.valor): 
                    resultado = "PERDI"
                    self.credito-= self.apuesta
                    unPozo.pozo += self.apuesta
                else:
                     resultado = "GANE"
                     self.credito+= self.apuesta
                     unPozo.pozo -= self.apuesta

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
    
"""
#INSTANCIO EL MAZO
barajaEspañola = Baraja([1,2,3,4,5,6,7,10,11,12],["ORO","COPA","ESPADA","BASTO"])
pozo = Pozo()
cleaning()
#animacionMazo()

barajaEspañola.mezclarBaraja()


#INSTANCIO EL JUGADOR
cacho = Jugador(100)
print(cacho.puntos)
cacho.ingresarApuesta()

for i in range(4):
    cacho.tomarCarta(barajaEspañola)
print(cacho.apuesta)

print(f"MANO DEL JUGADOR: {cacho.cartas}")

cartaRival = random.choice(barajaEspañola.baraja)
barajaEspañola.quitarCarta(cartaRival)

#PARA DEBUGGEAR
#print("BARAJA",barajaEspañola.baraja)


print(f"CARTA RIVAL: {cartaRival}")



print(cacho.resultado(cartaRival))


if cacho.resultado(cartaRival) == "PERDI":

    cacho.puntos -= cacho.apuesta
else:
    cacho.puntos +=  cacho.apuesta

print(cacho.puntos)

"""