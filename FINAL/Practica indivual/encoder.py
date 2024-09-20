import json
from locales import *
from nacionales import *
class encoder:
    @classmethod
    def cargar_gestor(cls,gestor_clientes):
        clientes=cls.leer_json()
        try:
            for cliente in clientes['gestorclientes']:
                if cliente['tipo']=='local':
                    nuevo_cliente=locales(**cliente['datos'])
                    gestor_clientes.insercion(nuevo_cliente)
                elif cliente['tipo']=='nacional':
                    nuevo_cliente=nacionales(**cliente['datos'])
                    gestor_clientes.insercion(nuevo_cliente)
        except KeyError:
            print('error de json!')
            return
    @classmethod
    def leer_json(cls):
        try:
            with open('FINAL/Practica indivual/clientes.json', mode='r') as archivo:
                diccionario=json.load(archivo)
                archivo.close()
                return diccionario
        except json.decoder.JSONDecodeError:
            print('json vacio!')
            return
        except FileNotFoundError:
            print('json no existente')
    @classmethod
    def guardar_json(cls,diccionario):
        with open('FINAL/Practica indivual/clientes.json', mode='w') as archivo:
            json.dump(diccionario,archivo,indent=4)
            archivo.close()