# Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк,
# количества слов в каждой строке.
counter = 0
with open("text7.txt", "w") as fail_color:
  print("green, white, black ", file=fail_color)
  print("yello, wblue, grey", file=fail_color)
  print("purple, red, pink", file=fail_color)
for line in fail_color:
    counter +=1
    line_words = line.split("")
    print(line,len(line_words))
    print(conter)

