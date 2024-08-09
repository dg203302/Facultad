from gestmat import gestormat
def test():
     matrices=gestormat()
     print('OPERACIONES DEL ALGEBRA LINEAL USANDO NUMPY')
     while True:
          op=int(input('ingrese la opcion: \n 1 para crear una o mas matrices, 2 para listar las operaciones entre matrices disponibles, 3 para listar las operaciones unitarias disponibles \n 0 para salir \n -'))
          if op == 0:
               break
          elif op == 1:
                    matrices.agreg()
          elif op == 2:
               if matrices.getlen() < 2:
                    print('debe crear una segunda matriz!')
               else:
                    matrices.op_en_m()
          elif op == 3:
               matrices.op_en_d_m()
if __name__ == '__main__':
    test()