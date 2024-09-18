from Listas_por_contenido import *
def concatenar(lista1, lista2, lista3):
    i=0
    while i<(lista1.get_cantidad()+lista2.get_cantidad()):
        if i>=lista1.get_cantidad():
            lista3.insertar(lista2.buscar(i-(lista1.get_cantidad())))
        else:
            lista3.insertar(lista1.buscar(i))
        i+=1
if __name__ == '__main__':
    lista1=lista_enlazada()
    lista2=lista_enlazada()
    lista3=lista_enlazada()
    lista1.insertar(1)
    lista1.insertar(2)
    lista1.insertar(3)
    lista1.insertar(4)
    lista1.insertar(5)
    lista2.insertar(6)
    lista2.insertar(7)
    lista2.insertar(8)
    lista2.insertar(10)
    concatenar(lista1, lista2, lista3)
    lista3.recorrer()