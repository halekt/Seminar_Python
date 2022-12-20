# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int


import random
list_1 = [-5,-4,-3,-1,0,1,2,3,4,5]
print ("исходный список: " + str(list_1))
for i in range(len(list_1)-1, 0, -1):
    j = random.randint(0, i + 1) 
    list_1[i], list_1[j] = list_1[j], list_1[i] 
print ("Перемешанный список: " +  str(list_1))

