# -- Задача 1 --
# Считайте с входящей строки два целых числа и выведите их сумму, разность, произведение.
perstr = int(input('Введите 1ое число: '))
vtstr = int(input('Введите 2ое число: '))
summ = perstr + vtstr
proiz = perstr * vtstr
razn = perstr - vtstr
print('Сумма: ', summ, 'Произведение: ', proiz, 'Разность: ', razn)


# -- Задача 2 --
# Дан ряд целых чисел от 10 до 25 включительно. Используя цикл for выведите на экран сумму двух последовательно идущих чисел.
ryadcel = [ 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
ryadcelspis = []
i = 0
for j in range(len(ryadcel) - 1):
    ryadcelspis.append(ryadcel[i] + ryadcel[i+1])
    i +=1
print(ryadcelspis)

print()

# -- Задача 3 --
# Для ряда целых чисел от 100 до 150 включительно выведите на экран только те, что делятся на 5 без остатка.
for k in range(100, 151): # range - диапазон # диапазон берет с -1
    while k % 5 == 0:
        print(k)
        k -= 1

print()

# -- Задача 4 --
# Проверка условий
N = int(input('Число: '))
if (N % 2 != 0):
    print('N нечетное')
elif ((N % 2 == 0) and (N >= 5) and (N <= 10)):
    print('N четное и принадлежит интервалу [5, 10]')
elif ((N % 2 == 0) and (N > 10)):
    print('N четное и N > 10')
elif ((N % 2 == 0) and (N < 5)):
    print('N четное и N < 5')

print()

# -- Задача 5 --
# Используя цикл while, посчитайте и выведите на экран сумму всех целых чисел от 15 до 22 включительно.
sumcelch2 = range(15, 23) # range [start | stop | step]
value = 0
while value == 0:
    print('Сумма всех целых чисел:', sum(sumcelch2))
    value = 1


print()

# -- Задача 6 --
# Используя цикл for, найдите сумму всех элементов заданного списка. (Без использования встроенных функций sum и т.д.)
my_list6 = [56, 23, 67, 45, 67, 2, 47, 158, 31, 34, 78, 23, 78, 23, 89, 23, 36]
sum6 = 0
for i6 in my_list6:
    sum6 += i6
print('Сумма всех элементов:', sum6)


print()

# -- Задача 7 --
# найдите значение максимального элемента списка... без max..
ss = 0
for i7 in range(len(my_list6)):
    if my_list6[i7] > ss:
        ss = my_list6[i7]
print('Максимальный элемент массива:', ss)

print()

# -- Задача 8 --
# Создать словарь
newdict = {
    'Nata': 2,
    'Alina': 3,
    'Marat': 5,
    'Lev': 1,
    'Valera': 0
}
print('Словарь:', newdict)

# -- Задача 9 --
# Обновить словарь
newdict.update({'Roma':4})
print('Обновленный словарь:', newdict)
