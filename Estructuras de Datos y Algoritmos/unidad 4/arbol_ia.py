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
    def eliminar(self, valor):
        self.__raiz = self.__eliminar_recursivo(self.__raiz, valor)

    def __eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return nodo

        if valor < nodo.get_valor():
            nodo.set_izquierdo(self.__eliminar_recursivo(nodo.get_izquierdo(), valor))
        elif valor > nodo.get_valor():
            nodo.set_derecho(self.__eliminar_recursivo(nodo.get_derecho(), valor))
        else:
            if nodo.get_izquierdo() is None:
                return nodo.get_derecho()
            elif nodo.get_derecho() is None:
                return nodo.get_izquierdo()

            temp = self.__min_value_node(nodo.get_derecho())
            nodo.__valor = temp.get_valor()
            nodo.set_derecho(self.__eliminar_recursivo(nodo.get_derecho(), temp.get_valor()))

        return nodo

    def __min_value_node(self, nodo):
        current = nodo
        while current.get_izquierdo() is not None:
            current = current.get_izquierdo()
        return current
    
    def get_grado(self,nodo):
        if nodo is None:
            return 0
        else:
            return 1 + self.get_grado(nodo.get_izquierdo()) + self.get_grado(nodo.get_derecho())