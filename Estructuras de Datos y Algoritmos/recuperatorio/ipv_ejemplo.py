from cola_secuencial import cola_secuencial
def ipv():
    cola = cola_secuencial(5)
    Ts = 0
    while Ts < 120:
        if Ts % 10 == 0:
            cola.insertar(Ts)
        elif Ts % 15 == 0:
            cola.suprimir()
        Ts += 1
    print('el tiempo mayor del no atendido', cola.suprimir())
ipv()