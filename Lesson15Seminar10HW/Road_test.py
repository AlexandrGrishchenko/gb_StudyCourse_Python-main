from unittest import TestCase
from Road_L11S07HW02 import *

class TestFunctions(TestCase):
    def test_road1_asphalt(self):
        self.assertEqual(Road1(20, 5000).asphalt(), 12500)

    def test_road1_typerr(self):
        with self.assertRaises(TypeError):
            Road1('20', 5000)

    def test_road1_valerr(self):
        with self.assertRaises(ValueError):
            Road1(20, -5000)

    def test_road1_inst(self):
        self.assertIsInstance(Road1(20, 5000), Road)

    def test_road1_is(self):
        self.assertIsNot(Road1(20, 5000), Road1(10, 2500))

    def test_road2_inst(self):
        self.assertIsInstance(Road2(20, 5000), Road)

    def test_road2_is(self):
        self.assertIs(Road2(20, 5000), Road2(10, 2500))
