from colas import *
cola=cola_secuencial(3)
cola.insertar(1)
cola.insertar(2)
cola.insertar(3)
cola.recorrer()
print(f'cantidad de elementos antes de suprimir: {cola.get_cantidad()}')
print('ahora suprimo')
cola.suprimir_primero()
cola.recorrer()
print(f'cantidad de elementos despues de suprimir: {cola.get_cantidad()}')