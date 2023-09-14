# Напишите функцию, которая принимает одно число и проверяет, 
# является ли оно простым

# Напоминание: Простое число - это число, которое имеет 
# 2 делителя: 1 и n(само число)


# Input: 5

# Output: yes

def is_number_simple(num: int) -> bool:
    if num % 2 == 0 and num != 2:
        return False

    for i in range(3, num, 2):
        if num % i == 0:
            return False
    return True


n = int(input('Введите число: '))
if is_number_simple(num=n):
    print(f'Число {n} является простым')
else:
    print(f'Число {n} простым не является')