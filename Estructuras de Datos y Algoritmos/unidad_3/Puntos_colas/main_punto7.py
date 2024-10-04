from cajeros import *
cajeros_atender=cajeros()
for i in range(0,10):
    cajeros_atender.agregar_clientes(i)
    cajeros_atender.atender()
    cajeros_atender.aumentar_cronometro()
cajeros_atender.mostrar_cantidades_promedios()