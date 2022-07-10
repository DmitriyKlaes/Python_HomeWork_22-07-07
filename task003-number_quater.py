# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).


def correct_value():  # Позволяет ввести в строку только числовое значение от 1 до 4
    result = input('Введите номер четверти: ')
    while not result.isdigit() or 1 > int(result) or int(result) > 4:
        result = input('Неверный ввод! Введите цифру от 1 до 4: ')
    return int(result)


def range_coordinates(quater_number):  # Основная функция для вывода возможных точек
    if quater_number == 1:
        print(f'Диапазон значений {quater_number} четверти: x > 0; y > 0')
    elif quater_number == 2:
        print(f'Диапазон значений {quater_number} четверти: x > 0; y < 0')
    elif quater_number == 3:
        print(f'Диапазон значений {quater_number} четверти: x < 0; y < 0')
    elif quater_number == 4:
        print(f'Диапазон значений {quater_number} четверти: x < 0; y > 0')


range_coordinates(correct_value())