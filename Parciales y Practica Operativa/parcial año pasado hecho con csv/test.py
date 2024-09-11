from gestor import *
import unittest
class testEnt(unittest.TestCase):
    __lista:gestorservicios
    __eje:object
    def setUp(self):
        self.__lista=gestorservicios()
        self.__eje=transporte('transportes 1','jose','chile este 432','30/04/2024',10,4,54,'juan jufre',5)
        self.__lista.agreg(self.__eje)
    def testcarga(self):
        self.assertEqual(isinstance(self.__lista.getuldat(),type(self.__eje)),True)