"""1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках
первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС."""



import sys
from random import randint
from timeit import default_timer


start = default_timer()
total_mem = 0
a = str(randint(90 ** 10000, 99 ** 10000))
print(sys.getsizeof(a), ' переменная "а" до разворота')
a = a[::-1]
# print(a)
print(sys.getsizeof(a[::-1]), ' переменная "а" развернутая простым срезом. # одинаково!')
total_mem += sys.getsizeof(a)

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

matrix = [[4, 5, 5, 4, 18],
          [8, 9, 9, 5, 31],
          [2, 4, 8, 1, 15],
          [5, 5, 1, 2, 13]]
print(sys.getsizeof(matrix), 'переменная matrix')
total_mem += sys.getsizeof(matrix)
result = []
for i in range(len(matrix)):
    a = min(matrix[i])
    result.append(a)
print(sys.getsizeof(a), 'последняя переменная a из цикла перебора матрицы')
total_mem += sys.getsizeof(a) # последняя переменная a из цикла)

# print(result)
print(sys.getsizeof(result), 'переменная result')
total_mem += sys.getsizeof(result)

print(default_timer() - start, 'sec.')
print(total_mem, 'bytes used memory')

