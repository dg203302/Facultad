from gestorclientes import *
if __name__=='__main__':
    gestor=lista_gestor()
    opcion=input('1 para cargar, 2 para inciso 2, 3 para inciso 3, 4 para guardar un json, 0 para salir\n-')
    while True:
        if opcion=='0':
            break
        elif opcion=='1':
            gestor.cargar()
        elif opcion=='2':
            gestor.inciso2()
        elif opcion=='3':
            gestor.inciso3()
        elif opcion=='4':
            gestor.gestor_a_json()
        opcion=input('1 para cargar, 2 para inciso 2, 3 para inciso 3, 4 para guardar un json, 0 para salir\n-')