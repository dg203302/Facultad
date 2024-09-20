from listaenl import *
from encoderjson import *
if __name__=='__main__':
    encjson=encoderjson()
    lista=lkdlist(encjson)
    op=int(input('1 para inciso a y b, 2 para inciso c, 3 para inciso d, 4 para inciso e, 5 para inciso f, 6 para guardar json, 0 para salir\n -'))
    while True:
        if op==0:
            break
        elif op==1:
            lista.ayb()
        elif op==2:
            lista.most()
        elif op==3:
            lista.d()
        elif op==4:
            lista.e()
        elif op==5:
            lista.f()
        elif op==6:
            lista.tojson(encjson)
        op=int(input(' -'))