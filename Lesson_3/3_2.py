n = int(input("Insert lenght = > "))
k = int(input("Insert shift = > ")) % n

list_1 = [int(input("Insert number = > ")) for _ in range (1,n + 1)]
print(list_1)

list_2 = []
list_2 = list_1[-k:] + list_1[:-k]

print(list_2)