# Отсортируйте по возрастанию методом слияния
# одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

from random import uniform


def merge_sort(li, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(li, start, mid)
        merge_sort(li, mid, end)
        merge_list(li, start, mid, end)


def merge_list(li, start, mid, end):
    left = li[start:mid]
    right = li[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            li[k] = left[i]
            i = i + 1
        else:
            li[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            li[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            li[k] = right[j]
            j = j + 1
            k = k + 1


li = [uniform(0, 50) for i in range(10)]
print(li, ' - исходный массив')
merge_sort(li, 0, len(li))
print(li, ' - отсортированный массив')
