class reparacion:
    __pate_rep:str
    __repa:str
    __repuesto:str
    __prec_rep:float
    __prec_manobra:float
    __est_rep:str
    def __init__(self,pate,rep,repu,preci,preci2,esta):
        self.__pate_rep=pate
        self.__repa=rep
        self.__repuesto=repu
        self.__prec_rep=float(preci)
        self.__prec_manobra=float(preci2)
        self.__est_rep=esta
    def getpate(self):
        return self.__pate_rep
    def getrepa(self):
        return self.__repa
    def getpre_rep(self):
        return self.__prec_rep
    def getpre_manobra(self):
        return self.__prec_manobra
    def get_est_rep(self):
        return self.__est_rep