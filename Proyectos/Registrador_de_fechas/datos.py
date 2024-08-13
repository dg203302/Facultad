import datetime
class datos_de_registro:
    __hora_actual:datetime
    __dia:datetime.time
    def __init__(self,hora_ocurrida,dia):
        self.__hora_actual=hora_ocurrida
        self.__dia=dia
    def get_hora(self):
        return self.__hora_actual
    def get_dia(self):
        return self.__dia
    def to_json(self):
        diccionario_dia=dict(hora_ocurrida=self.__hora_actual,dia=self.__dia)
        return diccionario_dia
    def __gt__(self,otrodato):
        return self.__dia>otrodato.get_dia()
    def __str__(self):
        return f'------------\nhora de la paja:{self.__hora_actual}\ndia de la paja:{self.__dia}\n------------'