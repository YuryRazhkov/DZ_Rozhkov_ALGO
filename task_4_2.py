# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»

# 1

def sieve1(n): #  в 20 раз быстрее вторго алгоритма
    sieve = dict()
    for i in range(2, n +1): sieve[i] = True
    for i in sieve:
        num = range(i, n +1, i)
        for f in num[1:]:
            sieve[f] = False
    return [i for i in sieve if sieve[i] == True]


# 2
def sieve2(n):
    sieve = set(range(2, n+1))
    nums = []
    while sieve:
        num = min(sieve)
        nums.append(num)
        sieve -= set(range(num, n + 1, num))
    return nums



def main():
    sieve1()
    sieve2()

if __name__ == '__main__':
    import cProfile

cProfile.run('sieve1(100000)')
print('\n', '*' * 100, '\n')
cProfile.run('sieve2(100000)')

 #
 #
 #         5 function calls in 0.302 seconds
 #
 #   Ordered by: standard name
 #
 #   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 #        1    0.002    0.002    0.302    0.302 <string>:1(<module>)
 #        1    0.006    0.006    0.006    0.006 task_4_2.py:14(<listcomp>)
 #        1    0.293    0.293    0.300    0.300 task_4_2.py:7(sieve1)
 #        1    0.000    0.000    0.302    0.302 {built-in method builtins.exec}
 #        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 #
 #
 #
 # ****************************************************************************************************
 #
 #         19188 function calls in 6.125 seconds
 #
 #   Ordered by: standard name
 #
 #   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 #        1    0.001    0.001    6.125    6.125 <string>:1(<module>)
 #        1    0.080    0.080    6.124    6.124 task_4_2.py:18(sieve2)
 #        1    0.000    0.000    6.125    6.125 {built-in method builtins.exec}
 #     9592    6.042    0.001    6.042    0.001 {built-in method builtins.min}
 #     9592    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
 #        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}