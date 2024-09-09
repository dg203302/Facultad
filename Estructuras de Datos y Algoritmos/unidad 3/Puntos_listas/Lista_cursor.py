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
        self.__elementos=[None]*self.__dimension
        self.__cantidad_elementos=0
        self.__disponible=-1
        self.__primer_elemento=0
    def buscar_vacio(self):
        i=0
        while i<self.__dimension:
            if self.__elementos[i]==None:
                self.__disponible=i
                return True
<<<<<<< HEAD
            else:
                return False
    #revisar despues
=======
            i+=1
        return False
>>>>>>> 6f30713c29746c2b364a90287d296397b67b51b5
    def insertar_en_posicion(self,dato,indice_insertar):
        if self.__cantidad_elementos<self.__dimension and self.buscar_vacio():
            nodo_a_insertar=nodo_cursor(dato)
            self.__elementos[self.__disponible]=nodo_a_insertar
            if self.__cantidad_elementos==0:
                self.__primer_elemento=self.__disponible
                self.__cantidad_elementos+=1
            elif indice_insertar==0:
                self.__elementos[self.__disponible].set_siguiente(self.__primer_elemento)
                self.__primer_elemento=self.__disponible
                self.__cantidad_elementos+=1
            else:
<<<<<<< HEAD
                i=self.__primer_elemento
                while i<indice_insertar:
                    i+=1
                if i==indice_insertar:
                    if i==self.__disponible or self.__elementos[i].get_dato()==None:                  #al final
                        self.__elementos[i-1].set_siguiente(self.__disponible)
                        self.__cantidad_elementos+=1
                    elif i!=self.__disponible or self.__elementos[i]!=None:                           #en el medio
                        if i==0:                                                                      #caso particular de que sea al inicio
                            self.__elementos[self.__disponible].set_siguiente(self.__primer_elemento)
                            self.__primer_elemento=self.__disponible
                            self.__cantidad_elementos+=1
                        elif i!=0 or i==self.__primer_elemento:                                                                         #en el medio ahora si
                            self.__elementos[self.__disponible].set_siguiente(i)
                            self.__elementos[i-1].set_siguiente(self.__disponible)
                            self.__cantidad_elementos+=1    
        else:
            print('lista llena!')
    #hacer busqueda, siguiente, anterior
    def busqueda_por_contenido(self,dato):
        i=self.__primer_elemento
        while self.__elementos[i].get_siguiente()!=-1 and self.__elementos[i].get_dato()!=dato:
            i=self.__elementos[i].get_siguiente()
        if self.__elementos[i].get_dato()==dato:
            if i==self.__primer_elemento:
                return 0
            else:
                return i+1
=======
                anterior=self.__primer_elemento
                for j in range(indice_insertar-1):
                    anterior=self.__elementos[anterior].get_siguiente()
                nodo_a_insertar.set_siguiente(self.__elementos[anterior].get_siguiente())
                self.__elementos[anterior].set_siguiente(self.__disponible)
                self.__cantidad_elementos+=1
        else:
            print('lista llena!')
        #ingresar por dato / comparar y en la busqueda ver que sea menor / si es menor al principio y asi
    def recorrer(self):
        if self.__cantidad_elementos!=0:
            cabeza = self.__primer_elemento
            print("Lista:", end=" ")
            while cabeza!=-1:
                print(self.__elementos[cabeza].get_dato(), end=" ")
                cabeza=self.__elementos[cabeza].get_siguiente()
            print()
        else:
            print("Lista vacía.")
>>>>>>> 6f30713c29746c2b364a90287d296397b67b51b5
    def recorrer_rudimentario(self):
        i=self.__primer_elemento
        while self.__elementos[i].get_siguiente()!=-1:
            print(f'CONTENIDO: {self.__elementos[i].get_dato()}\nSIGUIENTE: {self.__elementos[i].get_siguiente()}\n')
            i=self.__elementos[i].get_siguiente()
        print(f'CONTENIDO: {self.__elementos[i].get_dato()}\nSIGUIENTE: {self.__elementos[i].get_siguiente()}\ncantidad de elementos: {self.__cantidad_elementos}') #esto para que muestre el ultimo
if __name__=='__main__':
<<<<<<< HEAD
    lista_prueba=lista_cursor(5)
    lista_prueba.insertar_en_posicion(1,0)
    lista_prueba.insertar_en_posicion(2,1)
    lista_prueba.insertar_en_posicion(3,2)
    lista_prueba.insertar_en_posicion(4,0)
    lista_prueba.insertar_en_posicion(5,3)
    lista_prueba.recorrer_rudimentario()
    print(f'dato 1 en la posicion: {lista_prueba.busqueda_por_contenido(31)}')
    print(f'dato 2 en la posicion: {lista_prueba.busqueda_por_contenido(21)}')
    print(f'dato 3 en la posicion: {lista_prueba.busqueda_por_contenido(12)}')
=======
    
    lista_prueba=lista_cursor(5)
    lista_prueba.insertar_en_posicion(21,0)
    lista_prueba.insertar_en_posicion(12,1)
    lista_prueba.insertar_en_posicion(31,0)
    lista_prueba.insertar_en_posicion(231,2)
    lista_prueba.recorrer()
    
>>>>>>> 6f30713c29746c2b364a90287d296397b67b51b5
