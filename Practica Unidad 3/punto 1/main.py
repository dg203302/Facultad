from gestedif import gestedi
def test():
    ge=gestedi()
    op=int(input('1 para inciso c1, 2 para inciso c2, 3 para inciso c3, 4 para inciso c4:\n-'))
    while True:
        if op==0:
            break
        elif op==1:
            try:
                ge.c1()
            except:
                print('ingreso mal de nombre!')
        elif op==2:
            try:
                ge.c2()
            except:
                print('ingreso mal de nombre!')
        elif op==3:
            try:
                ge.c3()
            except:
                print('ingreso mal de propietario!')
        elif op==4:
            try:
                ge.c4()
            except:
                print('ingreso mal de numero de piso!')
        else:
            print('opcion incorrecta!')
        op=int(input('-'))
if __name__ == '__main__':
    test()