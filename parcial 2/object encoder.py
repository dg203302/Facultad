#decodificador
'''
def decodedificarDiccionario(slef,d):
    if "clase" not in d:
        return d
    else:
        clas_name=d['clase']
        class_=eval(clas_name)
        if clas_name=='clasegestor':
            objetos=d['objetos']
            gestor=clasegestor()
            for i in range(len(objetos)):
                dobjetos=objetos[i]
                class_name=dobjetos.pop('clase')
                class_=eval(class_name)
                atrib=dobjetos['atributos']
                obje=class_(**atrib)
                gestor.agreg(obje)
        return gestor
'''
#main
'''
dic=encoder.leerjson()
gest=encoder.decodific(dic)
'''