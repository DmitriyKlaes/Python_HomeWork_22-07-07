# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


def is_number(value):  # Определяет является ли строка числом
    try:
        float(value)
        return True
    except:
        return False


def correct_value():  # Позволяет ввести в строку только числовое значение
    result = input()
    while not is_number(result):
        result = input('Неверный ввод! Введите INT или FLOAT значение: ')
    try:
        int(result)
        return int(result)
    except:
        return float(result)


def distance_2d(x1, y1, x2, y2):  # Основной метод вычисления расстояния
    x = x2 - x1
    y = y2 - y1
    result = (x*x + y*y) ** 0.5
    return result


print('Введите координаты точки A: ')
x1, y1 = correct_value(), correct_value()
print('Введите координаты точки B: ')
x2, y2 = correct_value(), correct_value()
distance = distance_2d(x1, y1, x2, y2)
print(f'Расстояние между точками A [{x1}:{y1}] и B [{x2}:{y2}] в 2D пространстве равняется: {int(distance * 100) / 100}')