from pila_secuencial import pila
def factorial(numero):
    pila1=pila(1)
    factorial=1
    pila1.insertar(numero)
    while not pila1.vacia():
        numero_fac=pila1.suprimir()
        if numero_fac>0:
            factorial=factorial*numero_fac
            pila1.insertar(numero_fac-1)
        else:
            return factorial
if __name__=='__main__':
    numero=int(input('Ingrese un numero para calcular su factorial: '))
    print(f'El factorial de {numero} es: {factorial(numero)}')
