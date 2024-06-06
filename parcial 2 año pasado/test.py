from carga import *
from pasajeros import *
from gestorvehiculos import *
import unittest
class testcosas(unittest.TestCase):
    __gest:gestorvehiculos
    __claseeje1:carga
    __claseje2:pasajeros
    def setUp(self):
        self.__gest=gestorvehiculos()
        self.__claseeje1=carga('ford','2002','775an556', 5000, 30, 600)
        self.__claseje2=pasajeros('renault','2020','754fn534', 6000, 30, 8)
    def testcarga(self):
        self.__gest.agreg(self.__claseeje1)
        self.assertEqual(isinstance(self.__gest.getuldat(),type(self.__claseeje1)),True)