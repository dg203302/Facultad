from pilas import *
def pasar_a_numero_binario(pila,numero_a_dividir):
    if numero_a_dividir>=2:
        resto=numero_a_dividir%2
        pila.insertar(resto)
        n2=numero_a_dividir//2
        pasar_a_numero_binario(pila,n2)
    elif numero_a_dividir==0 or numero_a_dividir== 1:
        return pila.insertar(numero_a_dividir)
pila=pila_enlazada()
numero_decimal=int(input('ingrese el numero: '))
pasar_a_numero_binario(pila,numero_decimal)
pila.mostrar()