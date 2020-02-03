# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, stationery_title):
        print("Запуск отрисовки")
        self.stationery_title = stationery_title
    def draw (self):
         print("Родительский метод класса Stationery")
class Pen (Stationery):
    def __init__(self, pen_title):
        self.pen_title = pen_title
    def draw(self):
        print("Родительский метод класса Pen")
class Pencil (Stationery):
     def __init__(self, pencil_title):
        self.pencil_title = pencil_title
     def draw(self):
         print("Родительский метод класса Pencil")
class Handle:
    def __init__(self, handle_title):
       self.handle_title = handle_title
    def draw(self):
        print("Родительский метод класса Handle")

s = Stationery(1)
s.draw()

p = Pen(1)
p.draw()

p1=Pencil(1)
p1.draw()

h = Handle(1)
h.draw()











