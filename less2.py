import numpy as np
import time
print('-- Задача 1 --')
# -- Задача 1 --
# Подгрузка массива
trainvectorpath = 'train_vector_1.csv'
my_array = np.loadtxt(trainvectorpath) 
print(my_array, '\n\nТип:', type(my_array))

print()
print('-- Задача 2 --')

# -- Задача 2 --
# Среднее арифметическое
# sum - встроенная функция подсчета суммы
srarif = sum(my_array)
print('Среднее значение:', srarif/2, '\n')

# Преобразование массива в список
mylist = [my_array]
print(mylist)

# Время выполнение кода
starttime = time.time()
print("\nВремя выполнения кода: %s секунд" % (time.time() - starttime))

print()
print('-- Задача 2 --')

# -- Задача 3 --
# Подгрузка двумерного массива
irispath = 'iris.csv'
my2darray = np.loadtxt((irispath), dtype=object) #dtype=object - получил массив ссылок, иначе ошибка типизации str to float
print('\n\n', my2darray)

print()

matrixprov = [[1, 2, 3], # matrixprov подставить вместо my2darray для проверки корректной работы
          [2, 3, 4],
          [2, 3, 5]]
#print(np.asarray(my2darray).sum(axis=0)) # np.asarray - привести к np массиву
# axis = 0 - по столбцам, axis = 1 - по строкам; используется для индексации
print(my2darray.sum(axis=0)) # вывод суммы элементов массива по столбцам

print()
print('-- Задача 4 --')

# -- Задача 4 --
# Массив 3x3 [range: 11-40]
array3d = [np.arange(11, 41), np.arange(11, 41), np.arange(11, 41)]
for i4 in range(len(array3d)):
    print(array3d[i4][array3d[i4] < 20])
    print(array3d[i4][array3d[i4] < 20].sum())
    


print()
print('-- Задача 5 --')

# -- Задача 5 --
ray5 = np.array([
    ['Student1', 22, 5.0],
    ['Student2', 18, 3.3],
    ['Student3', 25, 4.8]
])
print(ray5)
ray5.sort()
print('\n Отсортированный массив:\n', ray5)
ray5[0, 0] = 10 # 0, 0 - 1ый столбец, 1ая строка (1ый элемент)
ray5[1, 0] = 10
ray5[2, 0] = 10
print('\n', ray5)