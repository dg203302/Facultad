from Listas_por_posicion import *
def concatenar(lista1, lista2, lista3):
    i=0
    while i<(lista1.get_cantidad()+lista2.get_cantidad()):
        if i>=lista1.get_cantidad():
            lista3.insertar(lista2.buscar(i-(lista1.get_cantidad())), i)
        else:
            lista3.insertar(lista1.buscar(i), i)
        i+=1
if __name__ == '__main__':
    lista1=lista_enlazada()
    lista2=lista_enlazada()
    lista3=lista_enlazada()
    lista1.insertar(1, 0)
    lista1.insertar(2, 1)
    lista1.insertar(3, 2)
    lista1.insertar(4, 3)
    lista1.insertar(5, 4)
    lista2.insertar(6, 0)
    lista2.insertar(7, 1)
    lista2.insertar(8, 2)
    lista2.insertar(9, 3)
    lista2.insertar(10,4)
    concatenar(lista1, lista2, lista3)
    lista3.recorrer()