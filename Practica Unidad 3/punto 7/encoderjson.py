import json
class encoderjson:
    def leerjson(self):
        with open('Practica Unidad 3/punto 7/personal.json',mode='r') as lect:
            dic=json.load(lect)
            lect.close()
            return dic
    def guardjson(self,dic):
        with open('Practica Unidad 3/punto 7/personal.json',mode='a') as guard:
            json.dump(dic,guard,indent=4)
            guard.close()