class lista_secuencial:
    __dimension:int
    __tope:int
    __cantidad:int
    __items:list
    def __init__(self,dimension=0):
        self.__dimension=dimension
        self.__tope=-1
        self.__cantidad=0
        self.__items=[0]*self.__dimension
    def vacia(self):
        return self.__cantidad==0
    def insertar_por_posicion(self,dato,posicion):
        if self.__cantidad<self.__dimension:
            if self.vacia():
                self.__tope+=1
                self.__items[self.__tope]=dato
            else:
                for i in range(self.__tope+1,posicion,-1):
                    self.__items[i]=self.__items[i-1]
                self.__items[posicion]=dato
            self.__cantidad+=1
        else:
            print('lista llena')
    def insertar_por_contenido(self,dato):
        if self.__cantidad<self.__dimension:
            if self.vacia():
                self.__tope+=1
                self.__items[self.__tope]=dato
            else:
                i=0
                while i < self.__cantidad and dato > self.__items[i]:
                    i+=1
                for j in range(self.__cantidad, i, -1):
                    self.__items[j] = self.__items[j-1]
                self.__items[i] = dato
                self.__tope += 1
            self.__cantidad += 1
        else:
            print('lista llena')
    def recorrer(self):
        for i in range(0,self.__cantidad):
            print(self.__items[i],end=' ')
    def suprimir_por_posicion(self,posicion):
        if not self.vacia():
            for i in range(posicion,self.__cantidad):
                self.__items[i]=self.__items[i+1]
            self.__cantidad-=1
        else:
            print('lista vacia')
    def suprimir_por_contenido(self,dato):
        if not self.vacia():
            if dato==self.__items[self.__tope]:
                self.__tope-=1
            else:
                i=0
                while dato!=self.__items[i]:
                    i+=1
                for j in range(i,self.__cantidad):
                    self.__items[j]=self.__items[j+1]
                self.__tope-=1
            self.__cantidad-=1
    def get_primero(self):
        pass
    def get_ultimo(self):
        pass
    def buscar(self):
        pass
    def get_siguiente_elem(self,dato):
        pass
    def get_elem_anterior(self,dato):
        pass
if __name__ == "__main__":
    lista = lista_secuencial(dimension=10)
    lista.insertar_por_posicion(5, 0)
    lista.insertar_por_posicion(10, 1)
    lista.insertar_por_posicion(15, 2)
    lista.insertar_por_posicion(100,3)
    lista.recorrer()
    lista.suprimir_por_contenido(100)
    lista.suprimir_por_posicion(1)
    '''
    lista.insertar_por_contenido(5)
    lista.insertar_por_contenido(10)
    lista.insertar_por_contenido(15)
    lista.insertar_por_contenido(100)
    lista.insertar_por_contenido(0)
    '''
    lista.recorrer()