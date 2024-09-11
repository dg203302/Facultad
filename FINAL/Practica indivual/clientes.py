class clientes:
    __nombre:str
    __apellido:str
    __email:str
    __contrasena:str
    def __init__(self,nombre,apellido,email,contrasena):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__email=email
        self.__contrasena=contrasena
    def get_nombre(self):
        return self.__nombre