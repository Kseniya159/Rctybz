#Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
#Пример файла:
#Иванов 23543.12
#Петров 13749.32
f = open ("text10.txt", "w")
print("Иванов  15423", file=f)
print("Петров  20425",file=f)
print("Сидоров  23525",file=f)
print("Кукушкин 45145",file=f)
print("Бессонов  36412",file=f)
print("Жуков 35123", file=f)
print("Захаров  24125",file=f)
print("Кабанов  51425", file=f)
print("Токмаков  23500",file=f)
print("Гречка  33123", file=f)

with open ("text10.txt", "r") as f:
    summa = []
    less = []
    line = f.read().split('n')
    for i in line:
        i = i.split()
        if int(i[1]) < 20000:
            less.append(i[0])
        summa.append(i[1])

print (f"Salary {less}.Average salary - {sum(map(int, summa))/ len(summa)}")
