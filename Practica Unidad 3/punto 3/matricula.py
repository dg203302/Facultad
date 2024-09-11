class matricula:
    __fecha:str
    __empleado:object
    __programa:object
    def __init__(self,fecha,empleado=None,programa=None):
        self.__fecha=fecha
        self.__empleado=empleado
        self.__programa=programa
    def getemp(self):
        return self.__empleado
    def getid(self):
        return self.__empleado.getid()
    def gethoras(self):
        return self.__programa.gethora()
    def getnomp(self):
        return self.__programa.getnomp()
    def getnomemp(self):
        return self.__empleado.getnom()
    def __str__(self):
        return f'{self.__fecha}{self.__empleado.getnom()}{self.__programa.getnomp()}'