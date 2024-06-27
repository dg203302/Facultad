class gestorvent:
    __dias: list
    def __init__(self):
        self.__dias= [[0 for dia in range(7)]for numero in range(5)]
#a) Leer por teclado, día de la semana, número de sucursal e importe de una factura, acumularlo para ese día y esa sucursal.
    def acum(self, num, dia, imp):
        self.__dias[num][dia]+=imp
        print("¡IMPORTE REGISTRADO!")
#b) Leer por teclado una sucursal, calcular el total de facturación para esa sucursal.
    def tota(self, nume):
        ac=0
        for j in range(7):
            ac=ac+self.__dias[nume][j]
        print(f'total acumulado en la semana para la sucursal {nume+1}: {ac}')
#c) Leer por teclado un día de la semana, obtener la sucursal que más facturó para ese día.
    def max(self,dia):
        max_emp=None
        max_val=-1
        for i in range(5):
            if self.__dias[i][dia] > max_val:
                max_val=self.__dias[i][dia]
                max_emp=i
        print(f'la mayor empresa que facturo el dia {dia+1} fue {max_emp+1}')
#d) Calcular la sucursal con menos facturación durante toda la semana.
    def min(self):
        min=1000
        min_suc=None
        for i in range(5):
            for j in range(7):
                if self.__dias[i][j] < min:
                    min=self.__dias[i][j]
                    min_suc=i
        print(f'minimo de la semana {min_suc}')
#e) Calcular el total facturado por todas las sucursales durante toda la semana.
    def totsem(self):
        for i in range(5):
            ac=0
            for j in range(7):
                ac+=self.__dias[i][j]
            print(f'cantidad recaudada por la empresa {i+1}: {ac}')
    def mostrar(self):
        print(self.__dias)