# Реализовать базовый класс Worker (работник). Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).


class IsString:
    def __set__(self, instance, value):
        if type(value) != str:
            raise TypeError(f' {self.my_attr} должно быть строка!')
        elif not value.istitle():
            raise ValueError(f' {self.my_attr} должно быть написано с заглавной буквы!')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class NonNegative:
    def __set__(self, instance, value):
        if type(value) not in (int, float):
            raise TypeError(f' {self.my_attr} должно быть число!')
        elif value < 0:
            raise ValueError(f' {self.my_attr} должно быть неотрицательным числом!')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker():
    name = IsString()
    surname = IsString()
    wage = NonNegative()
    bonus = NonNegative()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self.wage + self.bonus

    def __str__(self):
        return f"Имя: {self.get_full_name()}\nЗарплата: {self.get_total_income()}\n"
