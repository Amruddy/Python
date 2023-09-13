# Задача – «На вход программе подаются цифры,как только пользователь введёт 0 ввод прекращается.
# Вывести наибольший элемент получившейся последовательности».
# Есть два кода с ошибками, нужно определить где ошибок меньше.

# Примечание: Программные коды на следующих слайдах

#Ваня:

n = int(input())
max_number = n # 1 max
while n != 0:
    if n > max_number: # 2
        max_number = n
n = int(input()) # 3
print(max_number)

# Петя:

# n = int(input())
# max_number = -1
# while n != 0: # 1 n < 0
#     if max_number < n:
#         max_number = n # 2 n = max_number
# n = int(input()) # 4
# print(max_number) # 3 print(n)