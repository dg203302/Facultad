from pilas import *
def calcular_factorial(pila,numero_a_calcular):
    if numero_a_calcular>0:
        numero_factorial=numero_a_calcular*(calcular_factorial(pila,numero_a_calcular-1))
        return numero_factorial
    elif numero_a_calcular==0:
        return 1
pila=pila_enlazada()
numero=int(input('ingrese el numero que desee saber el factorial: '))
print(calcular_factorial(pila,numero))