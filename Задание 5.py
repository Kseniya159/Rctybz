# Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле
# и выводить ее на экран.
f = open("text77.txt", "w")
print ("22 36 37 85 12 14", file= f)
f = open("text77.txt", "r")
summa = f.readline().split()
a,b,c,d,f,e = int(summa[0]), int(summa[1]), int (summa[2]), int (summa [3]), int (summa[4]), int (summa[5])
print(a+b+c+d+f+e)