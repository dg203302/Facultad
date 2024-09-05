class nodo_cursor:
    __dato:object
    __siguiente:int
    def __init__(self,dato=None,siguiente=-1):
        self.__dato=dato
        self.__siguiente=siguiente
    def get_dato(self):
        return self.__dato
    def get_siguiente(self):
        return int(self.__siguiente)
    def set_siguiente(self,siguiente):
        self.__siguiente=siguiente
class lista_cursor:
    __primer_elemento:int
    __cantidad_elementos:int
    __dimension:int
    __elementos:list
    __disponible:int
    def __init__(self,dimension=0):
        self.__dimension=dimension
        self.__cantidad_elementos=0
        self.__disponible=0
        self.__primer_elemento=0
        self.__elementos=[nodo_cursor()]*self.__dimension
    def buscar_vacio(self):
        if self.__cantidad_elementos==0:
            self.__disponible=self.__primer_elemento
            return True
        else:
            i=0
            while i<self.__cantidad_elementos and self.__elementos[i].get_siguiente()!=-1:
                i+=1
            if self.__elementos[i].get_siguiente()==-1:
                self.__disponible=i+1
                return True
            else:
                return False
    def insertar_en_posicion(self,dato,indice_insertar):
        if self.__cantidad_elementos<self.__dimension and self.buscar_vacio():
            nodo_a_insertar=nodo_cursor(dato)
            self.__elementos[self.__disponible]=nodo_a_insertar
            if self.__cantidad_elementos==0:
                self.__cantidad_elementos+=1              #primer elemento, independientemente del indice
            else:
                i=self.__primer_elemento
                while i<indice_insertar:
                    i+=1
                if i==indice_insertar:
                    print(f'indice de la busqueda: {i}, indice del insertado: {self.__disponible}')
                    if i==self.__disponible or self.__elementos[i].get_dato()==None:                  #al final
                        self.__elementos[i-1].set_siguiente(self.__disponible)
                        self.__cantidad_elementos+=1
                    elif i!=self.__disponible or self.__elementos[i]!=None:                           #en el medio
                        if i==0:                                                                      #caso particular de que sea al inicio
                            self.__elementos[self.__disponible].set_siguiente(self.__primer_elemento)
                            self.__primer_elemento=self.__disponible
                            self.__cantidad_elementos+=1
                        else:                                                                         #en el medio ahora si
                            self.__elementos[self.__disponible].set_siguiente(i)
                            self.__elementos[i-1].set_siguiente(self.__disponible)
                            self.__cantidad_elementos+=1    
        else:
            print('lista llena!')
    def recorrer_rudimentario(self):
        i=self.__primer_elemento
        while self.__elementos[i].get_siguiente()!=-1:
            print(f'CONTENIDO: {self.__elementos[i].get_dato()}\nSIGUIENTE: {self.__elementos[i].get_siguiente()}\n')
            i=self.__elementos[i].get_siguiente()
        print(f'CONTENIDO: {self.__elementos[i].get_dato()}\nSIGUIENTE: {self.__elementos[i].get_siguiente()}\ncantidad de elementos: {self.__cantidad_elementos}') #esto para que muestre el ultimo
if __name__=='__main__':
    '''
    lista_prueba=lista_cursor(3)
    lista_prueba.insertar_en_posicion(21,0)
    lista_prueba.insertar_en_posicion(12,1)
    lista_prueba.insertar_en_posicion(31,0)
    lista_prueba.recorrer_rudimentario()
    '''