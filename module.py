import os
import sys
from time import sleep

def cleaning():

    """
    Limpia la consola de comandos

    """
    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('linux'):
        os.system('clear')


def animacionMazo(debug = False):
    if debug:
        ...
    else:

        print("Mezclando baraja .")
        sleep(1)
        cleaning()
        print("Mezclando baraja ..")
        sleep(1)
        cleaning()
        print("Mezclando baraja ...")
        sleep(1)
        cleaning()
        print("Mezclando baraja ..")
        sleep(1)
        cleaning()
        print("Mezclando baraja .")
        sleep(1)
        cleaning()
        print("Mazo mezclado")
        sleep(1)