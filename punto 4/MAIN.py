from gestorp import gestorped
from gestorm import gestormoto
def test():
    gm=gestormoto()
    gm.agreg()
    gp=gestorped()
    gp.agreg()
    op=input('ingrese la opcion que desee: ')
    while op != 'salir':
        if op == 'nuevo pedido':
            gp.nuev(gm)
        elif op == 'modificar pedido':
            pat=input('ingrese la patente que desee modificar: ')
            id=input('ingrese el id que desee modificar: ')
            tr=input('ingrese el tiempo real de dicho pedido: ')
            gp.modif(pat,id,tr)
        elif op == 'mostrar datos y tiempo promedio':
            pate=input('ingrese la patente que desee: ')
            gp.datprod(gm,pate)
        op=input('ingrese la opcion que desee: ')
if __name__ == '__main__':
    test()