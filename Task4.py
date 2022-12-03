# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Без применения встроеных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

number = int(input('Введите десятичное число: '))

# Вариант 1. Через строку и список + инверсия списка
# list_inverted = []
# list = []
# new_binary_number = ''

# К в.1 - вариант 1 цикла для записи исходного списка
# while number > 0:
#     number_division = number // 2
#     item = number - (number // 2) * 2
#     number = number_division
#     list_inverted.append(item)

# К в.1 - вариант 2 цикла для записи исходного списка
# while number > 0:
#     number_ost = number % 2
#     number = number // 2
#     list_inverted.append(number_ost)

# for i in range(len(list_inverted)):
#     list.append(str(list_inverted[len(list_inverted) - 1 - i]))
#
# new_binary_number = ''.join(list)
# print(f'Введенное число в двоичной системе счисления - это {new_binary_number}')



# Вариант 2.Арифметически
# d10 = 1
# result = 0
#
# while number != 0:
#     result += number % 2 * d10
#     number = number // 2
#     d10 *= 10
# print(f'Введенное число в двоичной системе счисления - это {result}')
