#-----------------------------------------COLUMNAS-----------------------------------------#
class sub_lista:
    __items_columnas: list
    __cantidad_columnas: int
    __tamano_columnas: int
    def __init__(self, tamano_columnas):
        self.__items_columnas = [None] * tamano_columnas
        self.__cantidad_columnas = 0
        self.__tamano_columnas = tamano_columnas
    def verificar(self):
        return self.__cantidad_columnas == self.__tamano_columnas
    def cargar(self, valor):
        self.__items_columnas[self.__cantidad_columnas] = valor
        self.__cantidad_columnas += 1
    def get_item_busqueda(self, valor):
        i = 0
        while i < self.__tamano_columnas and self.__items_columnas[i] != valor:
            i += 1
        if i < self.__tamano_columnas:
            return True
        else:
            return False
    def get_item_recorrer(self,indice):
        return self.__items_columnas[indice]
    def get_cantidad(self):
        return self.__cantidad_columnas
#-----------------------------------------FILAS-----------------------------------------#
#agregar area de overflow
class hash_bucket:
    __items_filas: list
    __tamano_filas: int
    __tamano_filas_overflow: int
    __items_overflow: list
    __cantidad_filas: int
    def __init__(self, cantidad_elementos, tamano_columnas):
        self.__tamano_filas=int(cantidad_elementos / tamano_columnas)
        self.__tamano_filas_overflow = int(self.__tamano_filas*0.2)
        self.__items_filas = [sub_lista(tamano_columnas) for _ in range(self.__tamano_filas)]
        self.__items_overflow= [sub_lista(tamano_columnas) for _ in range(self.__tamano_filas_overflow)]
        self.__cantidad_filas = 0
#----------------------------------------HASHEO----------------------------------------#
    def hasheo_modulo(self, clave):
        return clave % self.__tamano_filas
#-----------------------------------------INSERTAR-----------------------------------------#
    def insertar(self, valor):
        indice = self.hasheo_modulo(valor)
        if self.__items_filas[indice].verificar():
            indice_busqueda=0
            while self.__items_overflow[indice_busqueda].verificar():
                indice_busqueda+=1
            if indice_busqueda == len(self.__items_overflow):
                print('Overflow lleno')
            else:
                self.__items_overflow[indice_busqueda].cargar(valor)
            return
        else:
            self.__items_filas[indice].cargar(valor)
            self.__cantidad_filas += 1
#-----------------------------------------BUSCAR-----------------------------------------#
    def buscar(self, valor):
        indice = self.hasheo_modulo(valor)
        if self.__items_filas[indice].get_cantidad() == 0:
            print('No se encontro el valor')
            return
        elif self.__items_filas[indice].get_item_busqueda(valor) == False:
            indice=0
            while self.__items_overflow[indice].get_item_busqueda(valor)==False and indice<self.__tamano_filas_overflow:
                indice+=1
            if indice == len(self.__items_overflow):
                print('No se encontro el valor')
            else:
                print('Se encontro el valor en overflow')
        else:
            print('Se encontro el valor')
#-----------------------------------------RECORRER-----------------------------------------#
    def recorrer(self):
        for i in range(self.__tamano_filas):
            cadena = '['
            for j in range(self.__items_filas[i].get_cantidad()):
                cadena += str(self.__items_filas[i].get_item_recorrer(j)) + ','
            cadena = cadena.rstrip(',') + ']'
            print(f'{i} --> {cadena}')
        print('----------------Overflow----------------')
        for i in range(len(self.__items_overflow)):
            cadena = '['
            for j in range(self.__items_overflow[i].get_cantidad()):
                cadena += str(self.__items_overflow[i].get_item_recorrer(j)) + ','
            cadena = cadena.rstrip(',') + ']'
            print(f'{i} --> {cadena}')
#---------------------------------------------MAIN---------------------------------------------#
if __name__=='__main__':
    cantidad_elementos=100#int(input('Ingrese la cantidad de elementos: '))
    cantidad_columnas=5#int(input('Ingrese la cantidad de columnas: '))
    hasheo_bucket = hash_bucket(cantidad_elementos, cantidad_columnas)
    hasheo_bucket.insertar(10)
    hasheo_bucket.insertar(20)
    hasheo_bucket.insertar(30)
    hasheo_bucket.insertar(40)
    hasheo_bucket.insertar(50)
    hasheo_bucket.insertar(60)
    hasheo_bucket.insertar(70)
    hasheo_bucket.buscar(70)
    hasheo_bucket.buscar(10)
    hasheo_bucket.recorrer()