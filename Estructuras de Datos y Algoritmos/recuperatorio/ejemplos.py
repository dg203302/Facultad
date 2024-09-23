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
        else:
            i=0
            actual=self.__primero
            anterior=None
            while i<posicion and i<self.__cantidad:
                i+=1
                anterior=actual
                actual=self.__elementos[actual].get_siguiente()
            if anterior==None:
                nodo_insertar.set_siguiente(self.__primero)
                self.__primero=self.__disponible
            else:
                nodo_insertar.set_siguiente(actual)
                self.__elementos[anterior].set_siguiente(self.__disponible)
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
#suprimir
def suprimir_por_posicion(self,posicion):
    if not self.vacia() and posicion<=0 and posicion<=self.__tope:
        dato_recuperar=self.__elementos[posicion]
        for i in range(posicion,self.__cantidad):
            self.__items[i]=self.__items[i+1]
        self.__tope-=1
        self.__cantidad-=1
        return dato_recuperar
def suprimir_por_contenido(self,dato):
    if not self.vacia():
        i=0
        while dato!=self.__elementos[i] and i<self.__cantidad:
            i+=1
        if dato==self.__elementos[i]:
            dato_recuperar=self.__elementos[i]
            for j in range(i,self.__cantidad):
                self.__elementos[j]=self.__elementos[j+1]
            self.__tope-=1
            self.__cantidad-=1
            return dato_recuperar
def suprimir_por_posicion(self,posicion):
    if not self.vacia():
        if posicion==0:
            dato_recuperar=self.__primero.get_dato()
            self.__primero=self.__primero.get_siguiente()
            self.__cantidad-=1
        else:
            i=0
            anterior=None
            actual=self.__primero
            while i!=posicion:
                anterior=actual
                actual=actual.get_siguiente()
                i+=1
            if i==posicion:
                dato_recuperar=actual.get_dato()
                anterior.set_siguiente(actual.get_siguiente())
                self.__cantidad-=1
                return dato_recuperar
def suprimir_por_contenido(self,dato):
    if not self.vacia():
        if dato==self.__primero.get_dato():
            dato_recuperar=self.__primero.get_dato()
            self.__primero=self.__primero.get_siguiente()
            self.__cantidad-=1
            return dato_recuperar
        else:
            anterior=None
            actual=self.__primero
            while dato!=actual.get_dato():
                anterior=actual
                actual=actual.get_siguiente()
            if dato==actual.get_dato():
                dato_recuperar=actual.get_dato()
                anterior.set_siguiente(actual.get_siguiente())
                self.__cantidad-=1
                return dato_recuperar
def suprimir_por_posicion(self,posicion):
    if not self.vacia():
        if posicion==0:
            dato_recuperar=self.__elementos[self.__primero].get_dato()
            self.__primero=self.__elementos[self.__primero].get_siguiente()
            self.__cantidad-=1
            return dato_recuperar
        else:
            i=0
            anterior=None
            actual=self.__primero
            while i<posicion:
                anterior=actual
                actual=self.__elementos[actual].get_siguiente()
                i+=1
            if i==posicion:
                dato_recuperar=self.__elementos[actual].get_dato()
                self.__elementos[anterior].set_siguiente(self.__elementos[actual].get_siguiente())
                self.__cantidad-=1
                return dato_recuperar
