from manejadorbecas import manejadorbeca
from manejadorbeneficiarios import manejadorbene
def test():
    gestbec=manejadorbeca()
    gestbene=manejadorbene()
    op=int(input('1 para a,2 para b, 3 para c, 4 para d'))
    while op != 0:
        if op == 1:
            gestbec.a(gestbene)
        elif op == 2:
            gestbene.b(gestbec)
        elif op == 3:
            gestbene.c()
        elif op == 4:
            gestbec.d(gestbene)
        else:
            print('opcion invalida!')
if __name__ == '__main__':
    test()