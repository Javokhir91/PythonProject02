# Реализуйте алгоритм перемешивания списка

import random

arr = list(map(int, input().split()))
print(f'list -> {arr}')
random.shuffle(arr)
print(f'shuffle -> {arr}')
