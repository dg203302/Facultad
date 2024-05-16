from gestorprogramas import *
from gestorempleados import *
from gestormatricula import *
gstm=gstmatri()
gstp=gestprog()
gste=gestemp()
gste.registrar_empleados(gstp,gstm)
gstm.mostrarmat()
gstm.incisoa()
gstm.incisob()
gste.incisoc(gstm)