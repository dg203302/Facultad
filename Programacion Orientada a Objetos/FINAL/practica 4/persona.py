class persona:
    __nombre:str
    __apellido:str
    __dni:str
    def __init__(self,nombre,apellido,dni):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__dni=dni
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_dni(self):
        return self.__dni
    def __str__(self):
        return f'{self.__nombre} {self.__apellido} {self.__dni}'
    def to_json(self):
        return dict(tipo="persona", atributos=dict(nombre=self.__nombre, apellido=self.__apellido, dni=self.__dni))