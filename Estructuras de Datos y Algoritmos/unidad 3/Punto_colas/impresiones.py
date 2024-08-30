from colas import cola_enlazada
class impresiones:
    __impresora:cola_enlazada
    __tiempo_ejecucion:float
    __trabajos_ingresados:int
    __tiempo_trabajos_realizados:float
    __cantidad_trabajos_realizados:int
    __cantidad_trabajos_sin_atender:int
    __tiempo_maximo=float(5)
    def __init__(self):
        self.__impresora=cola_enlazada()
        self.__tiempo_ejecucion=0
        self.__trabajos_ingresados=0
        self.__tiempo_trabajos_realizados=0
        self.__cantidad_trabajos_realizados=0
        self.__cantidad_trabajos_sin_atender=0
    def ingresar_trabajos(self):
        tiempo_impresion=float(input('ingrese el tiempo de impresion del trabajo: '))
        self.__impresora.insertar(tiempo_impresion)
        self.__trabajos_ingresados+=1
        self.__tiempo_ejecucion+=1
    def atender(self):
        self.__tiempo_ejecucion+=self.__impresora.get_dato()
        if self.__tiempo_ejecucion<self.__tiempo_maximo:
            self.__impresora.suprimir()
            print('impresion realizada!')
            self.__tiempo_trabajos_realizados+=self.__tiempo_ejecucion
            self.__cantidad_trabajos_realizados+=1
            self.__tiempo_ejecucion=0
        else:
            tiempo_restante=self.__tiempo_ejecucion-5
            self.__impresora.suprimir()
            print('impresion excede tiempo')
            self.__impresora.insertar(tiempo_restante)
            self.__cantidad_trabajos_sin_atender+=1
            self.__tiempo_ejecucion=0
    def mostrar_trabajos(self):
        try:
            print(f'cantidad de trabajos sin atender: {self.__cantidad_trabajos_sin_atender}\npromedio de espera {self.__tiempo_trabajos_realizados/self.__cantidad_trabajos_realizados}')
        except ZeroDivisionError:
            print(f'cantidad de trabajos sin atender: {self.__cantidad_trabajos_sin_atender}')