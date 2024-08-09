from gestor import *
from encoder import *
def menu():
    encd=encoderjson()
    gest=gestorservicios()
    gest.cargaautojson(encd)
    op=int(input('1 para cargar nuevos servicios,2 para insertar un servicio en una posicion de la lista, 3 para eliminar un nodo, 4 para inciso b, 5 para inciso c, 6 para inciso d, 7 para guardar el json, 0 para salir\n --'))
    while True:
        if op==1:
            gest.cargamanual()
        elif op==2:
            gest.insertarmanual()
        elif op==3:
            gest.eliminar()
        elif op==4:
            gest.b()
        elif op==5:
            gest.c()
        elif op==6:
            gest.d()
        elif op==7:
            gest.tojson(encd)
        elif op==0:
            break
        op=int(input(' --'))
if __name__=='__main__':
    menu()