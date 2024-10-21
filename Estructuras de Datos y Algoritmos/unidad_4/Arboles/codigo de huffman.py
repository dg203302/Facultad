import heapq
from collections import defaultdict, Counter

class Nodo:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

def construir_arbol_huffman(caracteres):
    frecuencias = Counter(caracteres)
    cola = [Nodo(caracter, frecuencia) for caracter, frecuencia in frecuencias.items()]
    heapq.heapify(cola)
    while len(cola) > 1:
        nodo_izquierda = heapq.heappop(cola)
        nodo_derecha = heapq.heappop(cola)
        nueva_frecuencia = nodo_izquierda.frecuencia + nodo_derecha.frecuencia
        nuevo_nodo = Nodo(None, nueva_frecuencia)
        nuevo_nodo.izquierda = nodo_izquierda
        nuevo_nodo.derecha = nodo_derecha
        heapq.heappush(cola, nuevo_nodo)
    return heapq.heappop(cola)

def crear_codigo_huffman(raiz):
    codigo = {}
    def _crear_codigo_huffman(nodo, codigo_actual):
        if nodo is None:
            return
        if nodo.caracter is not None:
            codigo[nodo.caracter] = codigo_actual
        _crear_codigo_huffman(nodo.izquierda, codigo_actual + "0")
        _crear_codigo_huffman(nodo.derecha, codigo_actual + "1")
    _crear_codigo_huffman(raiz, "")
    return codigo

def codificar(cadena, codigo_huffman):
    return ''.join(codigo_huffman[caracter] for caracter in cadena)

def decodificar(cadena_codificada, raiz):
    resultado = []
    nodo_actual = raiz
    for bit in cadena_codificada:
        nodo_actual = nodo_actual.izquierda if bit == '0' else nodo_actual.derecha
        if nodo_actual.caracter is not None:
            resultado.append(nodo_actual.caracter)
            nodo_actual = raiz
    return ''.join(resultado)

# Lectura del archivo
nombre_archivo = 'archivo.txt'
with open(nombre_archivo, 'r') as file:
    contenido = file.read()

# Compresión utilizando Huffman
raiz = construir_arbol_huffman(contenido)
codigo_huffman = crear_codigo_huffman(raiz)
cadena_codificada = codificar(contenido, codigo_huffman)

# Almacenamiento del archivo comprimido
nombre_archivo_comprimido = 'archivo_comprimido.bin'
with open(nombre_archivo_comprimido, 'wb') as file:
    file.write(cadena_codificada.encode())

print("Archivo comprimido con éxito!")

# Descompresión para verificación
cadena_decodificada = decodificar(cadena_codificada, raiz)
print("Archivo descomprimido:", cadena_decodificada)

# Opcional: Guardar el archivo descomprimido
nombre_archivo_descomprimido = 'archivo_descomprimido.txt'
with open(nombre_archivo_descomprimido, 'w') as file:
    file.write(cadena_decodificada)
