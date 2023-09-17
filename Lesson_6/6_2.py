# Пользователь вводит размер массива – N
# и элементы массива (целые числа).
# нужно из этого массива вывести количество элементов,
# у которых ближайшие соседние элементы меньше самого элемента.

# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1

# Вывод: Вывод:
# 0 2

from random import randint

n = randint(5, 10)
list_1 = [randint(1, 10) for _ in range(n)]
print(n ,list_1)
count_nums = 0

for i in range(1, n - 1):
    if list_1[i - 1] < list_1[i] > list_1[i + 1]:
        count_nums += 1

print(count_nums)