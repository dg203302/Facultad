from GESTORVENTA import gestorvent
def menu():
    empre=gestorvent()
    print('REGISTRO VENTAS')
    sele=input('ingrese la operacion que desee. \n "REGISTRAR" para almacenar un importe \n "TOTAL EMP" para mostrar el total facturado por una sucursal especifica \n "MAX DIA" para mostrar la sucursal que mas facturo en un dia especifico \n "MIN SEMANAL" para mostrar la sucursal que menos facturo en la semana \n "TOTAL SEMANAL" para mostrar el total por sucursal en la semana \n "SALIR" para terminar \n --')
    while sele != 'SALIR':
        if sele == 'REGISTRAR':
            num=int(input('ingrese el dia de la semana: '))
            dia=int(input('ingres el numero de la empresa: '))
            imp=float(input(f'ingrese el importe de la empresa {num} en el dia {dia}: '))
            empre.acum(dia-1,num-1,imp)
        elif sele == 'TOTAL EMP':
            suc=int(input('ingrese la sucursal que desee: '))
            empre.tota(suc-1)
        elif sele == 'MAX DIA':
            diasem=int(input('ingrese el dia de la semana que desee: '))
            empre.max(diasem-1)
        elif sele == 'MIN SEMANAL':
            empre.min()
        elif sele == 'TOTAL SEMANA':
            empre.totsem()
        else:
            print('ingreso incorrecto')
        sele=input('ingrese la operacion que desee. \n "REGISTRAR" para almacenar un importe \n "TOTAL EMP" para mostrar el total facturado por una sucursal especifica \n "MAX DIA" para mostrar la sucursal que mas facturo en un dia especifico \n "MIN SEMANAL" para mostrar la sucursal que menos facturo en la semana \n "TOTAL SEMANAL" para mostrar el total por sucursal en la semana \n "SALIR" para terminar \n --')
"""""
def test():
    empre.mostrar()
    empre.acum(1, 3, 21)
    empre.acum(0, 4, 221)
    empre.acum(2, 1, 231)
    empre.acum(4, 4, 241)
    empre.mostrar()
    empre.tota(4)
    empre.max(3)
    empre.min()
    empre.totsem()
"""
if __name__ == '__main__':
    menu()
    #test()