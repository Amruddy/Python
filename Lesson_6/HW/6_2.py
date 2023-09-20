# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

nums = []

n = int(input("Введите количество элементов: "))

for i in range(n):
  nums.append(random.randint(0, 100))

print(nums)


min_val = int(input('Введите диапозон от: '))
max_val = int(input('Введите диапозон до: '))

indexes = []

for i in range(len(nums)):
  if min_val <= nums[i] <= max_val:
    indexes.append(i)

print(indexes)