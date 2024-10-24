class matriz_adyacencia:
    __matriz:list
    __n_nodos:int
    def __init__(self,numero_nodos):
        self.__n_nodos=numero_nodos
        self.__matriz=[[0 for i in range(numero_nodos)]for j in range(numero_nodos)]
#-----------------metodos-------------------#
#-------------------------------------------#
    def agregar_arista_no_dirigido(self,nodo1,nodo2):
        if (nodo1>=0 and nodo1<self.__n_nodos) and (nodo2>=0 and nodo2<self.__n_nodos):
            self.__matriz[nodo1][nodo2]=1
    def agregar_arista_dirigido(self,nodo1,nodo2):
        if (nodo1>=0 and nodo1<self.__n_nodos) and (nodo2>=0 and nodo2<self.__n_nodos):
            self.__matriz[nodo1][nodo2]=1
            self.__matriz[nodo2][nodo1]=1
#-------------------------------------------#
    def eliminar_arista(self,nodo1,nodo2):
        self.__matriz[nodo1][nodo2]=0
#-------------------------------------------#
    def imprimir(self):
        for i in range(self.__n_nodos):
            print(f'{i+1}',end='    ')
            for j in range(self.__n_nodos):
                print(self.__matriz[i][j],end=" ")
            print()
#-------------------------------------------#
    def adyacentes(self,nodo_adyacentes):
        if nodo_adyacentes>=0 and nodo_adyacentes<self.__n_nodos:
            #nodos_adyacentes=[None]*self.__n_nodos
            #c=0
            print(f'nodos adyacentes al nodo: {nodo_adyacentes+1}', end=': ')
            for nodos_columnas in range(self.__n_nodos):
                if self.__matriz[nodo_adyacentes][nodos_columnas]==1:
                    #nodo_adyacentes[c]=nodos_columnas
                    #c+=1
                    print(nodos_columnas+1,end=" ")
            print()
#-------------------------------------------#
    def numero_adyacentes(self,nodo_adyacentes):
        if nodo_adyacentes>=0 and nodo_adyacentes<self.__n_nodos:
            c=0
            for nodos_columnas in range(self.__n_nodos):
                if self.__matriz[nodo_adyacentes][nodos_columnas]==1:
                    c+=1
            print(f'numero de nodos adyacentes al nodo {nodo_adyacentes+1}: {c}')
#-------------------------------------------#
    def camino(self,nodo1,nodo2):
        if (nodo1>=0 and nodo1<self.__n_nodos) and (nodo2>=0 and nodo2<self.__n_nodos):
            if self.__matriz[nodo1][nodo2]==1:
                return [nodo1+1,nodo2+1]
            else:
                camino=[]
                camino.append(nodo1+1)
                j=nodo1
                for i in range(self.__n_nodos):
                    if self.__matriz[j][i]==1:
                        if i==nodo2:
                            camino.append(i+1)
                            return camino
                        else:
                            camino.append(i+1)
                            j=i
#-------------------------------------------#
    def conexidad(self):
        if all(self.REP(0)):
            print('el grafo es conexo')
        else:
            print('el grafo no es conexo')
#-------------------------------------------#
    def REA(self,nodo_inicio):#recorrido en anchura
        if nodo_inicio>=0 and nodo_inicio<self.__n_nodos:
            visitados=[False]*self.__n_nodos
            cola=[]
            cola.append(nodo_inicio)
            visitados[nodo_inicio]=True
            while cola:
                nodo_while=cola.pop(0)
                print(nodo_while+1,end=' ')
                for j in range(self.__n_nodos):
                    if self.__matriz[nodo_while][j]==1 and visitados[j]==False:
                        cola.append(j)
                        visitados[j]=True
#-------------------------------------------#
    def REP(self, nodo_inicio, visitados=None):#recorrido en profundidad
        if nodo_inicio>=0 and nodo_inicio<self.__n_nodos:
            if visitados is None:
                visitados=[False]*self.__n_nodos
            visitados[nodo_inicio]=True
            print(nodo_inicio+1,end=' ')
            for i in range(self.__n_nodos):
                if self.__matriz[nodo_inicio][i]==1 and visitados[i]==False:
                    self.REP(i,visitados)
            return visitados
#-------------------------------------------#
    def aciclico(self):
        band=False
        for i in range(self.__n_nodos):
            if self.__matriz[i][i]==1:
                band=True
        if band==True:
            print('el matriz_adyacencia agregar_arista_no_dirigido ciclo')
        else:
            print('el matriz_adyacencia agregar_arista_no_dirigido tiene ciclo')
#-------------------------------------------#
    def grado_entrada(self,nodo):
        if nodo>=0 and nodo<self.__n_nodos:
            ac=0
            for i in range(self.__n_nodos):
                if self.__matriz[i][nodo]==1:
                    ac+=1
            return ac
#-------------------------------------------#
    def grado_salida(self,nodo):
        if nodo>=0 and nodo<self.__n_nodos:
            ac=0
            for i in range(self.__n_nodos):
                if self.__matriz[nodo][i]==1:
                    ac+=1
            return ac
#-------------------------------------------#
    def nodo_fuente(self,nodo):
        if nodo>=0 and nodo<self.__n_nodos:
            if self.grado_entrada(nodo)==0:
                print(f'el nodo {nodo+1} es fuente')
            else:
                print(f'el nodo {nodo+1} no es fuente')
#-------------------------------------------#
    def nodo_sumidero(self,nodo):
        if nodo>=0 and nodo<self.__n_nodos:
            if self.grado_salida(nodo)==0:
                print(f'el nodo {nodo+1} es sumidero')
            else:
                print(f'el nodo {nodo+1} no es sumidero')
#-------------------------------------------#
if __name__=='__main__':
    matriz_adyacencia=matriz_adyacencia(5)
    matriz_adyacencia.agregar_arista_no_dirigido(0,1)
    matriz_adyacencia.agregar_arista_no_dirigido(0,2)
    matriz_adyacencia.agregar_arista_no_dirigido(0,3)
    matriz_adyacencia.agregar_arista_no_dirigido(1,0)
    matriz_adyacencia.agregar_arista_no_dirigido(1,2)
    matriz_adyacencia.agregar_arista_no_dirigido(1,4)
    matriz_adyacencia.agregar_arista_no_dirigido(2,0)
    matriz_adyacencia.agregar_arista_no_dirigido(2,1)
    matriz_adyacencia.agregar_arista_no_dirigido(2,3)
    matriz_adyacencia.agregar_arista_no_dirigido(3,0)
    matriz_adyacencia.agregar_arista_no_dirigido(3,2)
    matriz_adyacencia.agregar_arista_no_dirigido(3,4)
    matriz_adyacencia.agregar_arista_no_dirigido(4,1)
    matriz_adyacencia.agregar_arista_no_dirigido(4,3)
    matriz_adyacencia.imprimir()
    matriz_adyacencia.conexidad()
    print('recorrido en anchura')
    matriz_adyacencia.REA(0)
    print()
    '''
    #matriz_adyacencia.agregar_arista_no_dirigido(4,1)
    matriz_adyacencia.adyacentes(0)
    matriz_adyacencia.numero_adyacentes(0)
    print('camino del nodo 1 al nodo 5: ', matriz_adyacencia.camino(0,3))
    #matriz_adyacencia.agregar_arista_no_dirigido(1,1)
    matriz_adyacencia.aciclico()
    print('recorrido en profundidad')
    matriz_adyacencia.REP(0)
    print()
    matriz_adyacencia.grado_entrada(0)
    matriz_adyacencia.grado_salida(0)
    print('------------------------------------------')
    for i in range(5):
        matriz_adyacencia.nodo_fuente(i)
        matriz_adyacencia.nodo_sumidero(i)
        print('------------------------------------------')
    print('------------------------------------------')
    '''