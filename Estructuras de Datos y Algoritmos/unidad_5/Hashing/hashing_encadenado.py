#---------------------------------------NODO-------------------------#
class nodo:
    __dato:object
    __siguiente:object
    def __init__(self,dato=None,siguiente=None):
        self.__dato=dato
        self.__siguiente=siguiente
    def get_dato(self):
        return self.__dato
    def set_siguiente(self, siguiente):
        self.__siguiente=siguiente
    def get_siguiente(self):
        return self.__siguiente
#---------------------------------------HASHING ENCADENADO-------------------------#
class hashing_encadenado:
    __items:list
    __tamano:int
    __cantidad_elementos:int
    def __init__(self,tamano):
        self.__items=[None]*tamano
        self.__tamano=tamano
        self.__cantidad_elementos=0
#---------------------------------------------------------#
    def hasheo_modulo(self, clave):
        return clave%self.__tamano
    def insertar_modulo(self,valor):
        if self.__cantidad_elementos==self.__tamano:
            print('Tabla llena')
            return
        else:
            indice=self.hasheo_modulo(valor)
            if self.__items[indice]==None:
                self.__items[indice]=nodo(valor)
                self.__cantidad_elementos+=1
            else:
                actual = self.__items[indice]
                while actual.get_siguiente() is not None:
                    actual = actual.get_siguiente()
                actual.set_siguiente(nodo(valor))
                self.__cantidad_elementos+=1
#---------------------------------------------------------------#
    def buscar(self,valor):
        indice=self.hasheo_modulo(valor)
        actual=self.__items[indice]
        while actual != None and actual.get_dato()!=valor:
            actual=actual.get_siguiente()
        if actual==None:
            return False
        else:
            return True
#---------------------------------------------------------------#
    def mostrar(self):
        for i in range(0,self.__tamano):
            cadena='['
            actual=self.__items[i]
            while actual!=None:
                cadena+=str(actual.get_dato())+','
                actual=actual.get_siguiente()
            cadena+=']'
            print(f'{i}-->{cadena}')
#-----------------------------------MAIN-----------------------------------#
if __name__=='__main__':
    hasheo=hashing_encadenado(2)
    hasheo.insertar_modulo(10)
    hasheo.insertar_modulo(20)
    hasheo.insertar_modulo(30)
    hasheo.insertar_modulo(40)
    hasheo.mostrar()
    if hasheo.buscar(10) is True:
        print('encontrado')
    else:
        print('no encontrado')