class cola_secuencial:
    __dimension:int
    __cantidad:int
    __primero:int
    __ultimo:int
    __items:list
    def __init__(self,dimension=0):
        self.__dimension=dimension
        self.__cantidad=0
        self.__ultimo=0
        self.__primero=0
        self.__items=[0]*dimension
    def vacia(self):
        return self.__cantidad==0
    def insertar(self,dato):
        if self.__cantidad<self.__dimension:
            self.__ultimo=(self.__ultimo+1)%self.__dimension     #importante
            self.__items[self.__ultimo]=dato
            self.__cantidad+=1
        else:
            print('cola llena!')
    def recorrer(self):
        if not self.vacia():
            i = self.__primero
            j = 0
            while j < self.__cantidad:
                print(self.__items[i], end=' ')
                i = (i + 1) % self.__dimension
                j += 1
        else:
            print('cola vacia!')
    def suprimir(self):
        if not self.vacia():
            elem_suprimir=self.__items[self.__primero]
            self.__primero=(self.__primero+1)%self.__dimension     #importante
            self.__cantidad-=1
            return elem_suprimir
        else:
            print('cola vacia!')
'''
# Crear una instancia de la cola
cola = cola_secuencial(dimension=5)
# Insertar elementos en la cola
cola.insertar(10)
cola.insertar(20)
cola.insertar(30)
cola.insertar(40)
cola.insertar(50)
#cola.insertar(60)
# Mostrar los elementos de la cola
cola.recorrer()
# Suprimir elementos de la cola
print(f'elemento suprimido: {cola.suprimir()}')
print(f'elemento suprimido: {cola.suprimir()}')
cola.recorrer()
'''