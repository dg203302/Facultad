from locales import *
from nacionales import *
from nodo import *
from encoder import *
class lista_gestor:
    __cabeza:nodo
    __actual:nodo
    __indice:int
    __tope:int
    def __init__(self, cabeza=None, actual=None):
        self.__cabeza=cabeza
        self.__actual=actual
        self.__indice=0
        self.__tope=0
        encoder.cargar_gestor(self)
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__indice=0
            self.__actual=self.__cabeza
            raise StopIteration
        else:
            datos=self.__actual.obtener_datos()
            self.__actual=self.__actual.obtener_siguiente()
            self.__indice+=1
            return datos
    def cargar(self):
        nombre=input('ingrese el nombre del cliente')
        apellido=input('ingrese el apellido del cliente')
        email=input('ingrese el email del cliente')
        contrasena=input('ingrese la contraseña del cliente')
        tipo=input('que tipo de cliente desea ingresar: ')
        while tipo!='local' and tipo!='nacional':
            tipo=input('que tipo de cliente desea ingresar: ')
        if tipo=='local':
            direccion=input('ingrese la direccion del cliente: ')
            telefono=input('ingrese el telefono del cliente: ')
            cliente=locales(nombre,apellido,email,contrasena,direccion,telefono)
            self.insercion(cliente)
        elif tipo=='nacional':
            provincia=input('ingrese la provincia del cliente: ')
            localidad=input('ingrese la localidad del cliente: ')
            codigopostal=input('ingrese el codigo postal del cliente: ')
            cliente=nacionales(nombre,apellido,email,contrasena,provincia,localidad,codigopostal)
            self.insercion(cliente)
    def insercion(self,cliente_nuevo):
        nodo_nuevo=nodo(cliente_nuevo)
        if self.__cabeza==None:
            self.__cabeza=nodo_nuevo
            self.__actual=self.__cabeza
            self.__tope+=1
        else:
            while self.__actual.obtener_siguiente()!=None:
                self.__actual=self.__actual.obtener_siguiente()
            if self.__actual.obtener_siguiente()==None:
                self.__actual.actualizar_siguiente(nodo_nuevo)
                self.__actual=self.__cabeza
                self.__tope+=1
    def inciso2(self):
        for cliente in self:
            if isinstance(cliente,nacionales):
                print(f'nombre del cliente: {cliente.get_nombre()} \nprovincia del cliente: {cliente.get_provincia()}')
    def inciso3(self):
        posicion=int(input('ingrese la posicion que desee saber: '))
        try:
            while self.__indice!=self.__tope and self.__indice!=(posicion-1):
                self.__actual=self.__actual.obtener_siguiente()
                self.__indice+=1
            if self.__indice==(posicion-1):
                print(f'{type(self.__actual.obtener_datos())}')
        except IndexError:
            print('indice ingresado incorrecto!')
    def gestor_a_json(self):
        diccionario_gestor=dict(gestorclientes=[cliente.a_json() for cliente in self])
        encoder.guardar_json(diccionario_gestor)