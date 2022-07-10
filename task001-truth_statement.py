# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x, y, z = map(int, input('Введите три цифры через пробел: ').split())
if not (x and y and z) == (not x) or (not y) or (not z):
    print('True')
    print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z}')
else:
    print('False')