from gestorvehiculos import *
from encoder import *
encd=encoderjson()
gstr=gestorvehiculos()
objpru=carga('312312','42342','4234',34243,43,434)
gstr.agreg(objpru)
objpru2=pasajeros('312321312','42213342','423234',3424333,423,4)
gstr.agreg(objpru2)
encd.carga(gstr)
gstr.elimin()
#gstr.b()
#gstr.d()
#gstr.c()
gstr.tojson(encd)