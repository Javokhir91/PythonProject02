# 3'. Задайте список из вещественных чисел. Напишите программу, ' \
# которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lists = [1.1, 1.2, 3.1, 5, 10.01]
# lists_new = []
# for i in lists:
#     if i % 1 != 0:
#         lists_new.append(round(i % 1, 2))
# print(f"{lists_new} => {max(lists_new) - min(lists_new)}")

# lst = [1.1, 1.2, 3.1, 5, 10.01]
lists_new = [round(i % 1, 2) for i in lists if i % 1 != 0]
# print(max(new_lst) - min(new_lst))
print(f"{lists_new} => {max(lists_new) - min(lists_new)}")