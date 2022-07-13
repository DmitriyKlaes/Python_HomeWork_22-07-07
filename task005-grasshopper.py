# Кузнечик прыгает по столбикам, расположенным на одной линии на равных расстояниях друг от друга.
# Столбики имеют порядковые номера от 1 до N. В начале Кузнечик сидит на столбике с номером 1.
# Он может прыгнуть на следующий столбик или сразу на второй столбик, считая от ткущего.
# Требуется найти количество способов, которыми Кузнечик может добраться до столбика с номером N.
# Учитывайте, что Кузнечик не может прыгать назад.
# Программа должна вывести одно число: количество способов,
# которыми Кузнечик может добраться до столбика с номером N.

# Входная строка содержит натуральное число N (1 <= N <= 45)

# Примеры:
# 3 -> 2
# 10 -> 55

def correct_value():  # Позволяет ввести в строку только числовое значение
    result = input('Введите номер последнего столбика: ')
    while not result.isdigit() or 1 > int(result) or int(result) > 45:
        result = input('Неверный ввод! Введите число от 1 до 45: ')
    return int(result)


pillar = correct_value()
start_pillar, second_pillar = 0, 1
for i in range(pillar-1):
    result = start_pillar + second_pillar
    start_pillar, second_pillar = second_pillar, result
print(result)

# Дальше закомменитрован рекурсивный метод поиска результата
# Но он мне не понравился, так как слишком долгое вычисление дальше 25

# def correct_value():  # Позволяет ввести в строку только числовое значение
#     result = input('Введите номер последнего столбика: ')
#     while not result.isdigit() or 1 > int(result) or int(result) > 45:
#         result = input('Неверный ввод! Введите число от 1 до 45: ')
#     return int(result)


# def pillars_way(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         result = pillars_way(n-1) + pillars_way(n-2)
#         return result

# pillar = correct_value()
# result = pillars_way(pillar)
# print(result)