#si esta ocupado moverme con el modulo
class hashing_abierto:
    __items:list
    __tamano:int
    def __init__(self, tamano:int):
        self.__items=[None]*tamano
        self.__tamano=tamano
    def hasheo(self, clave):
        return clave%self.__tamano
    def insertar(self, valor):
        if self.__items[self.hasheo(valor)]==None:
            self.__items[self.hasheo(valor)]=valor
        else:
            i=0
            while self.__items[(self.hasheo(valor)+i)%self.__tamano]!=None and i<self.__tamano:
                i+=1
            if i>self.__tamano:
                print("Tabla llena")
            else:
                self.__items[(self.hasheo(valor)+i)%self.__tamano]=valor
    def buscar(self, valor):
        if self.__items[self.hasheo(valor)]==valor:
            return True
        else:
            i=0
            while self.__items[(self.hasheo(valor)+i)%self.__tamano]!=valor and self.__items[(self.hasheo(valor)+i)%self.__tamano]!=None and i<self.__tamano:
                i+=1
            if self.__items[(self.hasheo(valor)+i)%self.__tamano]==valor:
                return True
            else:
                return False
    def mostrar(self):
        print(self.__items)
if __name__=='__main__':
    h=hashing_abierto(10)
    h.insertar(10)
    h.insertar(20)
    h.insertar(30)
    h.insertar(40)
    h.insertar(50)
    h.insertar(60)
    h.insertar(70)
    h.insertar(80)
    h.insertar(90)
    h.insertar(100)
    h.mostrar()
    print(h.buscar(10))
    print(h.buscar(20))
    print(h.buscar(200))