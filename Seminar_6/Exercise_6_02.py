# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

num = input("Введите число: ")
summ = 0
for i in num:
    if i.isdigit():
        summ += int(i)
print(summ)

# улучшение
num1 = input('Введите число: ')
summ = sum(map(int, num1.replace('.', '')))
print (summ)