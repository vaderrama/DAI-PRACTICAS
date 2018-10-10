#!/usr/bin/env python3

from random import randint 

valorClave = randint(1,100)
valorEntrada = -1

while valorClave != valorEntrada:
        print ( ' Introduce un numero ' )
        valorEntrada = int(input())

        if valorClave > valorEntrada:

            print ( ' El numero buscado es mayor ')

        elif valorClave < valorEntrada :

            print ( ' El numero buscado es menor ')

        elif valorClave == valorEntrada :

            print ( ' Enhorabuena ! Has acertado el numero ')

            



