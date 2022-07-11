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

# pillar = input('Введите номер последнего столбика: ')
# while not pillar.isdigit() or 1 > int(pillar) or int(pillar) > 45:
#     pillar = input('Неверный ввод! Введите число от 1 до 45: ')
# # Программа не выполняется, пока не введешь цифру ор 1 до 45
# pillar = int(pillar)
# start_pillar = 0
# second_pillar = 1
# result = 0
# for i in range(pillar-1):
#     result = start_pillar + second_pillar
#     start_pillar = second_pillar
#     second_pillar = result
# print(result)

def correct_value():  # Позволяет ввести в строку только числовое значение
    result = input('Введите номер последнего столбика: ')
    while not result.isdigit() or 1 > int(result) or int(result) > 45:
        result = input('Неверный ввод! Введите число от 1 до 45: ')
    return int(result)


def pillars_way(n):
    if n == 1 or 2:
        return 1
    else:
        result = 0
        return result + pillars_way(n-1) + pillars_way(n-2)

pillar = correct_value()
print(pillars_way(pillar))