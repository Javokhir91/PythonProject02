# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

num = input("enter num:\n ")
sum = 0
for i in str(num):
    if i != ",":
        if i != ".":
            sum += int(i)
print(" ")
print(sum, end=" ")
