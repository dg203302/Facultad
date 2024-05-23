from gestormiembro import *
from gestorvisualizacion import *
def test():
    gstmi=gestormiembro()
    gstvi=gestorvisua()
    op=int(input('ingrese 0 para salir, 1 para inciso a, 2 para inciso b \n -'))
    while(True):
        if op==0:
            break
        elif op==1:
            gstmi.a(gstvi)
        elif op==2:
            gstmi.b(gstvi)
        op=int(input('-'))
if __name__ == '__main__':
    test()