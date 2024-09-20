from GESTOREQU import gest_equi
from GESTORFEC import gest_fech
def test():
    gestfech=gest_fech()
    gesteq=gest_equi()
    op=('SELECCIONE \n 1 para leer los equipos, 2 para leer las fechas, 3 para listar un equipo, 4 actualizar datos segun una fecha, 5 ordenar y almacenar \n -')
    while True:
        if op == 0:
            del gesteq
            del gestfech
            break
        elif op == 1:
            gesteq.cargaequi()
        elif op == 2:
            gestfech.cargafecha()
        elif op == 3:
            gestfech.listado(gesteq)
        elif op == 4:
            gestfech.act(gesteq)
        elif op == 5:
            gesteq.ordenyalmacen()
if __name__ == '__main__':
    test()