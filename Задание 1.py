# Создать класс TrafficLight (светофор)
# и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

class TrafficLight:
    trafficLight_color = "Красный"
    trafficLight_color_1="Желтый"
    trafficLight_color_2 = "Зеленый"
    def on_TrafficLight_running (self, trafficLight_name, trafficLight_name_1,trafficLight_name_2 ):
        print("Запуск")
        self__trafficLight_name = trafficLight_name
        self__trafficLight_name_1 = trafficLight_name_1
        self__trafficLight_name_2 =trafficLight_name_2
        TrafficLight.trafficLight_color

t = TrafficLight()
t.on_TrafficLight_running("Красный","Желтый","Зеленый")

import time
time.sleep(7)
print(t.on_TrafficLight_running)
print(t.trafficLight_color)

t_2 = TrafficLight()
t.on_TrafficLight_running("Красный","Желтый","Зеленый")
import time
time.sleep(2)
print(t.on_TrafficLight_running)
print(t.trafficLight_color_1)

t_3 = TrafficLight()
t.on_TrafficLight_running("Красный","Желтый","Зеленый")
import time
time.sleep(5)
print(t.on_TrafficLight_running)
print(t.trafficLight_color_2)