from ejemp import *
import unittest
class testsuma(unittest.TestCase):
    __ejmp:object
    def setUp(self):
        self.__ejmp=ejemp(2,2)
    def testsuma(self):
        self.assertEqual(self.__ejmp.suma(),4)
    def testresta(self):
        self.assertEqual(self.__ejmp.resta(),0)