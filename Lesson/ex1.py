my_list_1 = [3, 1, 3, 4, 2, 4, 12]
my_list_2 = [4, 15, 43, 1, 15, 1]

print(*[i for i in my_list_1 if i not in set(my_list_2)])