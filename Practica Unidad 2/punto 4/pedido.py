class pedido:
    __pate_asig: str
    __id_pedido: str
    __com_ped: str
    __t_est: int
    __t_real: int
    __prec: float
    def __init__(self, pate,id,com,t_e,precio):
        self.__pate_asig=pate
        self.__id_pedido=id
        self.__com_ped=com
        self.__t_est=t_e
        self.__t_real=0
        self.__prec=float(precio)
    def getpat(self):
        return self.__pate_asig
    def getid(self):
        return self.__id_pedido
    def gettest(self):
        return self.__t_est
    def gettreal(self):
        return self.__t_real
    def getpre(self):
        return self.__prec
    def modifictr(self, treal):
        self.__t_real=treal
    def __str__(self):
        return f'patente asignada: {self.__pate_asig}, id del pedido: {self.__id_pedido}, comidas pedidas: {self.__com_ped}, tiempo estimado: {self.__t_est}, tiempo real: {self.__t_real}'
    def __lt__(self,ped2):
        return self.__pate_asig < ped2.__pate_asig