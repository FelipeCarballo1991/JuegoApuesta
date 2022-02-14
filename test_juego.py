from Clases import Jugador

def test_seteoPuntosJugador():

   cacho = Jugador(100)


   assert cacho.puntos == 100

"""
def test_ingresoApuestaJugador():

    ...
    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    #monkeypatch.setattr('builtins.input', lambda _: 80)
    #cacho = Jugador(100)

    # go about using input() like you normally would:

    #cacho.ingresarApuesta()

    #assert cacho.apuesta == 80
    #i = input("What is your name?")
    #assert i == "Mark"
"""