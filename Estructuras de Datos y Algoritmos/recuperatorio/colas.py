class cola_secuencial:
    __dimension:int
    __cantidad:int
    __primero:int
    __ultimo:int
    __items:list
    def __init__(self,dimension=0):
        self.__dimension=dimension
        self.__cantidad=0
        self.__tope=-1
        self.__primero=0
        self.__items=[0]*dimension
    def vacia(self):
        return self.__cantidad==0
    def insertar(self,dato):
        if self.__cantidad<self.__dimension:
            self.__tope+=1
            self.__items[self.__tope]=dato
            self.__cantidad+=1
        else:
            print('cola llena!')
    def suprimir(self):
        if not self.vacia():
            elem_suprimir=self.__items[self.__primero]
            self.__primero+= 1
            self.__cantidad-=1
            if self.__primero>self.__ultimo:
                self.__primero=0
                self.__tope=-1
            return elem_suprimir
        else:
            print('cola vacia!')
    #probar ahora en calse