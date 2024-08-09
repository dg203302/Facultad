import json
class encoder:
    def tojson(self,jugadores):
        with open('PRACTICOS/Practico Tkinter/iteracion 2/con canvas forma botones/pysimonpuntajesusandocanvas.json', mode='a') as guard:
            json.dump(jugadores,guard,indent=4)
            guard.close()