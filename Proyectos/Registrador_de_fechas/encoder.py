import os
import json
from datos import *
class enconder_json:
    @classmethod
    def cargar_fechas(cls,gestor):
        ruta_base=os.path.dirname(os.path.abspath(__file__))
        nombre_json='fechas.json'
        try:
            with open(os.path.join(ruta_base, nombre_json),mode='r') as archivo_json:
                diccionario_datos=json.load(archivo_json)
                archivo_json.close()
                cls.cargar_gestor(gestor,diccionario_datos)
        except json.JSONDecodeError:
            return
    @classmethod
    def cargar_gestor(cls,gestor,diccionario_datos):
        for registro in diccionario_datos['gestor_fechas']:
            fecha=datos_de_registro(**registro)
            gestor.insertar(fecha)
    @classmethod
    def guardar_json(cls,diccionario_guardar=None):
        if diccionario_guardar==None:
            ruta_base=os.path.dirname(os.path.abspath(__file__))
            nombre_json='fechas.json'
            with open(os.path.join(ruta_base, nombre_json),mode='w') as archivo_json:
                archivo_json.close()
        else:
            ruta_base=os.path.dirname(os.path.abspath(__file__))
            nombre_json='fechas.json'
            with open(os.path.join(ruta_base, nombre_json),mode='w') as archivo_json:
                json.dump(diccionario_guardar,archivo_json,indent=4)
                archivo_json.close()