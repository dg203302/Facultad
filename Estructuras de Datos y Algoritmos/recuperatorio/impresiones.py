from cola_secuencial import cola_secuencial
import random
def impresiones():
    cola_impresiones=cola_secuencial(5)
    impresiones_incompletas=0
    impresiones_realizadas=0
    Ts=0
    while Ts<60:
        if Ts%5==0:
            cola_impresiones.insertar(random.randint(1,15))
            impresiones_incompletas+=1
        if not cola_impresiones.vacia():
            impresion=cola_impresiones.suprimir()
            if impresion-5<=0:
                print('se imprimio una hoja')             #solo para controlar que se imprima una hoja, no es necesario
                impresiones_realizadas+=1
                impresiones_incompletas-=1
                Ts+=5
            else:
                cola_impresiones.insertar(impresion-5)
                Ts+=5
        Ts+=1
    print(f'cantidad de impresiones sin realizar: {impresiones_incompletas}\npromedio de espera: {Ts/impresiones_realizadas}')
if __name__=='__main__':
    impresiones()