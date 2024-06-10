import json
from jugador import *
class encoder:
    def cargarjson(self):
        with open('SIMON DICE COMPLETO/pysimonpuntajes.json',mode='r') as lect:
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
        with open('SIMON DICE COMPLETO/pysimonpuntajes.json', mode='w') as guard:
            json.dump(jugadores,guard,indent=4)
            guard.close()
    