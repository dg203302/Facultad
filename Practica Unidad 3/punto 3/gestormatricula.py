class gstmatri:
    __matriculas:list
    def __init__(self):
        self.__matriculas=[]
    def agregmat(self,mat):
        self.__matriculas.append(mat)
    def incisoa(self):
        ac=0
        id=input('ingrese el id del empleado: ')
        for mat in self.__matriculas:
            if mat.getid()==id:
                ac+=mat.gethoras()
        print(f'el empleado con id: {id} tiene un total de: {ac} horas')
    def incisob(self):
        nomp=input('ingrese el nombre del programa de capacitacion: ')
        for mat in self.__matriculas:
            if mat.getnomp()==nomp:
                print(f'empleado matriculado: {mat.getnomemp()}')
    def c(self,empleado):
        b=False
        for matri in self.__matriculas:
            if empleado == matri.getemp():
                b=True
        if b==False:
            print(empleado.getnom())
    def mostrarmat(self):
        for mat in self.__matriculas:
            print(mat)