from nodo import *
class gestor_docentes:
    __inicio:nodo
    __actual:nodo
    __indice:int
    __tope:int
    def __init__(self, inicio=None, actual=None, indice=0, tope=0):
        self.__inicio=inicio
        self.__actual=actual
        self.__indice=indice
        self.__tope=tope
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__indice=0
            self.__actual=self.__inicio
            raise StopIteration
        else:
            datos=self.__actual.get_datos()
            self.__indice+=1
            self.__actual=self.__actual.get_siguiente()
            return datos
    def insercion_cola(self,persona):
        nodo_nuevo=nodo(persona)
        if self.__inicio==None or self.__tope==0:
            self.__inicio=nodo_nuevo
            self.__actual=self.__inicio
            self.__tope+=1
        else:
            while self.__indice<self.__tope and self.__actual.get_siguiente()!=None:
                self.__indice+=1
                self.__actual=self.__actual.get_siguiente()
            if self.__actual.get_siguiente()==None:
                self.__actual.set_siguiente(nodo_nuevo)
                self.__indice=0
                self.__actual=self.__inicio
                self.__tope+=1
    def carga_ejemplo(self):
        docente1=docente('jose','juan','334444555','matematica',40000,50)
        self.insercion_cola(docente1)
        investigador1=investigador('julian','maruca','323242','ciencas',24)
        self.insercion_cola(investigador1)
        persona1=persona('jose','mercado','323242442')
        self.insercion_cola(persona1)
        docente_investigador1=docente_investigador('diego','garcia','44991307','computacion',100000,20,'modificacion',90,8.5,200)
        self.insercion_cola(docente_investigador1)
    def mostrar(self):
        for persona in self:
            print(persona)

if __name__=='__main__':
    gestor=gestor_docentes()
    gestor.carga_ejemplo()
    gestor.mostrar()