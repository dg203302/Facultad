from pilas import pila_secuencial
class hanoi:
    __torre1:pila_secuencial
    __torre2:pila_secuencial
    __torre3:pila_secuencial
    __dimension:int
    def __init__(self, dimension):
        self.__dimension=dimension
        self.__torre1=pila_secuencial(self.__dimension)
        self.__torre2=pila_secuencial(self.__dimension)
        self.__torre3=pila_secuencial(self.__dimension)
    def inicio(self):
        for i in range(self.__dimension, 0,-1):
            self.__torre1.insertar(i)
        print('torre 1: ')
        self.__torre1.mostrar()
        print('torre 2:')
        self.__torre2.mostrar()
        print('torre 3:')
        self.__torre3.mostrar()
    def mover(self,torre_seleccionada,torre_destino):
        if torre_seleccionada==1:
            if self.__torre1.verificar_pila():
                print('torre vacia!')
            else:
                ficha_tope=self.__torre1.get_tope()
                if posicion_destino==2:
                    if ficha_tope>self.__torre2.get_tope():
                        self.__torre2.insertar(ficha_tope)
                        self.__torre1.suprimir_tope()
                elif posicion_destino==3:
                    if ficha_tope>self.__torre3.get_tope():
                        self.__torre3.insertar(ficha_tope)
                        self.__torre1.suprimir_tope()
        if torre_seleccionada==2:
            if self.__torre2.verificar_pila():
                print('torre vacia!')
            else:
                ficha_tope=self.__torre2.get_tope()
                if posicion_destino==1:
                    if ficha_tope>self.__torre1.get_tope():
                        self.__torre1.insertar(ficha_tope)
                        self.__torre2.suprimir_tope()
                elif posicion_destino==3:
                    if ficha_tope>self.__torre3.get_tope():
                        self.__torre3.insertar(ficha_tope)
                        self.__torre2.suprimir_tope()
        if torre_seleccionada==3:
            if self.__torre3.verificar_pila():
                print('torre vacia!')
            else:
                ficha_tope=self.__torre3.get_tope()
                if posicion_destino==1:
                    if ficha_tope>self.__torre1.get_tope():
                        self.__torre1.insertar(ficha_tope)
                        self.__torre3.suprimir_tope()
                if posicion_destino==2:
                    if ficha_tope>self.__torre2.get_tope():
                        self.__torre2.insertar(ficha_tope)
                        self.__torre3.suprimir_tope()
    def mostrar_torres_prueba(self):
        print('torre 1: ')
        self.__torre1.mostrar()
        print('torre 2:')
        self.__torre2.mostrar()
        print('torre 3:')
        self.__torre3.mostrar()
dimension=int(input('ingrese la cantidad de fichas: '))
torre_hanoi=hanoi(dimension)
torre_hanoi.inicio()
posicion_inicio=int(input('ingrese la torre de inicio: '))
posicion_destino=int(input('ingrese la torre de destino: '))
torre_hanoi.mover(posicion_inicio,posicion_destino)
torre_hanoi.mostrar_torres_prueba()
