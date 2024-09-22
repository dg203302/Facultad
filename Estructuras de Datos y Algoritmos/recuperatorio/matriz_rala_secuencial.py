from lista_secuencial import lista_secuencial
class dato:
    __valor:int
    __fila:int
    __columna:int
    def __init__(self,valor:int,fila:int,columna:int):
        self.__valor=valor
        self.__fila=fila
        self.__columna=columna
    def get_valor(self):
        return self.__valor
    def get_fila(self):
        return self.__fila
    def get_columna(self):
        return self.__columna
    def __str__(self):
        return f'({self.__fila}, {self.__columna}) = {self.__valor}'
def suma_matrices(matriz1,matriz2):
    matriz_suma=lista_secuencial(4)
    for i in range(4):         #n
        for j in range(4):     #n
            if i==j:            #n
                matriz_suma.insertar_por_posicion(dato(matriz1.buscar_por_posicion(i).get_valor()+matriz2.buscar_por_posicion(j).get_valor(),i,j),i)   #3
    matriz_suma.recorrer()
if __name__=='__main__':
    matriz1 = lista_secuencial(4)
    matriz2 = lista_secuencial(4)

    # Llenar la primera matriz
    matriz1.insertar_por_posicion(dato(1, 0, 0),0)
    matriz1.insertar_por_posicion(dato(2, 0, 1),1)
    matriz1.insertar_por_posicion(dato(3, 1, 0),2)
    matriz1.insertar_por_posicion(dato(4, 1, 1),3)

    # Llenar la segunda matriz
    matriz2.insertar_por_posicion(dato(5, 0, 0),0)
    matriz2.insertar_por_posicion(dato(6, 0, 1),1)
    matriz2.insertar_por_posicion(dato(7, 1, 0),2)
    matriz2.insertar_por_posicion(dato(8, 1, 1),3)
    matriz1.recorrer()
    print()
    matriz2.recorrer()
    print(  )
    suma_matrices(matriz1, matriz2)