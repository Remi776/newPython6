def get_Sum(value):
    res = 1
    for i in range(2, int(value ** 0.5) + 1):
        if value % i == 0:
            res += i + value // i
    return res


user_num = int(input())

for j in range(220, user_num):
    sum1 = get_Sum(j)
    sum2 = get_Sum(sum1)
    if sum2 == j and sum1 > sum2:
        print(sum1, j)

