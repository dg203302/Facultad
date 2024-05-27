from listaenl import *
from encoderjson import *
if __name__=='__main__':
    encjson=encoderjson()
    lista=lkdlist(encjson)
    lista.mostrar()
    lista.tojson(encjson)