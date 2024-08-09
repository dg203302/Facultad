from gestorproductos import *
def menu():
    gst=gestorproductos()
    print('ingrese la opcion que desee\n 1 para agregar productos, 2 para ver un tipo de producto, 3 para mostrar la cantidad de productos de cada tipo, 4 para listar todos los productos, 0 para salir')
    while True:
        try:
            op=int(input('--'))
            if op==0:
                break
            elif op==1:
                gst.agreg()
            elif op==2:
                gst.b()
            elif op==3:
                gst.c()
            elif op==4:
                gst.d()
        except ValueError:
            print('ingrese un numero!!!!')
if __name__ == '__main__':
    menu()