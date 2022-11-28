# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И"
# вариант скопировал. мне не вообще понятно с координатами, с матиматикой -0 (

X = Y = Z = [True, False]
res = True
for x in X:
    for y in Y:
        for z in Z:
            if not (not (x or y or z) == (not x and not y and not z)):
                res = False
if res:
    res = 'Истина'
else:
    res = 'Ложь'
print(res)

# решали совместно с одногрупниками
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x or y or z) == (not x and not y and not z):
                print(f'Утветрждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z '
                      f'истинно при значении переменных :\n x = {x}, y = {y}, z = {z}')
