class paciente:
    __nombre:str
    __apellido:str
    __email:str
    __nro_telefono:str
    __v_consulta=float(15000)
    def __init__(self,nombre,apellido,email,nrotel):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__email=email
        self.__nro_telefono=nrotel
    def get_nombre(self):
        return self.__nombre
    def calculo_importe_cobrado(self):
        return self.__v_consulta
    @classmethod
    def set_nuevo_valor_consulta(cls, nuevo_valor_consulta):
        cls.__v_consulta=nuevo_valor_consulta