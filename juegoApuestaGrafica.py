from cProfile import label
from cgitb import text
from email.policy import default
import random
# import tkinter

from tkinter import *
#from typing import NoReturn
 

raiz = Tk()

nro_cartas = [1,2,3,4,5,6,7,10,11,12]
palos = ['OROS', 'COPAS', 'BASTOS', 'ESPADAS']

mazo = [(p, c) for p in palos for c in nro_cartas]


    
cartaJugador = random.choice(mazo)

cartaRival = random.choice(mazo)

puntosDisponibles = 100

pozo = 100


raiz.geometry("650x350")
raiz.config(bg="green")

miFrame = Frame(raiz, width=500, height=400)

miFrame.pack()

miImagen=PhotoImage(file="C:/Users/Lautaro/Desktop/ppagm/curso/cartasespanolas/"+ str(cartaJugador[1]) + str(cartaJugador[0]) +".png")
miImagen2=PhotoImage(file="C:/Users/Lautaro/Desktop/ppagm/curso/cartasespanolas/"+ str(cartaJugador[1]) + str(cartaJugador[0]) +".png")
miImagen3=PhotoImage(file="C:/Users/Lautaro/Desktop/ppagm/curso/cartasespanolas/"+ str(cartaJugador[1]) + str(cartaJugador[0]) +".png")
miImagen4=PhotoImage(file="C:/Users/Lautaro/Desktop/ppagm/curso/cartasespanolas/"+ str(cartaJugador[1]) + str(cartaJugador[0]) +".png")

# C:\Users\Lautaro\Desktop\ppagm\curso\

# print(miImagen)

# Label(miFrame, text="CartasJugador1", fg="black").place(x=50 , y=50)
Label(miFrame, image=miImagen).place(x=50 , y=50)
Label(miFrame, image=miImagen2).place(x=100 , y=50)
Label(miFrame, image=miImagen3).place(x=150 , y=50)
Label(miFrame, image=miImagen4).place(x=200 , y=50)

Label(miFrame, text="TUS CARTAS: ").place(x=50 , y=30)

Label(miFrame, text="CARTA DEL MAZO: ").place(x=300 , y=30)


Label(miFrame, text="POZO: "+ str(pozo) , fg="black").place(x=30 , y=130)
Label(miFrame, text="PUNTOS DISPONIBLES: "+ str(puntosDisponibles) , fg="black").place(x=30 , y=150)
Label(miFrame, text="APUESTA: " , fg="black").place(x=30 , y=170)


puntosDisponiblesGrafica = puntosDisponibles

cuadroTexto = Entry(miFrame)
cuadroTexto.place(x=90, y=170)


#  cuadroTexto.get()


def procesoApuesta():
    apuestaGrafica =   100    
    while apuestaGrafica > puntosDisponiblesGrafica:
        apuestaGrafica = int(input(f"Podes apostar hasta {puntosDisponiblesGrafica}. Cantidad a apostar: "))

    if cartaJugador[0] != cartaRival[0]:
        print("PERDI")
        pozo += int(apuestaGrafica)
        puntosDisponiblesGrafica -= int(apuestaGrafica)
    elif cartaJugador[1] == 1:
        print("GANE")
        puntosDisponiblesGrafica += int(apuestaGrafica)
        pozo -= int(apuestaGrafica)
    elif cartaJugador[1] > cartaRival[1] and cartaRival[1] != 1:
        print("GANE")
        puntosDisponiblesGrafica = puntosDisponiblesGrafica + int(apuestaGrafica)
        pozo -= int(apuestaGrafica)
    else:
        print("PERDÍ")
        pozo = pozo + int(apuestaGrafica)
        puntosDisponibles -= int(apuestaGrafica)

# Label(miFrame, text="POZO: "+ str(pozo) , fg="black").place(x=30 , y=130)
# Label(miFrame, text="PUNTOS DISPONIBLES: "+ str(puntosDisponiblesGrafica) , fg="black").place(x=30 , y=150)
# Label(miFrame, text="APUESTA: " , fg="black").place(x=30 , y=170)

    
print(f"POZO: {pozo}")
print(f"Tenes para apostar: {puntosDisponibles}")


botonApostar = Button(miFrame, text="APOSTAR", command=procesoApuesta).place(x=100 , y=210)

puntosDisponibles = 100

pozo = 100

print(f"POZO: {pozo}")
print(f"Tenes para apostar: {puntosDisponibles}")

print("Tu carta es: " , cartaJugador)

apuesta = int(input("Cantidad a apostar: "))

while apuesta > puntosDisponibles:
    apuesta = int(input(f"Podes apostar hasta {puntosDisponibles}. Cantidad a apostar: "))
        

    
    
print(cartaRival)

if cartaJugador[0] != cartaRival[0]:
    print("PERDI")
    pozo += apuesta
    puntosDisponibles -= apuesta
elif cartaJugador[1] == 1:
    print("GANE")
    puntosDisponibles += apuesta
    pozo -= apuesta
elif cartaJugador[1] > cartaRival[1] and cartaRival[1] != 1:
    print("GANE")
    puntosDisponibles = puntosDisponibles + apuesta
    pozo -= apuesta
else:
    print("PERDÍ")
    pozo = pozo + apuesta
    puntosDisponibles -= apuesta

    
    print(f"POZO: {pozo}")
    print(f"Tenes para apostar: {puntosDisponibles}")


raiz.mainloop()
