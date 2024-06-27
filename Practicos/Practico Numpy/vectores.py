import numpy as np
class matriz:
    __mat: np.array
    #definicion de la matriz para el main
    def __init__(self,n,m):
        self.__mat=np.zeros((n,m), dtype=float)
        print(f'Caracteristicas de la matriz creada: \n Dimension: {np.shape(self.__mat)}, N° de elementos: {np.size(self.__mat)}')
    def cargar(self,i,j,v):
        self.__mat[i][j]=v
    #operaciones entre dos matrices
    def __add__(self, obj):        #sobrecarga +
        return self.__mat + obj.__mat
    def __mul__(self,obj):         #sobrecarga del *
        return np.dot(self.__mat, obj.__mat)
    def __sub__(self,obj):
        return self.__mat-obj.__mat
    #operaciones por cada matriz
    def inver(self):
        return np.linalg.inv(self.__mat)
    def traspuesta(self):
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
    def seno(self):                #seno de cada valor de la matriz 
        return np.sin(self.__mat)
    def coseno(self):              #coseno de cada valor de la matriz
        return np.cos(self.__mat)
    def __str__(self):
        return f'{self.__mat}'