class matriz_pesos:
    __matriz:list
    __n_nodos:int
    def __init__(self,numero_nodos):
        self.__n_nodos=numero_nodos
        self.__matriz=[[0 for i in range(numero_nodos)]for j in range(numero_nodos)]
    def agregar_arista_no_dirigido(self,nodo1,nodo2,peso):
        if nodo1<0 or nodo1>self.__n_nodos or nodo2<0 or nodo2>self.__n_nodos:
            return
        else:
            self.__matriz[nodo1][nodo2]=peso
            self.__matriz[nodo2][nodo1]=peso
    def agregar_arista_dirigido(self,nodo1,nodo2,peso):
        if nodo1<0 or nodo1>self.__n_nodos or nodo2<0 or nodo2>self.__n_nodos:
            return
        else:
            self.__matriz[nodo1][nodo2]=peso
    #continuar despues