from lkdlst import *
def test():
    lista=lkdlist()
    lista.carga()
    try:
        op=int(input('1 para insertar, 2 para mostrar\n-'))
        while op!=0:
            if op==1:
                lista.insertar()
            elif op==2:
                lista.most()
            op=int(input('-'))
    except ValueError:
        print('indice erroneo')
if __name__ == '__main__':
    test()