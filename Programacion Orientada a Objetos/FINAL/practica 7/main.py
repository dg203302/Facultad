from gestor_certificado import *
from gestor_empleado import *
from gestor_programas import *
if __name__=='__main__':
    gestorprogramas=gestor_programas()
    gestorempleados=gestor_empleados()
    gestorcertificados=gestor_de_certificados(gestorempleados,gestorprogramas)
    gestorcertificados.mostrar()