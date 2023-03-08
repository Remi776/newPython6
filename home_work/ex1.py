a_1, d, n = int(input('Enter the first value of arithmetic progression: a_1 = ')), \
            int(input('Enter the common difference: d = ')), \
            int(input('Enter the length of arithmetic progression: length =  '))

print(*[a_1 + (i - 1) * d for i in range(1, n + 1)])
