import json
class encoderjson:
    def load(self):
        with open('Python/parcial año pasado hecho con json/servicios.json',mode='r') as carg:
            d=json.load(carg)
            carg.close()
            return d
    def save(self,d):
        with open('Python/parcial año pasado hecho con json/nuevservicios.json',mode='a') as guard:
            json.dump(d,guard,indent=4)
            guard.close()