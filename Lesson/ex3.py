# my_list = [1, 2, 3, 4, 2, 3, 4, 3, 5, 6, 5, 3]
# copy_set_my_list = list(set(my_list))
# print(*my_list)
# print(*copy_set_my_list)
# print(sum(my_list.count(copy_set_my_list[i]) // 2 for i in range(len(copy_set_my_list))))
#
list_1 = [1, 2, 3, 4, 2, 3, 4, 3, 5, 6, 5, 3]
# list_2 = list(set(list_1))
# print(list_2)
# count = 0
# for i in range(len(list_2)):
#     count += list_1.count(list_2[i])//2
# print(count)

# -----------------------------Var2-------------------------------
# list_1 = [1, 2, 3, 4, 2, 3, 4, 3, 5, 6, 5, 3]             !!!!!!!!!!!!cпросить про присваемые ключи
# dict_list = dict.fromkeys(list_1, 0)
print(dict_list)
print(set(list_1))
for i in list_1:
    dict_list[i] += 1
print(list_1)
print(dict_list)
print(sum([i // 2 for i in dict_list.values() if not i % 2]))


