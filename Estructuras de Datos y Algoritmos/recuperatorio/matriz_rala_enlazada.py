from lista_enlazada import lista
class datos:
    __componente:int
    __fila:int
    __columna:int
    def __init__(self,componente:int,fila:int,columna:int):
        self.__componente=componente
        self.__fila=fila
        self.__columna=columna
    def get_componente(self):
        return self.__componente
    def get_fila(self):
        return self.__fila
    def get_columna(self):
        return self.__columna
    def __str__(self):
        return f'({self.__fila}, {self.__columna}) = {self.__componente}'
def suma_matrices(matriz1:lista,matriz2:lista):
    if matriz1.get_dimension()==matriz2.get_dimension():
        matriz_suma=lista()
        i=0
        j=0
        while i<matriz1.get_dimension():                                                                                                                                      #n
            matriz_suma.insertar_por_posicion(datos(matriz1.buscar_por_posicion(i).get_componente()+matriz2.buscar_por_posicion(j).get_componente(),i,j),i)      #3n
            i+=1
            j+=1
        matriz_suma.mostrar()
    else:
        print('las matrices no tienen la misma dimension')
if __name__=='__main__':
    matriz1=lista()
    matriz1.insertar_por_posicion(datos(100,0,0),0)
    matriz1.insertar_por_posicion(datos(200,0,1),1)
    matriz1.insertar_por_posicion(datos(300,1,0),2)
    matriz1.insertar_por_posicion(datos(400,1,1),3)
    matriz1.mostrar()
    matriz2=lista()
    matriz2.insertar_por_posicion(datos(304,0,0),0)
    matriz2.insertar_por_posicion(datos(405,0,1),1)
    matriz2.insertar_por_posicion(datos(506,1,0),2)
    matriz2.insertar_por_posicion(datos(607,1,1),3)
    matriz2.mostrar()
    suma_matrices(matriz1,matriz2)