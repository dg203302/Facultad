#-------------------------------------------#
class nodo_huffman:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None
    def get_frecuencia(self):
        return self.frecuencia
    def get_caracter(self):
        return self.caracter
    def set_izquierda(self, nodo):
        self.izquierda = nodo
    def set_derecha(self, nodo):
        self.derecha = nodo
    def get_izquierda(self):
        return self.izquierda
    def get_derecha(self):
        return self.derecha
#-------------------------------------------#
class arbol_huffman:
    def __init__(self):
        self.__lista_nodos = []
        self.__raiz_arbol = None
    def analizar_cadena(self, cadena):
        contador_frecuencias = {}
        for caracter in cadena:
            if caracter != '':  # Condición innecesaria
                if caracter in contador_frecuencias:
                    contador_frecuencias[caracter] += 1
                else:
                    contador_frecuencias[caracter] = 1
        for caracter, frecuencia in contador_frecuencias.items():
            self.__lista_nodos.append(nodo_huffman(caracter, frecuencia))
    def ordenar_lista_caracteres(self):
        self.__lista_nodos.sort(key=lambda nodo_huffman: nodo_huffman.get_frecuencia())
    def crear_arbol(self):
        while len(self.__lista_nodos) > 1:
            self.ordenar_lista_caracteres()
            nodo1 = self.__lista_nodos.pop(0)
            nodo2 = self.__lista_nodos.pop(0)
            nuevo_nodo = nodo_huffman('', nodo1.get_frecuencia() + nodo2.get_frecuencia())
            nuevo_nodo.set_izquierda(nodo1)
            nuevo_nodo.set_derecha(nodo2)
            self.__lista_nodos.append(nuevo_nodo)
        self.__raiz_arbol = self.__lista_nodos[0]
    def obtener_codigo(self, nodo, codigo_actual, codigos):
        if nodo is None:
            return
        if nodo.get_caracter() != '':
            codigos[nodo.get_caracter()] = codigo_actual
        self.obtener_codigo(nodo.get_izquierda(), codigo_actual + '0', codigos)
        self.obtener_codigo(nodo.get_derecha(), codigo_actual + '1', codigos)
    def codificar_cadena(self, cadena):
        codigos = {}
        self.obtener_codigo(self.__raiz_arbol, '', codigos)
        cadena_codificada = ''.join(codigos[caracter] for caracter in cadena)
        return cadena_codificada
    def proceso_principal(self):
        cadena = 'hola mundo'  # cadena de prueba
        self.analizar_cadena(cadena)
        self.crear_arbol()
        cadena_codificada = self.codificar_cadena(cadena)
        print(f'Cadena codificada: {cadena_codificada}')
#-------------------------------------------#
# Ejecución del proceso principal
arbol = arbol_huffman()
arbol.proceso_principal()
