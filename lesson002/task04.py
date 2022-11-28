# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)


with open('file.txt', 'r') as data:
    positions = data.read().split('\n')
positions = list(map(int, positions))

n = int(input())
list_gen = [i for i in range(-n, n+1)]
multi = 1
for pos in positions:
    multi *= list_gen[pos]
print(positions)
print(list_gen)
print(multi)
