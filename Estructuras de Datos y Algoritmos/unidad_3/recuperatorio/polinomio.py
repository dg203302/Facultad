from lista_secuencial import lista_secuencial
def suma(polinomio1,polinomio2):
    if polinomio1.get_dimension()!=polinomio2.get_dimension():
        print('Los polinomios no tienen el mismo grado')
    else:
        polinomio_suma=lista_secuencial(polinomio1.get_dimension())
        for i in range(polinomio1.get_dimension()):
            polinomio_suma.insertar_por_posicion(polinomio1.buscar_por_posicion(i)+polinomio2.buscar_por_posicion(i),i)
        polinomio_suma.recorrer()
def resta(polinomio1,polinomio2):
    if polinomio1.get_dimension()!=polinomio2.get_dimension():
        print('Los polinomios no tienen el mismo grado')
    else:
        polinomio_resta=lista_secuencial(polinomio1.get_dimension())
        for i in range(polinomio1.get_dimension()):
            polinomio_resta.insertar_por_posicion(polinomio1.buscar_por_posicion(i)-polinomio2.buscar_por_posicion(i),i)
        polinomio_resta.recorrer()
def multiplicacion_de_escalar(polinomio,escalar):
    polinomio_multiplicado=lista_secuencial(polinomio.get_dimension())
    for i in range(polinomio.get_dimension()):
        polinomio_multiplicado.insertar_por_posicion(polinomio.buscar_por_posicion(i)*escalar,i)
    polinomio_multiplicado.recorrer()
if __name__=='__main__':
    polinomio1=lista_secuencial(3)
    polinomio2=lista_secuencial(3)
    polinomio1.insertar_por_posicion(2,0)
    polinomio1.insertar_por_posicion(3,1)
    polinomio1.insertar_por_posicion(4,2)
    polinomio2.insertar_por_posicion(1,0)
    polinomio2.insertar_por_posicion(2,1)
    polinomio2.insertar_por_posicion(3,2)
    print()
    polinomio1.recorrer()
    print()
    polinomio2.recorrer()
    print('\nsuma de polinomios')
    suma(polinomio1,polinomio2)
    print('\nresta de polinomios')
    resta(polinomio1,polinomio2)
    print('\nmultiplicacion de un escalar y un polinomio')
    escalar=2
    multiplicacion_de_escalar(polinomio1,escalar)
    print()