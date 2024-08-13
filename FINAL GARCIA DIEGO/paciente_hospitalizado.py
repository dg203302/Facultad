from paciente import *
class paciente_hospitalizado(paciente):
    __numero_habitacion:int
    __fecha_ingreso:str
    __diagnostico:str
    __cantidad_dias_internacion:int
    __importe_concepto_descartables:float
    def __init__(self, nombre, apellido, email, nrotel,  numerohabitación,fechaingreso, diagnostico, cantidaddiasinternacion, importeconceptodescartables):
        super().__init__(nombre, apellido, email, nrotel)
        self.__numero_habitacion=numerohabitación
        self.__fecha_ingreso=fechaingreso
        self.__diagnostico=diagnostico
        self.__cantidad_dias_internacion=int(cantidaddiasinternacion)
        self.__importe_concepto_descartables=float(importeconceptodescartables)
    def get_diagnostico(self):
        return self.__diagnostico
    def calculo_importe_cobrado(self):
        return (super().calculo_importe_cobrado())+(self.__cantidad_dias_internacion*150000)+self.__importe_concepto_descartables