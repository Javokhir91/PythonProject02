# 4'.Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

decimal = int(input("enter decimal number: "))
gap = ''
while decimal > 0:
    gap = str(decimal % 2) + gap
    decimal //= 2
print(gap)
