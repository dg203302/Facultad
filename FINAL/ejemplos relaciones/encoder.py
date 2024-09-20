import json
from objeto_dato import *
class encoder_json:
    @classmethod
    def abrir_json(cls,gestor_ejemplo):
        with open('FINAL/ejemplos relaciones/muestras.json', mode='r') as archivo_json:
            diccionario=json.load(archivo_json)
            archivo_json.close()
            cls.cargar_gestor(diccionario,gestor_ejemplo)
    @classmethod
    def cargar_gestor(cls,diccionario,gestor_ejemplo):
        for objeto in diccionario['gestor_objetos']:
            objeto_dato=wachin(**objeto)
            gestor_ejemplo.insercion_al_final(objeto_dato)
    @classmethod
    def guardar_json(cls,diccionario_guardar):
        with open('FINAL/ejemplos relaciones/muestras.json',mode='w') as archivo_json:
            json.dump(diccionario_guardar,archivo_json,indent=4)
            archivo_json.close()