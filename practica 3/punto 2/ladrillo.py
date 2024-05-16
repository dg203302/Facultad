class Ladrillo:
    __alto: 25
    __largo: 15
    __ancho: 7
    __idladr: int
    __cant: int
    __kg_matpri: float
    __costo: float
    __mater_refrac=list
    def actcosto(self,costoad):
        self.__costo+=float(costoad)
    def __init__(self,idlad,cant,kgmate,costo):
        self.__idladr=idlad
        self.__cant=cant
        self.__kg_matpri=kgmate
        self.__costo=float(costo)
        self.__mater_refrac=[]
    def addmateref(self,materref):
        self.actcosto(materref.getcosto())
        self.__mater_refrac.append(materref)
    def getcost(self):
        return self.__costo
    def a(self):
        for mate in self.__mater_refrac:
            print(f'costo de los materiales: {mate.getcost()} caracteristicas de los materiales: {mate.getcaract()}')
    def mostrar_dat(self):
        print(f'|id ladrillo: {self.__idladr} |costo del ladrillo: {self.__costo}|')
        for mate in self.__mater_refrac:
            print(f'material: {mate}')
    def getid(self):
        return self.__idladr