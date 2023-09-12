# '''Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

new = "a a a b c a a d c d d".split()
print(new)
dict_1 ={}
for letter in new[:-1]:
    if letter in dict_1:
        dict_1[letter] += 1
        print(letter + "_" + str(dict_1[letter]), end = " ")
    else:
        dict_1[letter] = 0
        print(letter, end = " ")
if new[-1] in dict_1:
    dict_1[new[-1]] += 1
    print(new[-1] + "_" + str(dict_1[new[-1]]))
else:
    dict_1[new[-1]] = 0
    print(new[-1])

