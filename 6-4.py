'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f'Машина {self.color} {self.name} поехала.')

    def stop(self):
        print(f'Машина {self.color} {self.name} остановилась.')

    def turn(self, direction):
        print(f'Машина {self.color} {self.name} повернула на {direction}.')

    def show_speed(self):
        print(f'Скорость машины {self.color} {self.speed}.')


class TownCar(Car):
    def show_speed(self):
        print(f'Скорость машины {self.color} {self.name} {self.speed}.')
        if self.speed > 60:
            print('Превышение скорости.')


class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость машины {self.color} {self.name} {self.speed}.')
        if self.speed > 40:
            print('Превышение скорости.')


class PoliceCar(Car):
    pass


car = Car(50, 'красный', 'мазда')
car.go()
car.turn('право')
car.show_speed()
car.stop()

police_car = PoliceCar(80, 'синий', 'полиция')
police_car.go()
police_car.turn('право')
police_car.show_speed()
police_car.stop()

town_car = TownCar(70, 'зеленый', 'форд')
town_car.go()
town_car.turn('право')
town_car.show_speed()
town_car.stop()

work_car = WorkCar(50, 'феолетовый', 'таёта')
work_car.go()
work_car.turn('право')
work_car.show_speed()
work_car.stop()
