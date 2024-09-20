from pila_secuencial import pila as pila_sec
def decimal_a_binario(numero_ingresado):
    pila=pila_sec(10)
    pila.insertar(numero_ingresado)
    numero_binario=''
    while not pila.vacia():
        numero=pila.suprimir()
        if numero>0:
            numero_binario=str(numero%2)+numero_binario
            pila.insertar(numero//2)
        else:
            print(numero_binario)
if __name__=='__main__':
    for i in range(1,5):
        numero=i
        print(f'el numero decimal {numero} en binario es: ', end='')
        decimal_a_binario(numero)
        print('\n')
