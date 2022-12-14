# Задача №4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек
# в этой четверти (x и y).

# quart_number = int(input('Введите № четверти: '))

# if quart_number == 1:
#     print("x > 0, y > 0")
# elif quart_number == 2:
#     print("x < 0, y > 0")
# elif quart_number == 3:
#     print("x < 0, y < 0")
# elif quart_number == 4:
#     print("x > 0, y < 0")
# else:
#     print('Четверти с таким номером нет')


quart_number = int(input('Введите № четверти: '))

while quart_number > 0 and quart_number < 5:

    if quart_number == 1:
        print("x > 0, y > 0")
        break
    elif quart_number == 2:
        print("x < 0, y > 0")
        break
    elif quart_number == 3:
        print("x < 0, y < 0")
        break
    elif quart_number == 4:
        print("x > 0, y < 0")
        break

else:
    quart_number = int(input('Введите № четверти: '))
    print('Четверти с таким номером нет')