import csv
from nodo import *
from paciente_hospitalizado import *
from paciente_ambulatorios import *
class lista:
    __inicio:nodo
    __actual:nodo
    __indice:int
    __tope:int
    def __init__(self,inicio=None,actual=None,indice=0,tope=0):
        self.__inicio=inicio
        self.__actual=actual
        self.__indice=indice
        self.__tope=tope
        self.cargar_csv()
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__indice=0
            self.__actual=self.__inicio
            raise StopIteration
        else:
            dato=self.__actual.get_datos()
            self.__indice+=1
            self.__actual=self.__actual.get_siguiente()
            return dato
    def insertar(self,paciente):
        nodo_nuevo=nodo(paciente)
        if self.__inicio==None or self.__tope==0:
            self.__inicio=nodo_nuevo
            self.__actual=self.__inicio
            self.__tope+=1
        else:
            while self.__actual.get_siguiente()!=None and self.__indice<self.__tope:
                self.__actual=self.__actual.get_siguiente()
                self.__indice+=1
            if self.__actual.get_siguiente()==None:
                self.__actual.set_siguiente(nodo_nuevo)
                self.__tope+=1
                self.__indice=0
                self.__actual=self.__inicio
    def cargar_csv(self):
        archivo_csv=open('FINAL GARCIA DIEGO/pacientes.csv',mode='r')
        reader_csv=csv.reader(archivo_csv,delimiter=';')
        for fila in reader_csv:
            if fila[0]=='P':
                nuevo_paciente=paciente(fila[1],fila[2],fila[3],fila[4])
                self.insertar(nuevo_paciente)
            elif fila[0]=='O':
                nuevo_paciente=paciente_ambulatorio(fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7])
                self.insertar(nuevo_paciente)
            elif fila[0]=='H':
                nuevo_paciente=paciente_hospitalizado(fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9])
                self.insertar(nuevo_paciente)
        archivo_csv.close()
    def inciso_b(self):
        cant_p_hosp=0
        cant_p_amb=0
        for paciente in self:
            if isinstance(paciente,paciente_hospitalizado) and paciente.get_diagnostico()=='Neumonia':
                cant_p_hosp+=1
            elif isinstance(paciente,paciente_ambulatorio):
                cant_p_amb+=1
        print(f'Cantidad de pacientes hospitalizado con neumonia: {cant_p_hosp}\nCantidad de pacientes ambulatorios: {cant_p_amb}')
    def inciso_c(self):
        for paciente in self:
            print(f'importe cobrado al paciente {paciente.get_nombre()}: {paciente.calculo_importe_cobrado()}')
    def inciso_d(self,valor_leido):
        while self.__actual.get_siguiente()!=None and self.__indice<valor_leido:
            self.__actual=self.__actual.get_siguiente()
            self.__indice+=1
        if self.__indice==valor_leido:
            if isinstance(self.__actual.get_datos(),paciente) and (not(isinstance(self.__actual.get_datos(),paciente_ambulatorio)) and not(isinstance(self.__actual.get_datos(),paciente_hospitalizado))):
                print(f'el paciente {self.__actual.get_datos().get_nombre()} es un paciente comun')
            if isinstance(self.__actual.get_datos(),paciente_ambulatorio):
                print(f'el paciente {self.__actual.get_datos().get_nombre()} es un paciente ambulatorio')
            if isinstance(self.__actual.get_datos(),paciente_hospitalizado):
                print(f'el paciente {self.__actual.get_datos().get_nombre()} es un paciente hospitalizado')
            self.__actual=self.__inicio
            self.__indice=0
        elif valor_leido>self.__indice:
            self.__actual=self.__inicio
            self.__indice=0
            raise IndexError
    def inciso_e(self,nuevo_valor_consulta):
        for paciente in self:
            paciente.set_nuevo_valor_consulta(nuevo_valor_consulta)
    def prueba(self):
        for paciente in self:
            print(f'{paciente.get_nombre()}')