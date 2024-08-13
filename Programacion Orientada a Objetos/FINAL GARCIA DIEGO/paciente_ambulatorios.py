from paciente import *
class paciente_ambulatorio(paciente):
    __historial_medico:str
    __alergias:str
    __obra_social:str
    def __init__(self, nombre, apellido, email, nrotel, historial,alergias,obrasocial):
        super().__init__(nombre, apellido, email, nrotel)
        self.__historial_medico=historial
        self.__alergias=alergias
        self.__obra_social=obrasocial
    def calculo_importe_cobrado(self):
        if self.__obra_social=='Obra Social Provincia':
            return ((super().calculo_importe_cobrado())-15000)+5000
        elif self.__obra_social=='OSDE':
            return ((super().calculo_importe_cobrado())-15000)+2000
        else:
            return ((super().calculo_importe_cobrado())-15000)+10000