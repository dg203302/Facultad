from Listas import *
op=input('1 lista secuencial, 2 lista enlazada, 3 lista cursores')
while True:
    if op==0:
        break
    elif op==1:
        print('pruebas para lista secuencial')
        lista=lista_secuencial(5)
        lista.insertar(1,0)
        lista.insertar(2,1)
        lista.insertar(3,2)
        print('ingresando orden')
        lista.mostrar()
        lista.insertar(6,2)
        print('ingresando en un lugar ocupado')
        lista.mostrar()
        lista.recuperar(2)
        '''print('suprimir 1')
        lista.suprimir(0)
        lista.mostrar()
        print('suprimir 2')
        lista.suprimir(1)
        lista.mostrar()
        print('suprimir 3')
        lista.suprimir(2)
        lista.mostrar()'''
        lista.buscar(3)
    elif op==2:
        lista_prueba=lista_enlazada()
        lista_prueba.insertar(12)
        lista_prueba.insertar(10)
        lista_prueba.insertar(213)
        lista_prueba.insertar(320)
        lista_prueba.insertar(3330)
        print('recorriendo desde el inicio')
        lista_prueba.recorrer_desde_el_principio()
        print('recorriendo desde el ultimo')
        lista_prueba.recorrer_desde_el_ultimo()
    op=input('-')