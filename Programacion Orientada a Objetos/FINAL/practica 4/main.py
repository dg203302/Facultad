from lista import *
if __name__=='__main__':
    lista=gestor_personal()
    lista.mostrar()
    lista.insertar_posicion_ejemplo()
    lista.mostrar()
    lista.to_json()