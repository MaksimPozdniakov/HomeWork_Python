# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# без метода
# my_list = [2, 3, 5, 9, 3]
# sum = 0
#
# for i in range(len(my_list)):
#     if i % 2 != 0:
#         sum += my_list[i]
# print(sum)

# через отдельный метод
# def Sum_Of_Elements(my_list):
#     sum = 0
#
#     for i in range(len(my_list)):
#         if i % 2 != 0:
#             sum += my_list[i]
#     print(sum)
#
# my_list = [2, 3, 5, 9, 3]
# Sum_Of_Elements(my_list)