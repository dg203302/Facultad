from manejadorclientes import gestcli
from manejadorreparaciones import gestrep
def test():
    gc=gestcli()
    gc.carga()
    gr=gestrep()
    gr.carga()
    while True:
        op=int(input('1 para inciso a, 2 para inciso b, 3 para inciso c, 4 para inciso d, 0 para salir\n-'))
        if op == 0:
            break
        elif op == 1:
            gc.a(gr)
        elif op == 2:
            gr.b(gc)
        elif op == 3:
            gc.c(gr)
        elif op == 4:
            gc.d()
if __name__ == '__main__':
    test()