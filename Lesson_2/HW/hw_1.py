import random

n = input("Введите кол-во монеток ")
n = int(n)
while True:
    r = random.randrange(0, n)
    o = random.randrange(0, n)
    if r + o == n:
        break
print('Решка', r)
print('Орел', o)
if r > o:
    print(n - r)
else:
    print(n - o)
