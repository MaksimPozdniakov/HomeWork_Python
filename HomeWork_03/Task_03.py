# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import random
#
# my_float_list = [round(random.uniform(2, 5), 2) for i in range(7)]
# print(my_float_list)
#
# min = my_float_list[0]
# max = my_float_list[0]
#
# for i in range(len(my_float_list)):
#     if my_float_list[i] < min:
#         min = my_float_list[i]
#     elif my_float_list[i] > max:
#         max = my_float_list[i]
# print(min)
# print(max)
# print(round((max - min), 2))