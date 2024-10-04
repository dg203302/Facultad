from cola_secuencial import cola_secuencial
import random
Ts=0    #tiempo de simulacion
Tec=0   #tiempo de espera de clientes
cca=0   #cantidad de clientes atendidos
csa=0   #cantidad de clientes sin atender
teca=0  #tiempo de espera de clientes atendidos
tesa=0  #tiempo de espera de clientes sin atender
c1=0    #clientes en cajero 1
c2=0    #clientes en cajero 2
c3=0    #clientes en cajero 3
cajero=cola_secuencial(10)
while Ts<120:
    if Ts%2==0:
        if c1==0 or c2==0 or c3==0:
            eleccion=random.randint(1,3)
            if eleccion==1:
                c1+=1
            elif eleccion==2:
                c2+=1
            elif eleccion==3:
                c3+=1
            cajero.insertar(Ts)
        else:
            if c1<c2 and c1<c3:
                c1+=1
            elif c2<c1 and c2<c3:
                c2+=1
            elif c3<c1 and c3<c2:
                c3+=1
            cajero.insertar(Ts)
        csa+=1
    elif Ts%5==0 or Ts%3==0 or Ts%4==0: 
        if Ts%5==0:
            if c1>0:
                c1-=1
        elif Ts%3==0:
            if c2>0:
                c2-=1
        elif Ts%4==0:
            if c3>0:
                c3-=1
        csa-=1
        cca+=1
        teca+=cajero.suprimir()
    Ts+=1

# Avoid division by zero
promedio_espera_atendidos = teca/cca if cca != 0 else 0
promedio_no_atendidos = Ts/csa if csa != 0 else 0

print(f'cantidad de clientes sin atender: {csa}\ncantidad de clientes atendidos: {cca}\ntiempo total de los clientes en la cola: {teca}\npromedio de espera de los clientes atendidos: {promedio_espera_atendidos}\npromedio de clientes no atendidos: {promedio_no_atendidos}')