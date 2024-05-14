class Ladrillo:
    __alto: int
    __largo: int
    __ancho: int
    __cant: int
    __idladr: int
    __kg_matpri: float
    __costo: float
    __mater_refrac=list
    def __init__(self,alto,largo,ancho,cant,idlad,kgmate,costo):
        self.__alto=alto
        self.__largo=largo
        self.__ancho=ancho
        self.__cant=cant
        self.__idladr=idlad
        self.__kg_matpri=kgmate
        self.__costo=costo
        self.__mater_refrac=[]
    def addmateref(self,materref):
        self.__mater_refrac.append(materref)