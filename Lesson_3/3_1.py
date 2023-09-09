my_list = []

for i in range(5):
    my_list.append(input('ВВедите числа: '))    
print(my_list)
my_set = set(my_list)
print(*my_set)
print(len(my_set))