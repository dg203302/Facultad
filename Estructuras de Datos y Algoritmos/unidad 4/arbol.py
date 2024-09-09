class Nodo:
    def __init__(self, valor):
        self.__valor = valor
        self.__izquierdo = None
        self.__derecho = None

    def get_valor(self):
        return self.__valor

    def get_izquierdo(self):
        return self.__izquierdo

    def get_derecho(self):
        return self.__derecho

    def set_izquierdo(self, nodo):
        self.__izquierdo = nodo

    def set_derecho(self, nodo):
        self.__derecho = nodo


class ArbolBinario:
    def __init__(self):
        self.__raiz = None

    def get_raiz(self):
        return self.__raiz

    def insertar(self, valor):
        if self.__raiz is None:
            self.__raiz = Nodo(valor)
        else:
            self.__insertar_recursivo(self.__raiz, valor)

    def __insertar_recursivo(self, nodo, valor):
        if valor < nodo.get_valor():
            if nodo.get_izquierdo() is None:
                nodo.set_izquierdo(Nodo(valor))
            else:
                self.__insertar_recursivo(nodo.get_izquierdo(), valor)
        else:
            if nodo.get_derecho() is None:
                nodo.set_derecho(Nodo(valor))
            else:
                self.__insertar_recursivo(nodo.get_derecho(), valor)

    def buscar(self, valor):
        return self.__buscar_recursivo(self.__raiz, valor)

    def __buscar_recursivo(self, nodo, valor):
        if nodo is None or nodo.get_valor() == valor:
            return nodo
        if valor < nodo.get_valor():
            return self.__buscar_recursivo(nodo.get_izquierdo(), valor)
        return self.__buscar_recursivo(nodo.get_derecho(), valor)