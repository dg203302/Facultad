from personal import *
class docente(personal):
    __carre:str
    __cargo:str
    __cated:str
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, categoria='', area_investigacion='', tipo_investigacion='', categoria_incentivos='', importe_extra=0):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, categoria, area_investigacion, tipo_investigacion, categoria_incentivos, importe_extra)
        self.__carre=carrera
        self.__cargo=cargo
        self.__cated=catedra
    def getsueld(self):
        return self.getsueldoce()
    def getsueldoce(self): #cambiar que esta mal
        if self.__cargo == 'simple':
            return self._personal__sueld_bas+(self._personal__antig*(self._personal__antig/100))+(10*(10/100))
        elif self.__cargo == 'semiexclusivo':
            return self._personal__sueld_bas+(self._personal__antig*(self._personal__antig/100))+(20*(20/100))
        elif self.__cargo == 'exclusivo':
            return self._personal__sueld_bas+(self._personal__antig*(self._personal__antig/100))+(50*(50/100))
    def tojson(self):
        d=dict(tipo=__class__.__name__,datos=dict(cuil=self._personal__cuil, apellido=self._personal__ape, nombre=self._personal__nom, sueldo_basico=self._personal__sueld_bas, antiguedad=self._personal__antig, carrera=self.__carre, cargo=self.__cargo, catedra=self.__cated))
        return d