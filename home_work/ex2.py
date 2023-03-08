from random import randrange

my_list = [randrange(-10, 10) for _ in range(int(input('Enter the len of list: ')))]

n, m = int(input('lower value = ')), int(input('greater value = '))

print(my_list)
print(*[i for i, value in enumerate(my_list) if n <= value <= m])
