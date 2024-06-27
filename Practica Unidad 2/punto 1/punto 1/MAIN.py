from CAJAAHORRO import caja_ahorro
if __name__ == '__main__':
    nume=input('ingrese el numero de cuenta: ')
    Cuil=input('ingrese el cuil: ')
    Ape=input('ingrese el apellido: ')
    Nom=input('ingrese el nombre: ')
    Sald=float(input('ingrese el saldo: '))
    cuent1=caja_ahorro(nume,Cuil,Ape,Nom,Sald)
    cuent1.valcuil()
    cuent1.mostrardat()
    impor=float(input('ingrese el importe que desee extraer: '))
    cuent1.extimpt(impor)
    impdep=float(input('ingrese el importe que desee depositar: '))
    cuent1.dep(impdep)