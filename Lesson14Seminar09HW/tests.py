from unittest import TestCase
from random import randint
from tasks import *


class TestFunctions(TestCase):
    def setUp(self):
        self.lst1 = [4, 2, 8, 1, 2]
        self.res_more_prev = [8, 2]
        self.res_uniq = [4, 8, 1]
        self.lst2 = [3, 2, 1]
        self.rand = randint(1, 10)
        self.lstm = [[randint(0, 9) for _ in range(3)] for _ in range(3)]

    # L06S04HW02
    def test_more_previous1(self):
        self.assertListEqual(more_previous(self.lst1), self.res_more_prev)

    def test_more_previous2(self):
        self.assertFalse(more_previous(self.lst2))

    # L06S04HW04
    def test_unique_elements1(self):
        self.assertListEqual(unique_elements(self.lst1), self.res_uniq)

    def test_unique_elements2(self):
        self.assertTrue(unique_elements(self.lst2))

    # L11S07HW02
    def test_road1(self):
        self.assertEqual(Road(20, 5000).get_asphalt(), 12500)

    def test_road2(self):
        self.assertIsInstance(Road(self.rand * 10, self.rand * 1000), Road)

    # L12S08HW01
    def test_matrix1(self):
        self.assertListEqual(Matrix(self.lstm).list_out, self.lstm)

    def test_matrix2(self):
        self.assertIsNot(Matrix(self.lstm).list_out, self.lstm)

    def test_matrix3(self):
        self.assertTupleEqual(tuple(Matrix(self.lstm).size()), (3, 3))

    def test_matrix4(self):
        self.assertIsInstance(Matrix(self.lstm), list)

    # L12S08HW03
    def test_div1(self):
        self.assertAlmostEqual(div(1, 3), 0.333, 3)

    def test_div2(self):
        self.assertRaises(ZeroDivError, div, self.rand, 0)
