from gestor import *
def menu():
    gest=gestorservicios()
    gest.cargaautocsv()
    op=int(input('1 para cargar nuevos servicios, 2 para inciso b, 3 para inciso c, 4 para inciso d, 0 para salir\n --'))
    while True:
        if op==1:
            gest.cargamanual()
        elif op==2:
            gest.b()
        elif op==3:
            gest.c()
        elif op==4:
            gest.d()
        elif op==0:
            break
        op=int(input(' --'))
if __name__=='__main__':
    menu()