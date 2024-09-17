#____________________________nodo________________________________________#
class nodo:
    __dato:object
    __izq:object
    __der:object
    def __init__(self,dato=None,izq=None,der=None):
        self.__dato=dato
        self.__izq=izq
        self.__der=der
    def get_dato(self):
        return self.__dato
    def get_izq(self):
        return self.__izq
    def get_der(self):
        return self.__der
    def set_izq(self,nodo):
        self.__izq=nodo
    def set_der(self,nodo):
        self.__der=nodo
#______________________________________ARBOL__________________________________________________________#
class arbol:
    __raiz:nodo
    def __init__(self,raiz=None):
        self.__raiz=raiz
    #carga
    def insertar(self,dato):
        if self.__raiz is None:
            self.__raiz=nodo(dato)
        else:
            self.insertar_recursivo(self.__raiz,dato)
    def insertar_recursivo(self,nodo_actual,dato):
        if dato>nodo_actual.get_dato():
            if nodo_actual.get_der() is None:
                nodo_actual.set_der(nodo(dato))
                print(f'nodo insertado: {nodo_actual.get_dato()}')
            else:
                self.insertar_recursivo(nodo_actual.get_der(),dato)
        elif dato<nodo_actual.get_dato():
            if nodo_actual.get_izq() is None:
                nodo_actual.set_izq(nodo(dato))
                print(f'nodo insertado: {nodo_actual.get_dato()}')
            else:
                self.insertar_recursivo(nodo_actual.get_izq(),dato)
        elif dato==nodo_actual.get_dato():
            print('ya esta ingresado el nodo!')
            raise ValueError
    def recorrer_en_orden(self):
        print(f'raiz: {self.__raiz.get_dato()}')
        self.recorrer_recursivo(self.__raiz)
    def recorrer_recursivo(self,nodo_actual):
        if nodo_actual is not None:
            self.recorrer_recursivo(nodo_actual.get_izq())
            print(nodo_actual.get_dato())
            self.recorrer_recursivo(nodo_actual.get_der())
    def recorrer_inverso(self):
        print(f'raiz: {self.__raiz.get_dato()}')
        self.recorrer_recursivo_inverso(self.__raiz)
    def recorrer_recursivo_inverso(self,nodo_actual):
        if nodo_actual is not None:
            self.recorrer_recursivo_inverso(nodo_actual.get_der())
            print(nodo_actual.get_dato())
            self.recorrer_recursivo_inverso(nodo_actual.get_izq())
    def buscar(self,valor):
        return self.buscar_recursivo(self.__raiz,valor)
    def buscar_recursivo(self,nodo_actual,valor):
        if nodo_actual is None or nodo_actual.get_dato()==valor:
            if nodo_actual is None:
                print('no se encontro el valor')
                return
            else:
                return nodo_actual
        else:
            if valor<nodo_actual.get_dato():
                return self.buscar_recursivo(nodo_actual.get_izq(),valor)
            else:
                return self.buscar_recursivo(nodo_actual.get_der(),valor)
if __name__=="__main__":
    mi_arbol=arbol()
    nodos=[15, 10, 20, 8, 12, 17, 25, 6, 11, 16]
    for valor in nodos:
        mi_arbol.insertar(valor)
    mi_arbol.recorrer_inverso()

    valor=int(input('ingrese el valor a buscar: '))
    nodo_buscado=mi_arbol.buscar(valor)
    if nodo_buscado is not None:
        print(f'el valor {nodo_buscado.get_dato()} fue encontrado')