import pilas as pila
def decimal_a_binario(pila_prueba,numero):
    if numero>0:
        pila_prueba.insertar(numero%2)
        decimal_a_binario(pila_prueba,numero//2)
if __name__=='__main__':
    pila_prueba=pila.pila_secuencial(10)
    numero=int(100)
    decimal_a_binario(pila_prueba,numero)
    print(f'El numero {numero} en binario es:')
    pila_prueba.mostrar()