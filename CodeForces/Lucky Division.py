# https://codeforces.com/problemset/problem/122/A

n = int(input())
flag = 0
lucky_numbers = [4, 44, 47, 444, 447, 474, 7, 74, 77, 777, 774, 747]

for i in str(n):
    if(i != "4" and i != "7"):
        flag = 1
        break

if(flag == 1):
    for i in lucky_numbers:
        if(n % i == 0):
            flag = 0
            break

if(flag == 0):
    print("YES")
else:
    print("NO")
