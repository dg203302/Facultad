from ManejadorEvaluaciones import gestpun
from ManejadorFederados import gestfed
def test():
    gestfede=gestfed()
    gestpunta=gestpun()
    gestfede.agreg()
    gestpunta.agreg()
    op=int(input('ingrese la opcion: 1 para mostrar patinadores, 2 para mostrar mayor puntaje, 3 para listar los patinadores que participaron en estilo libre y escuela, 4 mostrar valoraciones por dni \n -'))
    while True:
        if op == 0:
            break
        elif op == 1:
            gestpunta.a(gestfede)
        elif op == 2:
            gestpunta.b(gestfede)
        elif op == 3:
            gestpunta.c(gestfede)
        elif op == 4:
            gestpunta.d()
        else:
            print('opcion incorrecta!')
        op=int(input('-'))
if __name__ == '__main__':
    test()