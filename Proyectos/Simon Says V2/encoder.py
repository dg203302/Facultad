import json, os
from jugador import *
class encoder:
    def cargarjson(self):
        ruta_base=os.path.dirname(os.path.abspath(__file__))
        nombre_json='pysimonpuntajes.json'
        with open(os.path.join(ruta_base, nombre_json),mode='r') as lect:
            try:
                diccio=json.load(lect)
            except json.decoder.JSONDecodeError:
                return
            else:
                lect.close()
                return diccio
    def cargarjugadores(self,gestor):
        dicc=self.cargarjson()
        if dicc==None:
            return
        else:
            for jugad in dicc['jugadores']:
                player=jugador(**jugad['jugador'])
                gestor.cargarjugadores(player)
    def agregarajson(self,jugadores):
        ruta_base=os.path.dirname(os.path.abspath(__file__))
        nombre_json='pysimonpuntajes.json'
        with open(os.path.join(ruta_base, nombre_json),mode='w') as guard:
            json.dump(jugadores,guard,indent=4)
            guard.close()
    def limpiar_jugadas(self):
        ruta_base=os.path.dirname(os.path.abspath(__file__))
        nombre_json='pysimonpuntajes.json'
        with open(os.path.join(ruta_base, nombre_json),mode='w') as limpiar:
            limpiar.close()