# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import functions

num_round = int(input('Введите количество знаков после запятой (округление результатов): '))

list = functions.full_randon_float_list(1, 10, num_round)
# list = [1.1, 1.2, 3.1, 5, 10.01]  # раскоммитить - для сверки с примером
list_new = []
list_fraction = []

print(f'Исходный список - это {list}')

for i in range(len(list)):  # удаляем целые значения из исходного списка
    if int(list[i]) != list[i]:
        list_new.append(list[i])
print(f'Список, содержащий только вещественные числа - это {list_new}')

for item in range(len(list_new)):  # формируем список, содержащий в себе только дробные части чисел
    list_fraction.append(round(list_new[item] * 10 % 10 / 10, num_round))
print(f'Список, содержащий дробные части вещественных чисел - это {list_fraction}')

max_element = functions.search_max(list_fraction)
min_element = functions.search_min(list_fraction)

print(f'Разница между максимальной и минимальной дробной частью - это {round(max_element - min_element, num_round)}')
