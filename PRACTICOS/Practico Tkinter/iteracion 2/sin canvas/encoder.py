import json
class encoder:
    def tojson(self,jugadores):
        with open('PRACTICOS/Practico Tkinter/iteracion 2/sin canvas/pysimonpuntajes.json', mode='a') as guard:
            json.dump(jugadores,guard,indent=4)
            guard.close()