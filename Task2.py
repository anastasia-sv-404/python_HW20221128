# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

import functions

list = functions.full_randon_int_list(1, 10)
print(list)

list_multiply = []

if len(list) % 2 == 0:
    size_new = int(len(list) / 2)
    for i in range(size_new):
        list_multiply.append(list[i] * list[len(list) - i - 1])
else:
    size_new = int(len(list) / 2) + 1
    for i in range(size_new):
        list_multiply.append(list[i] * list[len(list) - i - 1])
print(list_multiply)
