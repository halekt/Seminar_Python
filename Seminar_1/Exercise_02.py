# Задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1 
# - x=-34; y=-30 -> 3

while True:
    try:
        x = float(input('Введите координаты точки Х: '))
        y = float(input('Введите координаты точки Y: '))
        break
    except:
        print("Введите целое или дробное число через точку ")

if x > 0 and y > 0:
    print('Координаты точки X и Y принадлежат к 1-ой четверти')

elif x < 0 and y > 0:
    print('Координаты точки X и Y принадлежат к 2-ой четверти')


elif x < 0 and y < 0:
    print('Координаты точки X и Y принадлежат к 3-ей четверти')

elif x > 0 and y < 0:
    print('Координаты точки X и Y принадлежат к 4-ой четверти')

else:
    print('Координаты не должны быть равны 0')


