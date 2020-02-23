'''
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов
методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для
каждого экземпляра.
'''

class Stationery:
    def __init__(self, title):
        self.title =title

    def draw(self):
        print(f'“Запуск {self.title} отрисовки.”')


class Pen(Stationery):
    def draw(self):
        print(f'“Запуск {self.title} отрисовки ручкой.”')

class Pencil(Stationery):
    def draw(self):
        print(f'“Запуск {self.title} отрисовки карандашем.”')

class Handle(Stationery):
    def draw(self):
        print(f'“Запуск {self.title} отрисовки маркером.”')

stationery_name = Stationery('name')
stationery_name.draw()

pen_name = Pen('name')
pen_name.draw()

pencil_name = Pencil('name')
pencil_name.draw()

нandle_name = Handle('name')
нandle_name.draw()

