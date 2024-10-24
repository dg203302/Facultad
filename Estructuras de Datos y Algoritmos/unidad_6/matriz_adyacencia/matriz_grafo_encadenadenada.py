class nodo_grafo:
    __nodo_ady:object
    __siguiente:'nodo_grafo'
    def __init__(self, nodo_adyacente):
        self.__nodo_ady=nodo_adyacente
        self.__siguiente=None
    def get_nodo_ady(self):
        return self.__nodo_ady
    def set_nodo_ady_siguiente(self, nodo_adyacente):
        self.__siguiente=nodo_adyacente
    def get_siguiente(self):
        return self.__siguiente
class matriz_grafo_encadenada:
    __nodos_fila:list
    __cantidad_nodos:int
    def __init__(self,numero_nodos):
        self.__cantidad_nodos=numero_nodos
        self.__nodos_fila=[nodo_grafo(i) for i in range(numero_nodos)]
    def insertar_adyacente_no_dirigido(self,nodo1,nodo2):
        if (nodo1>=0 and nodo1<self.__cantidad_nodos) and (nodo2>=0 and nodo2<self.__cantidad_nodos):
            nodo_auxiliar=self.__nodos_fila[nodo1]
            while nodo_auxiliar.get_siguiente()!=None:
                nodo_auxiliar=nodo_auxiliar.get_siguiente()
            nodo_auxiliar.set_nodo_ady_siguiente(nodo_grafo(nodo2))
    def __str__(self):
        result = ""
        for i in range(self.__cantidad_nodos):
            result += f'{i+1}    '
            nodo_recorrer = self.__nodos_fila[i]
            while nodo_recorrer.get_siguiente() is not None:
                result += f'{nodo_recorrer.get_siguiente().get_nodo_ady()} '
                nodo_recorrer = nodo_recorrer.get_siguiente()
            result += '\n'
        return result
    def insertar_adyacente_dirigido(self,nodo1,nodo2):
        pass
if __name__=='__main__':
    grafo=matriz_grafo_encadenada(5)
    grafo.insertar_adyacente_no_dirigido(0,1)
    grafo.insertar_adyacente_no_dirigido(0,2)
    grafo.insertar_adyacente_no_dirigido(0,3)
    grafo.insertar_adyacente_no_dirigido(1,0)
    grafo.insertar_adyacente_no_dirigido(1,2)
    grafo.insertar_adyacente_no_dirigido(1,4)
    grafo.insertar_adyacente_no_dirigido(2,0)
    grafo.insertar_adyacente_no_dirigido(2,1)
    grafo.insertar_adyacente_no_dirigido(2,3)
    grafo.insertar_adyacente_no_dirigido(3,0)
    grafo.insertar_adyacente_no_dirigido(3,2)
    grafo.insertar_adyacente_no_dirigido(3,4)
    grafo.insertar_adyacente_no_dirigido(4,1)
    grafo.insertar_adyacente_no_dirigido(4,3)
    print(grafo)