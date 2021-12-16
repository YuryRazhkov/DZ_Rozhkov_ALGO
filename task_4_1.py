"""1. Проанализировать скорость и сложность одного любого алгоритма, разработанных
в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
   Алгоритм: 3. Сформировать из  числа
   обратное по порядку входящих в него цифр и вывести на экран.
   Например, если введено число 3486, то надо вывести число 6843.
"""

import cProfile
import timeit
from random import randint


# 3.1 Простой срез
def first_func(a):
    return a[::-1]  # Самый быстрый быстрый алгоритм.


# 3.2 С использованием цикла и строковых методов
def second_func(a):
    result = ''
    for i in range(1, len(a) + 1):
        result += str(a[-i])
        i += 1
    return int(result)  # Алгоритм выполнянется примерно в 2 раза дольше первого.


# 3.3 С использованием цикла и деления
def third_func(a):
    result = 0
    a_int = int(a)
    for i in range(1, len(a) + 1):
        x = (a_int % 10) * 10 ** (len(a) - i)
        a_int //= 10
        result += x
    return result


a = randint(90 ** 10000, 99 ** 10000)


def main():
    start1 = timeit.default_timer()  # Самый быстрый быстрый алгоритм.
    first_func(str(a))
    print(timeit.default_timer() - start1, ' - Простой срез')

    start2 = timeit.default_timer()  # Алгоритм выполнянется примерно в 2-3 раза дольше первого.
    second_func(str(a))
    print(timeit.default_timer() - start2, ' - С использованием цикла и строковых методов')

    start3 = timeit.default_timer()  # Самый долгийю Выполняется на порядки дольше предыдущий.
    third_func(str(a))
    print(timeit.default_timer() - start3, ' - С использованием цикла и деления')

    print('\n', '*' * 100, '\n')


main()
# 0.0081045  - Простой срез
# 0.02333310000000001  - С использованием цикла и строковых методов
# 4.6830801  - С использованием цикла и деления


if __name__ == '__main__':
    import cProfile

cProfile.run('first_func(str(a))')
print('\n', '*' * 100, '\n')
cProfile.run('second_func(str(a))')
print('\n', '*' * 100, '\n')
cProfile.run('third_func(str(a))')

# 4 function calls in 0.008 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.007    0.007    0.008    0.008 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_4_1.py:15(first_func)
#         1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# ****************************************************************************************************
#
#          5 function calls in 0.016 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.008    0.008    0.016    0.016 <string>:1(<module>)
#         1    0.009    0.009    0.009    0.009 task_4_1.py:19(second_func)
#         1    0.000    0.000    0.016    0.016 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#
#  ****************************************************************************************************

#          19961 function calls in 4.487 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.007    0.007    4.487    4.487 <string>:1(<module>)
#         1    4.477    4.477    4.479    4.479 task_4_1.py:27(third_func)
#         1    0.000    0.000    4.487    4.487 {built-in method builtins.exec}
#     19957    0.002    0.000    0.002    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
