class caja_ahorro:
    __nro_cuenta:str
    __cuil:str
    __apell:str
    __nom:str
    __sald:float
    def __init__(self, nro,cuil,ape,no,sld):
        self.__nro_cuenta=nro
        self.__cuil=cuil
        self.__apell=ape
        self.__nom=no
        self.__sald=sld
    def mostrardat(self):
        print("DATOS DE LA CAJA DE AHORRO \n NOMBRE DE CUENTA: {} \n CUIL: {} \n NOMBRE DEL DUEÑO: {} \n APELLIDO DEL DUEÑO {} \n SALDO DE LA CUENTA: {} \n".format(self.__nro_cuenta, self.__cuil, self.__nom, self.__apell, self.__sald))
    def extimpt(self,imp_ext):
        if self.__sald >= imp_ext:
            self.__sald=self.__sald-imp_ext
            print('el nuevo saldo de la cuenta es: {}'.format(self.__sald))
            return(imp_ext)
        else:
            return(-1)
    def dep(self,imp_dep):
        if imp_dep>0:
            self.__sald=self.__sald+imp_dep
            print('deposito realizado correctamente')
        else:
            print('operacion incorrecta: importe erroneo')
    def valcuil(self):
        valid=False
        cui=[]
        for char in self.__cuil:
            if char != '-':
                cui.append(int(char))
        mul=(cui[0]*5)+(cui[1]*4)+(cui[2]*3)+(cui[3]*2)+(cui[4]*7)+(cui[5]*6)+(cui[6]*5)+(cui[7]*4)+(cui[8]*3)+(cui[9]*2)
        resto=mul % 11
        if resto == 0:
            print('cuil valido con codigo de verificacion 0')
            valid=True
        elif resto == 1:
            if cui[1] == 0:
                if cui[10] == 9:
                    print('cuil valido , hombre y digito igual a 9')
                    valid=True
            elif cui[1] == 7:
                if cui[10] == 4:
                    print('cuil valido , mujer y digito igual a 4')
                    valid=True
            else:
                print(f'{resto}, {mul}, {cui}, {valid}') #para ver que estaba mal
                print('cuil invalido')
        else:
            digi=(11-resto)
            if cui[10] == digi:
                print(f'codigo de verificacion igual a {digi}')
                valid=True
            else:
                print(f'{resto}, {mul}, {cui}, {valid}') #para ver que estaba mal
                print('cuil invalido')
    def getcuil(self):
        return self.__cuil
    def getnom(self):
        return self.__nom
    def getap(self):
        return self.__apell
    def getsal(self):
        return self.__sald