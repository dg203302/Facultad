from lista_enlazada import lista
if __name__=='__main__':
    #-------------------listas-------------------#
    lista1=lista()
    lista2=lista()
    for i in range(1,5):
        lista1.insertar_por_posicion(i,i-1)
    for i in range(1,5):
        lista2.insertar_por_posicion(i+4,i-1)
    lista1.mostrar()
    lista2.mostrar()
    #-------------------listas-------------------#
    #-------------------concatenar-------------------#
    lista3=lista1
    lista3.get_ultimo().set_siguiente(lista2.get_primero())
    lista3.mostrar()
    #-------------------concatenar-------------------#