# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
class Car:
    def __init__ (self, car_speed, car_color,car_name) :#car_is_police):
        car_name = "Toyota"
        car_color = "красный"
        car_speed = 60

        #self.car_is_police = car_is_police
    def on_car_go (self):
        print(" Машина поехала")
    def on_car_stop (self):
        print(" Машина остановилась")
    def on_car_turn (self):
        print(" Машина повернула")
    def on_car_show_speed (self):
         print("Текущая скорость автомобиля")
class TownCar(Car):
    def towncar_method (self):
        print("Дочерний метод класса TownCar")
    def on_car_show_speed (self):
      if self.car_speed > 60:
        print("Превышение скорости")
        return self.car_speed

class SportCar (Car):
    def sportcar_method (self):
        print("Дочерний метод класса SportCar")
class WorkCar (Car):
    def workcar_method (self):
        print("Дочерний метод класса WorkCar")
    def on_car_show_speed (self):
       if self.car_speed > 40:
        print("Превышение скорости")
        return self.car_speed



class PoliceCar (Car):
    def policecar_method (self):
        print("Дочерний метод класса PoliceCar")


c = Car("Toyota", "красный", 60 )

print(c.car_name)
print(c.car_color)
print(c.car_speed)

c.on_car_go()
c.on_car_stop()
c.on_car_turn()
c.on_car_show_speed()
t = TownCar()
t.towncar_method ()
print(t.on_car_show_speed())
s = SportCar()
s.sportcar_method ()
w = WorkCar
w.workcar_method ()
print(WorkCar.on_car_show_speed ())
p = PoliceCar
p.policecar_method ()