from colas import cola_secuencial
import random
class cajeros:
    __cajero1:cola_secuencial
    __cajero2:cola_secuencial
    __cajero3:cola_secuencial
    __cantidad_clientes_atendidos:int
    __cantidad_clientes_sin_atender:int
    __cronometro_general:int
    __cantidad_por_cajero=5
    def __init__(self) -> None:
        self.__cajero1=cola_secuencial(self.__cantidad_por_cajero)
        self.__cajero2=cola_secuencial(self.__cantidad_por_cajero)
        self.__cajero3=cola_secuencial(self.__cantidad_por_cajero)
        self.__cantidad_clientes_atendidos=0
        self.__cantidad_clientes_sin_atender=0
        self.__cronometro_general=0
    def agregar_clientes(self,nuevo_cliente):
        if self.__cajero1.get_cantidad()==0 and self.__cajero2.get_cantidad()==0 and self.__cajero3.get_cantidad()==0 or self.__cajero1.get_cantidad()==0 or self.__cajero2.get_cantidad()==0 or self.__cajero3.get_cantidad()==0:
            eleccion=random.randint(1,3)
            if eleccion==1:
                self.__cajero1.insertar(nuevo_cliente)
            elif eleccion==2:
                self.__cajero2.insertar(nuevo_cliente)
            elif eleccion==3:
                self.__cajero3.insertar(nuevo_cliente)
        elif self.__cajero1.get_cantidad()==5 and self.__cajero2.get_cantidad()==5 and self.__cajero3.get_cantidad()==5:
            if self.__cajero1.get_cantidad()<self.__cajero2.get_cantidad() and self.__cajero1.get_cantidad()<self.__cajero3.get_cantidad():
                self.__cajero1.insertar(nuevo_cliente)
            elif self.__cajero2.get_cantidad()<self.__cajero1.get_cantidad() and self.__cajero2.get_cantidad()<self.__cajero3.get_cantidad():
                self.__cajero2.insertar(nuevo_cliente)
            elif self.__cajero3.get_cantidad()<self.__cajero1.get_cantidad() and self.__cajero3.get_cantidad()<self.__cajero2.get_cantidad():
                self.__cajero3.insertar(nuevo_cliente)
        self.aumentar_cronometro()
    def aumentar_cronometro(self):
        self.__cronometro_general+=1
    def atender(self):
        if self.__cronometro_general%5==0:
            self.__cajero1.suprimir_primero()
            print(f'tiempo total en ser atendido: {self.__cronometro_general}')
            self.__cantidad_clientes_atendidos+=1
            self.__cantidad_clientes_sin_atender+=self.__cajero1.get_cantidad()
        elif self.__cronometro_general%3==0:
            self.__cajero2.suprimir_primero()
            print(f'tiempo total en ser atendido: {self.__cronometro_general}')
            self.__cantidad_clientes_atendidos+=1
            self.__cantidad_clientes_sin_atender+=self.__cajero1.get_cantidad()
        elif self.__cronometro_general%4==0:
            self.__cajero3.suprimir_primero()
            print(f'tiempo total en ser atendido: {self.__cronometro_general}')
            self.__cantidad_clientes_atendidos+=1
            self.__cantidad_clientes_sin_atender+=self.__cajero1.get_cantidad()
    def mostrar_cantidades_promedios(self):
        print(f'cantidad de clientes sin atender: {self.__cantidad_clientes_sin_atender}\ncantidad de clientes atendidos: {self.__cantidad_clientes_atendidos}\npromedio de clientes atendidos: {self.__cronometro_general/self.__cantidad_clientes_atendidos}\ncantidad de clientes no atendidos: {self.__cronometro_general/self.__cantidad_clientes_sin_atender}')
    @classmethod
    def modificar_cantidad_por_cajero(cls,nueva_cantidad):
        cls.__cantidad_por_cajero=nueva_cantidad