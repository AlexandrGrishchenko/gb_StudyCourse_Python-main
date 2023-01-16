from unittest import TestCase
from random import randint
from Worker_L11S07HW03 import *


class TestFunctions(TestCase):
    def setUp(self):
        self.wage = randint(50, 150) * 10 ** 3
        self.bonus = randint(self.wage // 4, self.wage // 2)

    def test_fullname(self):
        self.assertEqual(Position('Алекс', 'Смирнов', 'Сотрудник K', self.wage, self.bonus).get_full_name(), 'Алекс Смирнов')

    def test_total_income(self):
        self.assertEqual(Position('Алекс', 'Смирнов', 'Сотрудник K', self.wage, self.bonus).get_total_income(),
                         self.wage + self.bonus)

    def test_name(self):
        with self.assertRaises(TypeError):
            Position(1, 'Смирнов', 'Сотрудник K', self.wage, self.bonus)
            Position('Алекс', 1, 'Сотрудник K', self.wage, self.bonus)

        with self.assertRaises(ValueError):
            Position('алекс', 'Смирнов', 'Сотрудник K', self.wage, self.bonus)
            Position('Алекс', 'смирнов', 'Сотрудник K', self.wage, self.bonus)

    def test_income(self):
        with self.assertRaises(TypeError):
            Position('Алекс', 'Смирнов', 'Сотрудник K', str(self.wage), self.bonus)
            Position('Алекс', 'Смирнов', 'Сотрудник K', self.wage, str(self.bonus))

        with self.assertRaises(ValueError):
            Position('Алекс', 'Смирнов', 'Сотрудник K', -self.wage, self.bonus)
            Position('Алекс', 'Смирнов', 'Сотрудник K', self.wage, -self.bonus)

    def test_instance(self):
        self.assertIsInstance(Position('Алекс', 'Смирнов', 'Сотрудник K', self.wage, self.bonus), Worker)

    def test_is(self):
        self.assertIsNot(Position('Алекс', 'Смирнов', 'Сотрудник K', self.wage, self.bonus),
                         Position('Иван Иванов', 'Иванович', 'Сотрудник В', self.wage, 0))
