from vectores import matriz
class gestormat:
    __gest: list
    def __init__(self):
        self.__gest=[]
    def agreg(self):
        n=int(input('ingrese las filas de la matriz: '))
        m=int(input('ingrese las columnas de la matriz: '))
        matri=matriz(n,m)
        for i in range(n):
            for j in range(m):
                v=float(input(f'ingrese el valor de la matriz en la posicion {i+1}, {j+1}: '))
                matri.cargar(i,j,v)
        print(f'valores de la matriz: \n {matri}')
        self.__gest.append(matri)
    def op_en_m(self):
        i=int(input(f'seleccione 1era matriz de las {len(self.__gest)}: '))
        j=int(input(f'seleccione 2da matriz de las {len(self.__gest)}: '))
        if i <= len(self.__gest) and j <= len(self.__gest):
            sop=int(input('OPERACIONES DISPONIBLES: \n 1 suma, 2 multiplicacion, 3 resta \n -'))
            if sop == 1:
                print(f'suma de las matrices: \n {self.__gest[i-1]+self.__gest[j-1]}')
            elif sop == 2:
                print(f'multiplicacion de las matrices: \n {self.__gest[i-1]*self.__gest[j-1]}')
            elif sop == 3:
                print(f'resta de las matrices: \n {self.__gest[i-1]*self.__gest[j-1]}')
            else:
                print('opcion incorrecta!')
        else: 
             print('matrices/matriz incorrecta')
    def op_en_d_m(self):
        i=int(input(f'eliga la matriz una de las {len(self.__gest)}: '))
        if i <= len(self.__gest):
            opu=int(input(f'las operaciones para la matriz {i} son: \n 1 inversa, 2 traspuesta, 3 calculo de determinante, 4 calculo de norma, 5 calculo de traza, 6 valor minimo de la matriz, 7 valor maximo de la matriz, 8 valor medio de la matriz, 9 seno de cada valor de la matriz, 10 coseno de cada valor de la matriz \n -'))
            if opu == 1:
                print(f'{self.__gest[i-1].inver()}')
            elif opu == 2:
                print(f'{self.__gest[i-1].traspuesta()}')
            elif opu == 3:
                print(f'{self.__gest[i-1].deter()}')
            elif opu == 4:
                print(f'{self.__gest[i-1].norma()}')
            elif opu == 5:
                print(f'{self.__gest[i-1].traza()}')
            elif opu == 6:
                print(f'{self.__gest[i-1].min()}')
            elif opu == 7:
                print(f'{self.__gest[i-1].max()}')
            elif opu == 8:
                print(f'{self.__gest[i-1].media()}')
            elif opu == 9:
                print(f'{self.__gest[i-1].seno()}')
            elif opu == 10:
                print(f'{self.__gest[i-1].coseno()}')
            else:
                print("opcion incorrecta!")
        else:
            print('matriz incorrecta')
    def getlen(self):
        return len(self.__gest)