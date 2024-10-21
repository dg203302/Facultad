class matriz_adyacencia:
    __matriz:list
    __n_nodos:int
    def __init__(self,numero_nodos):
        self.__n_nodos=numero_nodos
        self.__matriz=[[0 for i in range(numero_nodos)]for j in range(numero_nodos)]
    def agregar_arista_no_dirigido(self,nodo1,nodo2):
        if (nodo1>=0 and nodo1<self.__n_nodos) and (nodo2>=0 and nodo2<self.__n_nodos):
            self.__matriz[nodo1][nodo2]=1
    def agregar_arista_no_dirigido(self,nodo1,nodo2):
        if (nodo1>=0 and nodo1<self.__n_nodos) and (nodo2>=0 and nodo2<self.__n_nodos):
            self.__matriz[nodo1][nodo2]=1
            self.__matriz[nodo2][nodo1]=1
    def eliminar_arista(self,nodo1,nodo2):
        self.__matriz[nodo1][nodo2]=0
    def imprimir(self):
        for i in range(self.__n_nodos):
            for j in range(self.__n_nodos):
                print(self.__matriz[i][j],end=" ")
            print()

    def adyacentes_integrado(self,nodo_adyacentes):
        if nodo_adyacentes>=0 and nodo_adyacentes<self.__n_nodos:
            return [indice_columna+1 for indice_columna in range(self.__n_nodos) if self.__matriz[nodo_adyacentes][indice_columna]==1]
        return []
    
    def numero_adyacentes_integrado(self,nodo_adyacentes):
        if nodo_adyacentes>=0 and nodo_adyacentes<self.__n_nodos:
            return sum(self.__matriz[nodo_adyacentes])
    
    def adyacentes_no_integrado(self,nodo_adyacentes):
        if nodo_adyacentes>=0 and nodo_adyacentes<self.__n_nodos:
            print(f'nodos adyacentes al nodo: {nodo_adyacentes+1}', end=': ')
            for nodos_columnas in range(self.__n_nodos):
                if self.__matriz[nodo_adyacentes][nodos_columnas]==1:
                    print(nodos_columnas+1,end=" ")
            print()
    
    def numero_adyacentes_no_integrado(self,nodo_adyacentes):
        if nodo_adyacentes>=0 and nodo_adyacentes<self.__n_nodos:
            c=0
            for nodos_columnas in range(self.__n_nodos):
                if self.__matriz[nodo_adyacentes][nodos_columnas]==1:
                    c+=1
            print(f'numero de nodos adyacentes al nodo {nodo_adyacentes+1}: {c}')
if __name__=='__main__':
    matriz_adyacencia=matriz_adyacencia(5)
    matriz_adyacencia.agregar_arista_no_dirigido(0,1)
    matriz_adyacencia.agregar_arista_no_dirigido(0,2)
    matriz_adyacencia.agregar_arista_no_dirigido(1,2)
    matriz_adyacencia.agregar_arista_no_dirigido(2,3)
    matriz_adyacencia.agregar_arista_no_dirigido(3,4)
    matriz_adyacencia.agregar_arista_no_dirigido(4,0)
    matriz_adyacencia.imprimir()
    #print(f'adyacentes del nodo 1: {matriz_adyacencia.adyacentes_integrado(0)}')
    #print(f'numero de adyacentes del nodo 1: {matriz_adyacencia.numero_adyacentes_integrado(0)}')
    matriz_adyacencia.adyacentes_no_integrado(0)
    matriz_adyacencia.numero_adyacentes_no_integrado(0)