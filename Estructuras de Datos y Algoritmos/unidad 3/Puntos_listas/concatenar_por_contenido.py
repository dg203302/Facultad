from Listas_por_contenido import *
import time
def concatenar(lista1, lista2, lista3):
    i=0
    while i<(lista1.get_cantidad()+lista2.get_cantidad()):
        if i>=lista1.get_cantidad():
            lista3.insertar(lista2.buscar(i-(lista1.get_cantidad())))
        else:
            lista3.insertar(lista1.buscar(i))
        i+=1
    #calculo de eficiencia
    #1
    #(n+m)-1
        #(m+n)
            #n+2
        #n+1
    #n+m
    
    #1+((n+m)-1)+(m+n)+(n+2)+(n+1)
    #1+((n+m)-1)+(m+n)+n+2+n+1
    #1+((n+m)-1)+m+n+2+n+1
    #1+(n+m)+m+n+2+n
    
    #eficiencia final 3n+2m+3
    
    #O(n+m) aproximado O(n)


    #1
    #(2n)-1
        #(2n)
            #2n^2
        #n^2
    #2n-1
    
    #2n-1+2n+n^2+n^2
    #2n^2+4n-1
    #orden O(n^2)
    
    #eficiencia final 3n+2m+3
if __name__ == '__main__':
    lista1=lista_enlazada()
    lista2=lista_enlazada()
    lista3=lista_enlazada()
    for i in range(1,253):
        if i>(i/2):
            lista2.insertar(i)
        else:
            lista1.insertar(i)
    tiempo_inicial = time.time()
    concatenar(lista1, lista2, lista3)
    tiempo_final = time.time()
    lista3.recorrer()
    print("Tiempo de ejecución: ", tiempo_final-tiempo_inicial)