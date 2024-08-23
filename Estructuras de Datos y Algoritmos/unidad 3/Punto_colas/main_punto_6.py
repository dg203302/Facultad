from punto_6 import *
if __name__=='__main__':
    op=int(input('0 para salir, 1 para ingresar impresiones, 2 para atender las impresiones, 3 para mostrar trabajos\n-'))
    while True:
        impresora=impresiones()
        if op==0:
            break
        elif op==1:
            impresora.ingresar_trabajos()
        elif op==2:
            impresora.atender()
        elif op==3:
            impresora.mostrar_trabajos()
        elif op==4:
            impresora.prueba_menu()
        op=int(input('-'))