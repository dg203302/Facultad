import numpy as np
class matriz:
    __mat: np.array
    def __init__(self):
        self.__mat=np.random.randint(1, 100, (3,3))
    #operaciones entre dos matrices
    def __add__(self, obj):        #sobrecarga +
        return self.__mat + obj.__mat
    def __mul__(self,obj):         #sobrecarga del *
        return np.dot(self.__mat, obj.__mat)
    def __sub__(self,obj):
        return self.__mat-obj.__mat
    #operaciones por cada matriz
    def inver(self):               #inversa de la matriz
        return np.linalg.inv(self.__mat)
    def traspuesta(self):          #traspuesta
        return np.transpose(self.__mat)
    def deter(self):               #determinante de la matriz
        return np.linalg.det(self.__mat)
    def norma(self):               #norma de la matriz
        return np.linalg.norm(self.__mat)
    def traza(self):               #traza de la matriz
        return np.trace(self.__mat)
    def min(self):                 #minimo de la matriz
        return np.min(self.__mat)
    def max(self):                 #maximo de la matriz
        return np.max(self.__mat)
    def media(self):
        return np.mean(self.__mat)
    #descripcion de la matriz
    def desc_matriz(self):
        print(f'Dimension de la matriz: {np.shape(self.__mat)} \n numero de elementos {np.size(self.__mat)} \n matriz: \n {self.__mat}')