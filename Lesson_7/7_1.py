# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# if values == transformed_values:
# print(‘ok’)
# else:
# print(‘fail’)

# - В переменную transformation нужно прописать такую функцию,
# что бы в переменной transormed_values получилась копия списка values - 2


transformation = lambda x: x - 2 + 9
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
if values == transormed_values:
    print('ok')
else:
    print('fail')
print(transormed_values)