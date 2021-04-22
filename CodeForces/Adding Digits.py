# https://codeforces.com/problemset/problem/260/A

user_input = input().split()
a = int(user_input[0])
b = int(user_input[1])
n = int(user_input[2])
a_copy = a

for j in range(0, 10):

    add = int(str(a) + str(j))
    if(add % b == 0):
        a = str(add) + "0" * (n - 1)
        break
    if(j == 9 and a_copy == a):
        a = -1
        break

print(a)
