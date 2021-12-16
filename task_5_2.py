"""  2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections
"""


from collections import deque


def sum_hex(x, y):
    hex_num = {}  # Преподователь не велел руками набирать. Только генерить
    for i in range(10):
        hex_num[str(i)] = i
        hex_num[i] = str(i)
    for i in range(ord('A'), ord('G')):
        hex_num[chr(i)] = i - ord('A') + 10
        hex_num[i - ord('A') + 10] = chr(i)


    result = deque()
    transfer = 0

    if len(y) > len(x):
        x, y = deque(y), deque(x)

    else:
        x, y = deque(x), deque(y)

    while x:

        if y:
            res = hex_num[x.pop()] + hex_num[y.pop()] + transfer

        else:
            res = hex_num[x.pop()] + transfer

        transfer = 0

        if res < 16:
            result.appendleft(hex_num[res])

        else:
            result.appendleft(hex_num[res - 16])
            transfer = 1

    if transfer:
        result.appendleft('1')

    return list(result)


def mult_hex(x, y):
    hex_num = {}
    for i in range(11):
        hex_num[str(i)] = i
        hex_num[i] = str(i)
    for i in range(ord('A'), ord('G')):
        hex_num[chr(i)] = i - ord('A') + 10
        hex_num[i - ord('A') + 10] = chr(i)

    result = deque()
    spam = deque([deque() for _ in range(len(y))])

    x, y = x.copy(), deque(y)

    for i in range(len(y)):
        m = hex_num[y.pop()]

        for j in range(len(x) - 1, -1, -1):
            spam[i].appendleft(m * hex_num[x[j]])

        for _ in range(i):
            spam[i].append(0)

    transfer = 0

    for _ in range(len(spam[-1])):
        res = transfer

        for i in range(len(spam)):
            if spam[i]:
                res += spam[i].pop()

        if res < 16:
            result.appendleft(hex_num[res])

        else:
            result.appendleft(hex_num[res % 16])
            transfer = res // 16

    if transfer:
            result.appendleft(hex_num[transfer])

    return list(result)


a = list(input('Введите 1-е шестнадцатиричное число: ').upper())
b = list(input('Введите 2-е шестнадцатиричное число: ').upper())
print(a, b)

print(*a, '+', *b, '=', *sum_hex(a, b))

print(*a, '*', *b, '=', *mult_hex(a, b))

# Введите 1-е шестнадцатиричное число: A1
# Введите 2-е шестнадцатиричное число: C3
# ['A', '1'] ['C', '3']
# A 1 + C 3 = 1 6 4
# A 1 * C 3 = 7 A A 3
