import json
from trabajador import *
class encoderjson:
    @classmethod
    def carga_por_json(cls, gestor_personal):
        diccionario_json=cls.cargar_json()
        if diccionario_json==None:
            return
        else:
            for cliente in diccionario_json["gestor_personal"]:
                if cliente["tipo"]=='persona':
                    nueva_persona=persona(**cliente["atributos"])
                    gestor_personal.insercion_al_final(nueva_persona)
                elif cliente["tipo"]=='trabajador':
                    nuevo_trabajador=trabajdor(**cliente['atributos'])
                    gestor_personal.insercion_al_final(nuevo_trabajador)
    @classmethod
    def cargar_json(cls):
        try:
            with open('FINAL/practica 4/personal.json', mode='r') as archivo_json:
                diccionario=json.load(archivo_json)
                archivo_json.close()
                return diccionario
        except json.JSONDecodeError:
            print('json vacio!')
            return None
        except FileNotFoundError:
            print('archivo no existente!')
            return None
    @classmethod
    def to_json(cls,diccionario_clase):
        with open('FINAL/practica 4/personal.json', mode='w') as archivo_json:
            json.dump(diccionario_clase,archivo_json,indent=4)
            archivo_json.close()