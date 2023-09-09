# Напишите программу для печати всех уникальных значений в словаре.

# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# Примечание: Список словарей задан изначально. Пользователь его не вводит

library = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
           {"VI": "S005"},  {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
res_list = []

for cur_dict in library:
    for key in cur_dict:
        res_list.append(cur_dict[key])

res_set = set(res_list)
print(res_set)