from ManejadorEvaluaciones import gestpun
from ManejadorFederados import gestfed
def test():
    gestfede=gestfed()
    gestpunta=gestpun()
    gestfede.agreg()
    gestpunta.agreg()
    op=int(input('ingrese la opcion: 1 para cargar los csv, 2 para mostrar patinadores, 3 para mostrar mayor puntaje, 4 para listar los patinadores que participaron en estilo libre y escuela, 5 mostrar valoraciones por dni \n -'))
    while True:
        if op == 0:
            break
        elif op == 2:
            gestpunta.a(gestfede)
        elif op == 3:
            gestpunta.b(gestfede)
        elif op == 4:
            gestpunta.c(gestfede)
        elif op == 5:
            gestpunta.d()
        op=int(input('-'))
if __name__ == '__main__':
    test()