def count_of_num(my_list, count=0):
    for i in range(1, len(my_list) - 1):
        if my_list[i - 1] < my_list[i] > my_list[i + 1]:
            count += 1
    return count


list1 = [int(input(f'list[{i}] = ')) for i in range(int(input('len of list = ')))]
print(f'Count = {count_of_num(list1)}')

# Var2
# print(len([i for i in range(1, len(list1) - 1) if list1[i] == max(list1[i - 1:i + 2])]))
