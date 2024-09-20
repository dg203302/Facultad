class pila:
    __dimension:int
    __cantidad:int
    __tope:int
    __items:list
    def __init__(self,dimension=0):
        self.__dimension=dimension
        self.__cantidad=0
        self.__tope=-1
        self.__items=[0]*dimension
    def vacia(self):
        return self.__tope==-1
    def insertar(self,dato):
        if self.__cantidad<self.__dimension:
            self.__tope+=1
            self.__items[self.__tope]=dato
            self.__cantidad+=1
        else:
            print('pila llena!')
    def suprimir(self):
        if not self.vacia():
            item_a_suprimir=self.__items[self.__tope]
            self.__tope-=1
            self.__cantidad-=1
            return item_a_suprimir
        else:
            print('pila vacia!')
    def recorrer(self):
        for i in range(self.__tope,-1,-1):
            print(self.__items[i], end='')