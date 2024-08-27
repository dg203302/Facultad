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
    def mover(self,torre_seleccionada,posicion_destino):
        if torre_seleccionada==1:
            if self.__torre1.verificar_pila():
                print('torre vacia!')
            else:
                ficha_tope=self.__torre1.get_tope()
                if posicion_destino==2:
                    self.__torre2.insertar(ficha_tope)
                    self.__torre1.suprimir_tope()
                elif posicion_destino==3:
                    self.__torre3.insertar(ficha_tope)
                    self.__torre1.suprimir_tope()
        if torre_seleccionada==2:
            if self.__torre2.verificar_pila():
                print('torre vacia!')
            else:
                ficha_tope=self.__torre2.get_tope()
                if posicion_destino==1:
                    self.__torre1.insertar(ficha_tope)
                    self.__torre2.suprimir_tope()
                elif posicion_destino==3:
                    self.__torre3.insertar(ficha_tope)
                    self.__torre2.suprimir_tope()
        if torre_seleccionada==3:
            if self.__torre3.verificar_pila():
                print('torre vacia!')
            else:
                ficha_tope=self.__torre3.get_tope()
                if posicion_destino==1:
                    self.__torre1.insertar(ficha_tope)
                    self.__torre3.suprimir_tope()
                if posicion_destino==2:
                    self.__torre2.insertar(ficha_tope)
                    self.__torre3.suprimir_tope()
        self.mostrar_torres()
    def mostrar_torres(self):
        print('torre 1: ')
        self.__torre1.mostrar()
        print('torre 2:')
        self.__torre2.mostrar()
        print('torre 3:')
        self.__torre3.mostrar()
    def verificar(self):
        try:
            i=self.__dimension-1
            comparador=1
            while i>=0 and comparador<=self.__dimension:
                if self.__torre3.ubicar(i)!=comparador:
                    raise StopIteration
                comparador+=1
                i-=1
            return True
        except StopIteration:
            return False