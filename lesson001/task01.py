# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет,
# является ли этот день выходным.
#
# Пример: 6 -> да
#         7 -> да
#         1 -> нет
# вариант 1
weeks = input('Введите число недели: ')
if weeks.isdigit():
    week = int(weeks)
    if 0 < week < 6:
        print('нет')
    elif 5 < week < 8:
        print('да')
    else:
        print('ОТ 1го ДО 7. что тут не понятного')
else:
    print('ОТ 1го ДО 7. что тут не понятного')

# week = int(input('Введите число недели от 1 до 7: '))
#
# if 0 < week < 6:
#     print('нет')
# elif 5 < week < 8:
#     print('да')
# else:
#     print('Введите число недели от 1 до 7')

# вариант 2
# while True:  # цикл нашел c интеренета
#     try:
#         weeks = int(input("Введите число недели от 1 до 7: "))
#     except:
#         print("Нужно ввести число, попробуйте ещё раз ...\n")
#         continue
#     break
# if 0 < weeks < 6:
#     print('нет')
# elif 5 < weeks < 8:
#     print('да')
# else:
#     print('ОТ 1го ДО 7. что тут не понятного')
# i = input()
# var = {1: 'Понидельник', # тут хотел продолжит, но не смог пока что )
#        2: 'Вторник'
#        }
#
# if i in ['6', '7']:
#     print('да')
# else:
#     print('нет')
