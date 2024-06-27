from CAJAAHORRO import caja_ahorro
from GESTOR import contenedor
def test():
    conte=contenedor()
    cuenta1=caja_ahorro('234232','20-44991307-9','garcia','diego',234434.545)
    conte.agreg(cuenta1)
    cuenta2=caja_ahorro('675675','20-54651207-7','doe','john',234345.3432)
    conte.agreg(cuenta2)
    cuila=input('ingrese el cuil que quiere saber: ')
    conte.obtener_datos(cuila)
if __name__ == '__main__':
    test()