# Файлы
# Как работать с файлами:
# Связать файловую переменную с файлом,
# определив модификатор работы
# а - открытие для добавления данных
# r - открытие для чтения данных
# w - открытие для записи данных
# w+, r+

# лучший вариант
# with open('file.txt', 'w') as data:
#     data.write('line_1\n')
#     data.write('line_2\n')

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w')
# # data.writelines(colors)  # разделителей не будет
# data.writelines('LINE 2\n')
# data.writelines('LINE 3\n')
# data.close()

# path = 'file.txt'  # открываем файл
# data = open(path, 'r')  # читаем содердимое в файле
# for line in data:
#     print(line)
# data.close()

# exit()


