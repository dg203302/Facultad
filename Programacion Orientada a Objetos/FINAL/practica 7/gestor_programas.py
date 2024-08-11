import csv
from programa import *
class gestor_programas:
    __programas:list
    def __init__(self):
        self.__programas=[]
        with open('Programacion Orientada a Objetos/FINAL/practica 7/programas.csv',mode='r') as programas_csv:
            lector=csv.reader(programas_csv,delimiter=';')
            for fila in lector:
                programa_nuevo=programa(fila[0],fila[1])
                self.__programas.append(programa_nuevo)
            programas_csv.close()
    def buscar_programas(self,nombre_programa):
        i=0
        while self.__programas[i].get_nombre_programa()!=nombre_programa:
            i+=1
        if self.__programas[i].get_nombre_programa()==nombre_programa:
            return self.__programas[i]