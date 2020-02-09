# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру,
# например словарь.
# Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров,
# отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка:
# постарайтесь по возможности реализовать
# в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.


Printer = ('HP Laserjet 2130', 1950, '4800x1200', 'A4', 'laserjet')
Scanner =  ('CANON Pixma MG3640S BK', 3640, '4800x1200', 'A4', 'inkjet')
Xerox = ('XEROX CopyCentre C118', 87800, '600x600', 'A3', 18, 10000)

class Warehouse:


    __equipments = dict()
    __issued_equipments = dict()

    def add_Equipment(self, key, value):

        if self.__equipments.get(key) == None:
         self.__equipments[key] = 0
        self.__equipments[key] += value

class Office (Warehouse):
    def __init__(self):
        print("Оргтехника")
    def put_paper (self):
        print("Метод Закладка бумаги")
    def reception (self):
        print("Прием")
    def broadcast (self):
        print("Передача")

class Printer (Office):
    def __init__(self):
        print("Принтер")
    def put_paper(self):
        print("Метод Закладка бумаги")
    def print (self):
        print("Печать")
    def reception(self):
        print("Прием")
    def broadcast(self):
        print("Передача")

class Scanner (Office):
    def __init__(self):
        print("Сканер")
    def put_paper(self):
        print("Метод Закладка бумаги")
    def scan (self):
        print("Сканирование")
    def reception(self):
        print("Прием")
    def broadcast(self):
        print("Передача")

class Xerox (Office):
    def __init__(self):
        print("Ксерокс")
    def put_paper(self):
        print("Метод Закладка бумаги")
    def xer (self):
        print("Копирование")
    def reception(self):
        print("Прием")
    def broadcast(self):
        print("Передача")

warehouse = Warehouse(dict)
warehouse.add_Equipment()
office = Office()
office.put_paper()
office.reception()
office.broadcast()
printer =Printer()
printer.put_paper()
printer.print()
print.reception()
print.broadcast()
scanner =  Scanner ()
scanner.put_paper()
scanner.scan ()
scanner.reception()
scanner.broadcast()
xerox = Xerox()
xerox.put_paper()
xerox.xer()
xerox.reception()
xerox.broadcast()


