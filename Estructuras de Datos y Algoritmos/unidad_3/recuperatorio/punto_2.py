from cola_enlazada import cola
cola_reg=cola()
cca=0
csa=0
ts=0
cajero=False
while ts<120:
    if ts%5==0:
        if cajero==True:
            cola_reg.insertar(ts)
        else:
            cajero=True
        csa+=1
    if ts%2==0:
        if cajero==True:
            cajero=False
            csa-=1
            cca+=1
        else:
            cola_reg.suprimir()
            cajero=True
    ts+=1
print(cca,abs(ts/csa))