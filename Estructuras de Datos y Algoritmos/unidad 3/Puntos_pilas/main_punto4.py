from punto_4 import *
dimension=int(input('ingrese la cantidad de fichas: '))
torre_hanoi=hanoi(dimension)
torre_hanoi.inicio()
while True:
    posicion_inicio=int(input('ingrese la torre de inicio: '))
    posicion_destino=int(input('ingrese la torre de destino: '))
    torre_hanoi.mover(posicion_inicio,posicion_destino)
    if torre_hanoi.verificar()==True:
        break