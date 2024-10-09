#si esta ocupado moverme con el modulo
class hashing_abierto:
    __items:list
    __tamano:int
    __cantidad_elementos:int
    def __init__(self, tamano:int):
        self.__items=[None]*tamano
        self.__tamano=tamano
        self.__cantidad_elementos=0
#---------------------------------------------------------#
    def hasheo_modulo(self, clave):
        return clave%self.__tamano
    def insertar_modulo(self, valor):
        if self.__cantidad_elementos==self.__tamano:
            print('Tabla llena')
            return
        else:
            if self.__items[self.hasheo_modulo(valor)]==None:
                print('colisiones en la insercion:',0)
                self.__items[self.hasheo_modulo(valor)]=valor
                self.__cantidad_elementos+=1
            else:
                i=0
                while self.__items[self.hasheo_modulo((self.hasheo_modulo(valor)+i))%self.__tamano]!=None and i<self.__tamano:
                    i+=1
                print('colisiones en la insercion:',i)
                self.__items[self.hasheo_modulo(self.hasheo_modulo(valor)+i)]=valor
                self.__cantidad_elementos+=1
    def buscar_modulo(self, valor):
        if self.__items[self.hasheo_modulo(valor)]==valor:
            return True
        else:
            i=0
            while self.__items[(self.hasheo_modulo(valor)+i)%self.__tamano]!=valor and self.__items[(self.hasheo_modulo(valor)+i)%self.__tamano]!=None and i<self.__tamano:
                i+=1
            if self.__items[(self.hasheo_modulo(valor)+i)%self.__tamano]==valor:
                print('colisiones en la busqueda:',i)
                return True
            else:
                return False
#---------------------------------------------------------------#
    def hasheo_cuadrado_medio(self, clave):
        return (clave**2 // 100 % 100) % self.__tamano
    def insertar_cuadrado_medio(self, valor):
        if self.__cantidad_elementos==self.__tamano:
            print('Tabla llena')
            return
        else:
            if self.__items[self.hasheo_cuadrado_medio(valor)]==None:
                print('colisiones en la insercion:',0)
                self.__items[self.hasheo_cuadrado_medio(valor)]=valor
                self.__cantidad_elementos+=1
            else:
                i=0
                while self.__items[(self.hasheo_cuadrado_medio(valor)+i) % self.__tamano] != None and i < self.__tamano:
                    i+=1
                print('colisiones en la insercion:',i)
                self.__items[(self.hasheo_cuadrado_medio(valor)+i) % self.__tamano]=valor
                self.__cantidad_elementos+=1
    #implementar busqueda cuadrado medio
#---------------------------------------------------------------#
    def hasheo_plegado(self,valor):
        #for con paso 3
        str_valor = str(valor)
        ac = 0
        for char in str_valor:
            ac += int(char)
        return ac % self.__tamano
    def insertar_plegado(self,valor):
        if self.__cantidad_elementos==self.__tamano:
            print('Tabla llena')
            return
        else:
            if self.__items[self.hasheo_plegado(valor)]==None:
                print('colisiones en la insercion:',0)
                self.__items[self.hasheo_plegado(valor)]=valor
                self.__cantidad_elementos+=1
            else:
                i=0
                while self.__items[(self.hasheo_plegado(valor)+i) % self.__tamano] != None and i < self.__tamano:
                    i+=1
                print('colisiones en la insercion:',i)
                self.__items[(self.hasheo_plegado(valor)+i) % self.__tamano]=valor
                self.__cantidad_elementos+=1
    #implementar busqueda plegado
#---------------------------------------------------------------#
    def hasheo_extraccion(self, valor):
        str_valor = str(valor)
        ac = 0
        for i in range(0,int(len(str_valor)/2)):    #esto para plegado, para extraccion es lo mismo pero con la mitad de caracteres.
            ac += int(str_valor[i])
        return ac % self.__tamano
    def insertar_extraccion(self, valor):
        if self.__cantidad_elementos == self.__tamano:
            print('Tabla llena')
            return
        else:
            if self.__items[self.hasheo_extraccion(valor)] == None:
                print('colisiones en la insercion:', 0)
                self.__items[self.hasheo_extraccion(valor)] = valor
                self.__cantidad_elementos += 1
            else:
                i = 0
                while self.__items[(self.hasheo_extraccion(valor) + i) % self.__tamano] != None and i < self.__tamano:
                    i += 1
                print('colisiones en la insercion:', i)
                self.__items[(self.hasheo_extraccion(valor) + i) % self.__tamano] = valor
                self.__cantidad_elementos += 1
    def mostrar(self):
        print(self.__items)
if __name__=='__main__':
    print('----------------METODO MODULO--------------------')
    h1=hashing_abierto(5)
    h1.insertar_modulo(10)
    h1.insertar_modulo(20)
    h1.insertar_modulo(30)
    h1.insertar_modulo(40)
    h1.insertar_modulo(50)
    #overflow
    h1.insertar_modulo(65)
    h1.insertar_modulo(75)
    #overflow
    h1.mostrar()
    print('----------------METODO CUADRADO--------------------')
    h2=hashing_abierto(5)
    h2.insertar_cuadrado_medio(10)
    h2.insertar_cuadrado_medio(20)
    h2.insertar_cuadrado_medio(30)
    h2.insertar_cuadrado_medio(40)
    h2.insertar_cuadrado_medio(50)
    #overflow
    h2.insertar_cuadrado_medio(65)
    h2.insertar_cuadrado_medio(75)
    #overflow
    h2.mostrar()
    print('----------------METODO PLEGADO--------------------')
    h3=hashing_abierto(5)
    h3.insertar_plegado(10)
    h3.insertar_plegado(20)
    h3.insertar_plegado(30)
    h3.insertar_plegado(40)
    h3.insertar_plegado(50)
    #overflow
    h3.insertar_plegado(65)
    h3.insertar_plegado(75)
    #overflow
    h3.mostrar()
    print('----------------METODO EXTRACCION--------------------')
    h4=hashing_abierto(5)
    h4.insertar_extraccion(10)
    h4.insertar_extraccion(20)
    h4.insertar_extraccion(30)
    h4.insertar_extraccion(40)
    h4.insertar_extraccion(50)
    #overflow
    h4.insertar_extraccion(65)
    h4.insertar_extraccion(75)
    #overflow
    h4.mostrar()