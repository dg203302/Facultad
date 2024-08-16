class pila:
    __dimension:int
    __cantidad_elementos:int
    __items:list
    __tope:int
    def __init__(self,dimension=0):
        self.__dimension=dimension
        self.__items=[0]*self.__dimension
        self.__cantidad_elementos=0
        self.__tope=-1
    def verificar_pila(self):
        return (self.__tope==0)
    def agregar(self,elemento):
        if self.__cantidad_elementos<self.__dimension:
            self.__tope+=1
            self.__items[self.__tope]=elemento
            self.__cantidad_elementos+=1
        else:
            raise IndexError
    def mostrar(self):
        if not(self.verificar_pila()):
            for i in range(self.__tope,-1,-1):
                print(self.__items[i])
        else:
            print('pila no cargada')
    def suprimir(self):
        if self.__cantidad_elementos<=self.__cantidad_elementos:
            for i in range(self.__tope,-1,-1):
                self.__items[i]=0
pila_ejemplo=pila(3)
pila_ejemplo.agregar(29)
pila_ejemplo.agregar(2939)
pila_ejemplo.agregar(293)
pila_ejemplo.mostrar()
try:
    pila_ejemplo.agregar(32)
except IndexError:
    print('pila llena!!')
pila_ejemplo.suprimir()
pila_ejemplo.mostrar()