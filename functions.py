from random import randint as rnd  # случайные int числа, которые находятся в определенном интервале [x, y]
from random import uniform as uni  # случайные float числа, которые находятся в определенном интервале [x, y]

def full_randon_int_list(min_value, max_value):  # Заполнение списка заданного размера рандомными int значениями.
    size = int(input('Введите длину списка: '))
    list = []
    for i in range(size):
        list.append(rnd(min_value, max_value))
    return list


def full_randon_float_list(min_value, max_value,
                           num_round):  # Заполнение списка заданного размера рандомными float значениями.
    size = int(input('Введите длину списка: '))
    list = []
    for i in range(size):
        list.append(round(uni(min_value, max_value), num_round))
    return list


def search_max(list):  # поиск максимального элемента в списке
    max = list[0]
    for i in range(1, len(list)):
        if list[i] > max:
            max = list[i]
    return max


def search_min(list):  # поиск минимального элемента в списке
    min = list[0]
    for i in range(1, len(list)):
        if list[i] < min:
            min = list[i]
    return min
