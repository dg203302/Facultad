class programa:
    __nombre_programa:str
    __duracion_programa:int
    def __init__(self,nombre_programa,duracion_programa):
        self.__nombre_programa=nombre_programa
        self.__duracion_programa=duracion_programa
    def get_nombre_programa(self):
        return self.__nombre_programa
    def get_duracion_programa(self):
        return self.__duracion_programa
    def __str__(self):
        return f'nombre del programa: {self.__nombre_programa}, duracion del programa: {self.__duracion_programa}'