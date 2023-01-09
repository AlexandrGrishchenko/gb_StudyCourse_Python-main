# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
from random import randint


class Car:
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        #print(f'{self.color} {self.name} started moving.')
        return f'{self.color} {self.name} started moving.'

    def stop(self):
        #print(f'{self.color} {self.name} stopped.')
        return f'{self.color} {self.name} stopped.'

    def turn(self, direction):
        #print(f'{self.color} {self.name} turned {direction}.')
        return f'{self.color} {self.name} turned {direction}.'

    def show_speed(self):
        #print(f'{self.color} {self.name} is going at a speed of {self.speed} km/h.')
        return f'{self.color} {self.name} is going at a speed of {self.speed} km/h.'

    def __str__(self):
        return f'{self.name} {self.color} {self.speed} {self.is_police}'


class TownCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)
        self.is_police = False

    def show_speed(self):
        if self.speed <= 60:
            #print(f'{self.color} {self.name} is going at a speed of {self.speed} km/h.')
            return f'{self.color} {self.name} is going at a speed of {self.speed} km/h.'
        else:
            #print(f'{self.color} {self.name} exceeded the speed limit!')
            return f'{self.color} {self.name} exceeded the speed limit for town cars!'


class SportCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)
        #self.is_police = False

    def sport(self):
        if self.is_police:
            return f'{self.color} {self.name} is police car now.'
        else:
            return f'{self.color} {self.name} is sport car.'


class WorkCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)
        self.is_police = False

    def show_speed(self):
        if self.speed <= 40:
            #print(f'{self.color} {self.name} is going at a speed of {self.speed} km/h.')
            return f'{self.color} {self.name} is going at a speed of {self.speed} km/h.'
        else:
            #print(f'{self.color} {self.name} exceeded the speed limit!')
            return f'{self.color} {self.name} exceeded the speed limit for work cars!'


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)
        self.is_police = True


tc = TownCar('Lada', 'Red', randint(20, 80), False)
sc = SportCar('Audi', 'Blue', randint(40, 150), False)
wc = WorkCar('KAMAZ', 'Green', randint(15, 60), False)
pc = PoliceCar('Kia', 'Grey', randint(30, 160), True)

print(tc)
print(sc)
print(wc)
print(pc, '\n')

print(tc.go())
print(tc.show_speed(), '\n')

print(sc.sport())
sc.is_police = True
print(sc.sport())
print(sc.turn('left'))
print(sc.show_speed(), '\n')

print(wc.show_speed())
print(wc.stop(), '\n')

print(pc.go())
print(pc.show_speed())
