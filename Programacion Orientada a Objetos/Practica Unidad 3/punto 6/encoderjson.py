import json
class encoderjson:
    def leerjson(self):
        with open('Python/practica 3/punto 6/calefactores.json',mode='r') as arc:
            da=json.load(arc)
            arc.close()
            return da
    def guardarjson(self,dge):
        with open('Python/practica 3/punto 6/calefactoresguard.json',mode='a') as guard:
            json.dump(dge,guard,indent=4)
            guard.close()