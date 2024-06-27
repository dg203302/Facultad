from lkdlst import *
def test():
    lista=lkdlist()
    lista.carga()
    op=int(input('1 para inciso a, 2 para inciso b, 3 para inciso c, 4 para inciso d, 0 para salir\n-'))
    while op!=0:
        if op==1:
            lista.a()
        elif op==2:
            lista.b()
        elif op==3:
            lista.c()
        elif op==4:
            lista.d()
        op=int(input('-'))
if __name__ == '__main__':
    test()