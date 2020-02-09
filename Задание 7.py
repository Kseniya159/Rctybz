# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта,
# создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
class Complex:
    def __init__(self,num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
     return self.num_1 + other.num_1, self.num_2 + other.num_2
    def __mul__(self, other):
     return self.num_1*self.num_2 - other.num_1*other.num_2 + self.num_1*other.num_2 + other.num_1*self.num_2
     def __str__(self):
         return self.num_1, self.num_2

res = Complex(1,2)
res_2 = Complex (2,3)
res_3 = res + res_2
print(res_3)
res_4 = res * res_2
print(res_4)