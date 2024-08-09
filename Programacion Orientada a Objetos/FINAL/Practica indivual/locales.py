from clientes import *
class locales(clientes):
    __direccion_postal:str
    __telefono:str
    def __init__(self, nombre, apellido, email, contrasena, direccionpostal,telefono):
        super().__init__(nombre, apellido, email, contrasena)
        self.__direccion_postal=direccionpostal
        self.__telefono=telefono
    def a_json(self):
        return dict(tipo='local', datos=dict(nombre=self._clientes__nombre, apellido=self._clientes__apellido, email=self._clientes__email, contrasena=self._clientes__contrasena, direccionpostal=self.__direccion_postal, telefono=self.__telefono))