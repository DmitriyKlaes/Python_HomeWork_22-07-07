# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def is_number(value): # Определяет является ли строка числом
    try:
        float(value)
        return True
    except:
        return False


def correct_value(): # Позволяет ввести в строку только числовое значение
    result = input()
    while not is_number(result) or float(result) == 0:
        result = input(
            'Неверный ввод! Введите INT или FLOAT значение > или < 0: ')
    try:
        int(result)
        return int(result)
    except:
        return float(result)


def get_number_of_quater(x, y): # Основная функция для поиска четверти
    result = 0
    if (x > 0 and y > 0):
        result = 1
    elif (x > 0 and y < 0):
        result = 2
    elif (x < 0 and y < 0):
        result = 3
    elif (x < 0 and y > 0):
        result = 4
    return result


print('Введите координату X: ')
x = correct_value()
print('Введите координату Y: ')
y = correct_value()
quater = get_number_of_quater(x, y)
print(f'Точка {x}:{y} находится в {quater} четверти!')