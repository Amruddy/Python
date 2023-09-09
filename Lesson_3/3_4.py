# Дан массив, состоящий из целых чисел. Напишите программу, 
# которая подсчитает количество элементов массива,больших 
# предыдущего (элемента с предыдущим номером)

# Input: [0, -1, 5, 2, 3]
# Output: 2
# Пояснение: (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения списка или список задан изначально.

num_list = [0, -1, 5, 2, 3, 87, 5]
count = 0

for i in range (len(num_list) - 1):
    if num_list[i] < num_list[i + 1]:
        count += 1
print(count)

res_list = [num_list [i + 1] if num_list[i] < num_list[i + 1] else 0 for i in range (len(num_list) - 1) ]
print(res_list)
