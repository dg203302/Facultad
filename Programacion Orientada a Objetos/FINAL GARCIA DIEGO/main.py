from lista import *
if __name__=='__main__':
    gestor_pacientes=lista()
    opcion=input('1 para inciso b, 2 para inciso c, 3 para inciso d, 4 para inciso e, 0 para salir\n-')
    while True:
        if opcion=='0':
                break
        elif opcion=='1':
            gestor_pacientes.inciso_b()
        elif opcion=='2':
            gestor_pacientes.inciso_c()
        elif opcion=='3':
            try:
                indice=int(input('que paciente desea saber: '))-1
                gestor_pacientes.inciso_d(indice)
            except IndexError:
                print('indice fuera de rango!')
            except ValueError:
                print('valor invalido')
            except TypeError:
                print('valor invalido')
        elif opcion=='4':
            valor_consulta=float(input('ingrese el nuevo valor de consulta: '))
            gestor_pacientes.inciso_e(valor_consulta)
        else:
            print('invalido')
        opcion=input('-')