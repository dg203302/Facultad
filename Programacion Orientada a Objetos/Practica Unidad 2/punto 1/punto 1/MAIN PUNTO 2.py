from CAJAAHORRO import caja_ahorro
from GESTOR import contenedor
def test():
    conte=contenedor()
    for i in range(2):
        nume=input('ingrese el numero de cuenta: ')
        cuil=input('ingrese el cuil: ')
        Ape=input('ingrese el apellido: ')
        Nom=input('ingrese el nombre: ')
        Sald=float(input('ingrese el saldo: '))
        cuenta=caja_ahorro(nume,cuil,Ape,Nom,Sald)
        conte.agreg(cuenta)
    cuila=input('ingrese el cuil que quiere saber: ')
    conte.obtener_datos(cuila)
if __name__ == '__main__':
    test()