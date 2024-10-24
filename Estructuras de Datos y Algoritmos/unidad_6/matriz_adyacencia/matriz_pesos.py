class matriz_pesos:
    __matriz:list
    __n_nodos:int
    def __init__(self,numero_nodos):
        self.__n_nodos=numero_nodos
        self.__matriz=[['-' for i in range(numero_nodos)]for j in range(numero_nodos)]
    def agregar_arista_no_dirigido(self,nodo1,nodo2,peso):
        if nodo1<0 or nodo1>self.__n_nodos or nodo2<0 or nodo2>self.__n_nodos:
            return
        else:
            self.__matriz[nodo1][nodo2]=peso
            self.__matriz[nodo2][nodo1]=peso
    def agregar_arista_dirigido(self,nodo1,nodo2,peso):
        pass
    def djisktra(self,nodo_inicio):
        distancias=['inf' for i in range(self.__n_nodos)]
        caminos=[[] for i in range(self.__n_nodos)]
        cola_prioridad=[]
        distancias[nodo_inicio]=0
        cola_prioridad.append(nodo_inicio)
        while cola_prioridad:
            nodo=cola_prioridad.pop(0)
            for i in range(self.__n_nodos):
                if self.__matriz[nodo][i]!='-':
                    if distancias[i]=='inf':
                        distancias[i]=distancias[nodo]+1
                        caminos[i]=caminos[nodo]+[nodo]
                        cola_prioridad.append(i)
                    else:
                        if distancias[i]>distancias[nodo]+1:
                            distancias[i]=distancias[nodo]+1
                            caminos[i]=caminos[nodo]+[nodo]
                            cola_prioridad.append(i)
        print('distancias', distancias)
        print('caminos', caminos)
    def mostrar(self):
        for i in range(self.__n_nodos):
            print(f'{i+1}',end='    ')
            for j in range(self.__n_nodos):
                print(self.__matriz[i][j],end=" ")
            print()
if __name__=='__main__':
    matriz_con_pesos=matriz_pesos(5)
    matriz_con_pesos.agregar_arista_no_dirigido(0, 1, 'a')
    matriz_con_pesos.agregar_arista_no_dirigido(0, 2, 'b')
    matriz_con_pesos.agregar_arista_no_dirigido(0, 3, 'c')
    matriz_con_pesos.agregar_arista_no_dirigido(1, 0, 'd')
    matriz_con_pesos.agregar_arista_no_dirigido(1, 2, 'e')
    matriz_con_pesos.agregar_arista_no_dirigido(1, 4, 'f')
    matriz_con_pesos.agregar_arista_no_dirigido(2, 0, 'g')
    matriz_con_pesos.agregar_arista_no_dirigido(2, 1, 'h')
    matriz_con_pesos.agregar_arista_no_dirigido(2, 3, 'i')
    matriz_con_pesos.agregar_arista_no_dirigido(3, 0, 'j')
    matriz_con_pesos.agregar_arista_no_dirigido(3, 2, 'k')
    matriz_con_pesos.agregar_arista_no_dirigido(3, 4, 'l')
    matriz_con_pesos.agregar_arista_no_dirigido(4, 1, 'm')
    matriz_con_pesos.agregar_arista_no_dirigido(4, 3, 'n')
    matriz_con_pesos.mostrar()
    print('-----------------------------metodos-----------------------------')
    matriz_con_pesos.djisktra(0)