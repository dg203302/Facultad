import unittest
from gestorclientes import *
class testeos(unittest.TestCase):
    __gestor:lista_gestor
    __cliente_nacional:nacionales
    __cliente_local:locales
    def setUp(self):
        self.__gestor=lista_gestor()
        self.__cliente_nacional=nacionales('diego','jose','dg15828@gmail.com','123455676','san juan', 'capital', '5400')
        self.__cliente_local=locales('jose','julian','nose12456@gmail.com','123455676','capital 5400', '264313245')
    def testcarga(self):
        self.assertIsInstance(self.__cliente_local,locales)
        self.assertIsInstance(self.__cliente_nacional,nacionales)