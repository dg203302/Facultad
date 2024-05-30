import json
from carga import *
from pasajeros import *
from gestorvehiculos import *
#hacer asi la carga por json!!!!!!!!!!!!!!!!!!!!!!!!!!
class encoderjson:
    def loadjson(self):
        with open('parcial 2 año pasado/vehiculos.json',mode='r') as lect:
            d=json.load(lect)
            lect.close()
            return d
    def savejson(self,d):
        with open('nuevehiculos.json',mode='r') as guard:
            json.dump(d,guard,indent=4)
    def carga(self,gestorvehi):
        d=self.loadjson()
        try:
            if d['clase']=='gestorvehiculos':
                for obje in d['vehiculos']:
                    if obje['tipo']=='carga':
                        cargavehi=carga(**obje['atributos'])
                        gestorvehi.agreg(cargavehi)
                    elif obje['tipo']=='pasajeros':
                        pasajervehi=pasajeros(**obje['atributos'])
                        gestorvehi.agreg(pasajervehi)
        except KeyError:
            print('gestor incorrecto!')
'''
    def encoder(self,d):
        if 'clase' not in d:
            return d
        else:
            class_name=d['vehiculos']
            class_=eval(class_name)
            if class_name == 'gestorvehiculos':
                vehics=d['vehiculos']
                gestor=gestorvehiculos()
                for i in range(len(vehics)):
                    nvehics=vehics[i]
                    class_name=nvehics.pop('clase')
                    class_=eval(class_name)
                    atrib=nvehics['atributos']
                    vehiculo=class_(**atrib)
                    gestor.agreg(vehiculo)
            return gestor
'''