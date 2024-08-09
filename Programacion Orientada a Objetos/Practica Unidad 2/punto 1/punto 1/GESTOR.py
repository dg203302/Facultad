from CAJAAHORRO import caja_ahorro
class contenedor:
    __cajas: list
    def __init__(self):
        self.__cajas=[]
    def agreg(self,cuenta):
        self.__cajas.append(cuenta)
    def obtener_datos(self,cuil):
        i=0
        enc=False
        while enc == False and i < len(self.__cajas):
            if self.__cajas[i].getcuil() == cuil:
                enc=True
        if enc == True:
            print(f'nombre de la cuenta: {self.__cajas[i].getnom()}, apellido de la cuenta: {self.__cajas[i].getap()}, saldo de la cuenta: {self.__cajas[i].getsal()}')
        else:
            print('cuil no valido')