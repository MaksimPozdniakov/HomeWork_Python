# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование
# библиотеки Random для и получения случайного int

import random

my_list = [1, 2, 3, 4, 5, 6, 7]
copy_list = my_list[:]

for i in range(len(my_list)):
    random_num = random.randint(0, (len(my_list)) - 1)
    copy_list[i], copy_list[random_num] = copy_list[random_num], copy_list[i]

print(my_list)
print(copy_list)









