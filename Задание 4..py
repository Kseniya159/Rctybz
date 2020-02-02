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
        self.car_speed = car_speed
        self.car_color = car_color
        self.car_name = car_name
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
      i = 0
      while i < 60:
        print("Превышение скорости")
        break

class SportCar (Car):
    def sportcar_method (self):
        print("Дочерний метод класса SportCar")
class WorkCar (Car):
    def workcar_method (self):
        print("Дочерний метод класса WorkCar")
    def on_car_show_speed (self):
         print("Текущая скорость автомобиля")
    i = 0
    while i < 40:
       print("Превышение скорости")
       break



class PoliceCar (Car):
    def policecar_method (self):
        print("Дочерний метод класса PoliceCar")


#c = Car(50, "красный", "Toyota")
#print(Car.car_speed())
#print(Car.car_color())
#print(Car.car_name())
print(Car.on_car_go(0))
print(Car.on_car_stop(0))
print(Car.on_car_turn(0))
print(Car.on_car_show_speed(40))
print(TownCar.towncar_method (0))
print(TownCar.on_car_show_speed(0))
print(SportCar.sportcar_method (0))
print(WorkCar.workcar_method (0))
print(WorkCar.on_car_show_speed (0))
print(PoliceCar.policecar_method (0))