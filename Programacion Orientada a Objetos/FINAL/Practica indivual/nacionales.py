from clientes import *
class nacionales(clientes):
    __provincia:str
    __localidad:str
    __codigo_postal:str
    def __init__(self, nombre, apellido, email, contrasena, provincia, localidad, codigopostal):
        super().__init__(nombre, apellido, email, contrasena)
        self.__provincia=provincia
        self.__localidad=localidad
        self.__codigo_postal=codigopostal
    def get_provincia(self):
        return self.__provincia
    def a_json(self):
        return dict(tipo='nacional', datos=dict(nombre=self._clientes__nombre, apellido=self._clientes__apellido, email=self._clientes__email, contrasena=self._clientes__contrasena, provincia=self.__provincia, localidad=self.__localidad, codigopostal=self.__codigo_postal))