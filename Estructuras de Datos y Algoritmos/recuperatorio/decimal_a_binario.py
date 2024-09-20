from pilas import pila_secuencial
def decimal_a_binario(numero_ingresado):
    pila=pila_secuencial(10)
    pila.insertar(numero_ingresado)
    numero_binario=''
    while not pila.vacia():
        numero=pila.suprimir()
        if numero>0:
            numero_binario=str(numero%2)+numero_binario
            pila.insertar(numero//2)
    return numero_binario
if __name__=='__main__':
    numero=2
    print(f'el numero decimal {numero} en binario es {decimal_a_binario(numero)}')