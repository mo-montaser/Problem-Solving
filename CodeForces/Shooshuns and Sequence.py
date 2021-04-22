# https://codeforces.com/problemset/problem/222/A

from collections import Counter

user_inputs = input().split(" ")
n = int(user_inputs[0])
k = int(user_inputs[1])
numbers = list(map(int, input().split(" ")))
numbers_copy = numbers[:]
flag = 0
flag_2 = 0
first_k = numbers[k - 1]

if(n == 1 or len(Counter(numbers)) == 1):
    flag = 0
    flag_2 = 1
else:
    for i in range(n - k + 1):
        if(first_k != numbers[k + i - 1]):
            flag = -1
            flag_2 = 1
            break

    if(flag != -1 and flag_2 == 0):
        for i in range(1, k - 1):
            if(numbers[k - 2] == numbers[k - 1]):
                k = k - 1
            else:
                break
        flag = k - 1
print(flag)
