# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class IsPositive:
    def __set__(self, instance, value):
        if type(value) not in (int, float):
            raise TypeError(f'The {self.my_attr} must be a number!')
        elif value <= 0:
            raise ValueError(f'The {self.my_attr} must be a positive number!')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    _mass = 25
    _thickness = 5
    length = IsPositive()
    width = IsPositive()

    def __init__(self, length, width):
        self.length = length
        self.width = width


class Road1(Road):
    def __init__(self, length, width):
        super().__init__(length, width)

    def asphalt(self):
        return self.length * self.width * self._mass * self._thickness / 1000


class Road2(Road, metaclass=Singleton):
    def __init__(self, length, width):
        super().__init__(length, width)

    def asphalt(self):
        return self.length * self.width * self._mass * self._thickness / 1000
