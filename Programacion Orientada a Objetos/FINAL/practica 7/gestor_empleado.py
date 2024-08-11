import csv
from empleado import *
class gestor_empleados:
    __empleados:list
    def __init__(self):
        self.__empleados=[]
        with open('Programacion Orientada a Objetos/FINAL/practica 7/empleados.csv',mode='r') as empleados_csv:
            lector=csv.reader(empleados_csv,delimiter=';')
            for fila in lector:
                empleado_nuevo=empleado(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.__empleados.append(empleado_nuevo)
            empleados_csv.close()
    def buscar_empleados(self,id):
        i=0
        while self.__empleados[i].get_id()!=id:
            i+=1
        if self.__empleados[i].get_id()==id:
            return self.__empleados[i]