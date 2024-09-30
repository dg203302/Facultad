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
    def set_dato(self,dato):
        self.__dato=dato
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
#----------------------------------------------------------------------------------------#
    def insertar(self,dato):
        if self.__raiz is None:
            self.__raiz=nodo(dato)
        else:
            self.insertar_recursivo(self.__raiz,dato)
    def insertar_recursivo(self,nodo_actual,dato):
        if dato>nodo_actual.get_dato():
            if nodo_actual.get_der() is None:
                nodo_actual.set_der(nodo(dato))
                #print(f'nodo insertado: {nodo_actual.get_dato()}')
            else:
                self.insertar_recursivo(nodo_actual.get_der(),dato)
        elif dato<nodo_actual.get_dato():
            if nodo_actual.get_izq() is None:
                nodo_actual.set_izq(nodo(dato))
                #print(f'nodo insertado: {nodo_actual.get_dato()}')
            else:
                self.insertar_recursivo(nodo_actual.get_izq(),dato)
        elif dato==nodo_actual.get_dato():
            print('ya esta ingresado el nodo!')
            raise ValueError
#-----------------------------------------------------------------------------------------#
    def recorrer_en_orden(self):
        print(f'raiz: {self.__raiz.get_dato()}')
        self.recorrer_recursivo(self.__raiz)
    def recorrer_recursivo(self,nodo_actual):
        if nodo_actual is not None:
            self.recorrer_recursivo(nodo_actual.get_izq())
            print(f'nodo actual: {nodo_actual.get_dato()}')
            self.recorrer_recursivo(nodo_actual.get_der())
#-----------------------------------------------------------------------------------------#
    def recorrer_inverso(self):
        print(f'raiz: {self.__raiz.get_dato()}')
        self.recorrer_recursivo_inverso(self.__raiz)
    def recorrer_recursivo_inverso(self,nodo_actual):
        if nodo_actual is not None:
            self.recorrer_recursivo_inverso(nodo_actual.get_der())
            print(f'nodo actual: {nodo_actual.get_dato()}')
            self.recorrer_recursivo_inverso(nodo_actual.get_izq())
#-----------------------------------------------------------------------------------------#
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
#------------------------------------------------------------------------------------------#
    def eliminar(self,valor):
        self.eliminar_recursivo(self.__raiz,valor)
    def eliminar_recursivo(self,nodo_actual,valor):
        if nodo_actual is None:
            print('no se encontro el valor')
            return None
        elif valor<nodo_actual.get_dato():
            nodo_actual.set_izq(self.eliminar_recursivo(nodo_actual.get_izq(),valor))
        elif valor>nodo_actual.get_dato():
            nodo_actual.set_der(self.eliminar_recursivo(nodo_actual.get_der(),valor))
        else:
            if nodo_actual.get_izq() is None:      #si tiene un hijo derecho
                return nodo_actual.get_der()
            elif nodo_actual.get_der() is None:    #si tiene un hijo izquierdo
                return nodo_actual.get_izq()
            else:    #si tiene dos hijos
                nodo_temporal=self.valor_minimo_nodo(nodo_actual.get_der())
                nodo_actual.set_dato(nodo_temporal.get_dato())             #asigna el valor del menor en el nodo encontrado
                nodo_actual.set_der(self.eliminar_recursivo(nodo_actual.get_der(),nodo_temporal.get_dato()))    #elimina el valor del menor de donde estaba orinalmente
        return nodo_actual
    def valor_minimo_nodo(self,nodo):
        while nodo.get_izq() is not None:
            nodo=nodo.get_izq()
        return nodo
#------------------------------------------------------------------------------------------#
    def get_altura(self):
        return self.get_altura_recursivo(self.__raiz)
    def get_altura_recursivo(self,nodo_actual):
        if nodo_actual is None:
            return 0
        else:
            altura_izq=self.get_altura_recursivo(nodo_actual.get_izq())
            altura_der=self.get_altura_recursivo(nodo_actual.get_der())
            return 1+max(altura_izq,altura_der)
#------------------------------------------------------------------------------------------#
    def get_hojas(self,dato):
        if self.__raiz is None:
            print('no hay nodos en el arbol')
            return
        else:
            return self.get_hojas_recursivo(self.__raiz,dato)
    def get_hojas_recursivo(self,nodo_actual,dato):
        if nodo_actual is None:
            return 0
        elif nodo_actual.get_dato()==dato and nodo_actual.get_izq() is None and nodo_actual.get_der() is None:
            return 1
        else:
            return self.get_hojas_recursivo(nodo_actual.get_izq(),dato)+self.get_hojas_recursivo(nodo_actual.get_der(),dato)
#------------------------------------------------------------------------------------------#
    def get_hijos(self,dato):
        if self.__raiz is None:
            print('no hay nodos en el arbol')
            return
        else:
            return self.get_hijos_recursivo(self.__raiz,dato)
    def get_hijos_recursivo(self,nodo_actual,dato):
        if nodo_actual is None:
            return 0
        elif nodo_actual.get_dato()==dato and nodo_actual.get_izq() is not None and nodo_actual.get_der() is not None:
            return 2
        else:
            return self.get_hijos_recursivo(nodo_actual.get_izq(),dato)+self.get_hijos_recursivo(nodo_actual.get_der(),dato)
#------------------------------------------------------------------------------------------#
    def get_grado(self,dato):
        if dato==self.__raiz.get_dato():
            return 0
        else:
            return self.get_grado_recursivo(self.__raiz,dato)
    def get_grado_recursivo(self,nodo,dato):
        if nodo is None:
            return 0
        elif nodo.get_dato()==dato:
            return 1+self.get_grado_recursivo(nodo.get_izq(),dato)+self.get_grado_recursivo(nodo.get_der(),dato)
        else:
            return self.get_grado_recursivo(nodo.get_izq(),dato)+self.get_grado_recursivo(nodo.get_der(),dato)
#______________________________________MAIN__________________________________________________________#
if __name__=="__main__":
    mi_arbol=arbol()
    nodos=[15, 10, 20, 8, 12, 17, 25, 6, 11, 16]
    for valor in nodos:
        mi_arbol.insertar(valor)
    mi_arbol.recorrer_inverso()
    #valor=int(input('ingrese el valor a buscar: '))
    #nodo_buscado=mi_arbol.buscar(valor)
    #if nodo_buscado is not None:
    #    print(f'el valor {nodo_buscado.get_dato()} fue encontrado')
    #valor=int(input('ingrese el valor a eliminar: '))
    #mi_arbol.eliminar(valor)
    #mi_arbol.recorrer_inverso()
    print(f'altura del arbol: {mi_arbol.get_altura()}')
    print(f'cantidad de hojas: {mi_arbol.get_hojas(15)}')
    print(f'grado: {mi_arbol.get_grado(11)}')
    print(f'cantidad de hijos: {mi_arbol.get_hijos(25)}')