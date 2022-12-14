# Ввод и вывод данных

print('Введите a')
a = float(input()) # если нужны целые числа то пишем int вместо float
print('Введите b')
b = float(input())

print(a,b)
print('{} {}'.format(a,b))
print(f'{a} {b}')

print(a, '+', b, '=', a+b)