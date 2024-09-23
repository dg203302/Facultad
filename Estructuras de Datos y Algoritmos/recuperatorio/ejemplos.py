def insertar_por_posicion(self,dato,posicion):
    if self.__cantidad<self.__dimension:
        if self.vacia():
            self.__elementos[0]=dato
        else:
            for i in range(self.__cantidad,posicion,-1):
                self.__elementos[i]=self.__elementos[i-1]
            self.__elementos[posicion]=dato
            self.__tope+=1
        self.__cantidad+=1
    else:
        print('lista llena')
def insertar_por_posicion(self,dato,posicion):
    nodo_insertar=nodo(dato)
    if self.vacia():
        self.__primero=nodo_insertar
    elif posicion==0:
        nodo_insertar.set_proximo(self.__primero)
        self.__primero=nodo_insertar
    else:
        i=0
        anterior=self.__primero
        while i<posicion-1:
            anterior=anterior.get_proximo()
            i+=1
        if i==posicion-1:
            nodo_insertar.set_proximo(anterior.get_proximo())
            anterior.set_proximo(nodo_insertar)
def insertar_por_posicion(self,dato,posicion):
    if self.__cantidad<self.__dimension and self.get_disponible():
        nodo_insertar=nodo(dato)
        self.__elementos[self.__disponible]=nodo_insertar
        if self.vacia():
            self.__primero=self.__disponible
        elif posicion==0:
            nodo_insertar.set_proximo(self.__primero)
            self.__primero=self.__disponible
        else:
            i=0
            anterior=self.__primero
            while i<posicion-1:
                anterior=self.__elementos[anterior].get_proximo()
                i+=1
            if i==posicion-1:
                nodo_insertar.set_proximo(self.__elementos[anterior].get_proximo())
                self.__elementos[anterior].set_proximo(self.__disponible)
        self.__cantidad+=1
#inserciones por contenido
def insertar_por_contenido(self,dato):
    if self.__cantidad<self.__dimension:
        if self.vacia():
            self.__elementos[self.__tope]=dato
        else:
            i=0
            while i<self.__cantidad and dato>self.__elementos[i]:
                i+=1
            if dato<self.__elementos[i]:
                for j in range(self.__cantidad,i,-1):
                    self.__elementos[j]=self.__elementos[j-1]
                self.__elementos[i]=dato
                self.__tope+=1
        self.__cantidad+=1
def insertar_por_contenido(self,dato):
    nodo_insertar=nodo(dato)
    if self.vacia():
        self.__primero=nodo_insertar
    else:
        anterior=None
        actual=self.__primero
        while dato>actual.get_dato():
            anterior=actual
            actual=actual.get_proximo()
        if anterior==None:
            nodo_insertar.set_proximo(self.__primero)
            self.__primero=nodo_insertar
        else:
            nodo_insertar.set_proximo(actual)
            anterior.set_proximo(nodo_insertar)
    self.__cantidad+=1
def insertar_por_contenido(self,dato):
    if self.__cantidad<self.__dimension and self.get_disponible():
        nodo_insertar=nodo(dato)
        self.__elementos[self.__disponible]=nodo_insertar
        if self.vacia():
            self.__primero=self.__disponible
        elif dato<self.__elementos[self.__primero].get_dato():
            nodo_insertar.set_proximo(self.__primero)
            self.__primero=self.__disponible
        else:
            anterior=None
            actual=self.__primero
            while actual!=-1 and dato>self.__elementos[actual].get_dato():
                actual=anterior
                actual=actual.get_proximo()
            if actual==-1 or dato<self.__elementos[actual].get_dato():
                nodo_insertar.set_proximo(actual)
                self.__elementos[anterior].set_proximo(self.__disponible)
        self.__cantidad+=1