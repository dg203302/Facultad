import csv
from certificado import *
class gestor_de_certificados:
    __certificados:list
    def __init__(self,gestor_empleados,gestor_programas):
        self.__certificados=[]
        certificados_csv=open('Programacion Orientada a Objetos/FINAL/practica 7/certificados.csv',mode='r')
        lector=csv.reader(certificados_csv,delimiter=';')
        for fila in lector:
            empleado_certificado=gestor_empleados.buscar_empleados(fila[0])
            programa_certificado=gestor_programas.buscar_programas(fila[1])
            nuevo_certificado=certificado(empleado_certificado,programa_certificado)
            self.__certificados.append(nuevo_certificado)
        certificados_csv.close()
    def mostrar(self):
        for certificado in self.__certificados:
            print(f'EMPLEADO:\n{certificado.get_empleado()}\nINSCRIPTO EN EL PROGRAMA:\n{certificado.get_programa()}\n')