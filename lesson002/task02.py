# 2. Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N.
# *Пример:*
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import math


def mult():
    count = '1'
    for el in range(2, n + 1):
        if el == n:
            count += f'*{i}'
    return count


n = int(input('enter the number'))
for i in range(1, n + 1):
    factorial = (math.factorial(i))
    print(factorial, end=' ')
avg = [mult() for i in range(1, n + 1)]
print(avg)
