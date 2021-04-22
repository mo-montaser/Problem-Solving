# https://codeforces.com/problemset/problem/136/A

n = int(input())  # number of his friends

Pi = input().split(' ')  # givers
Pi_i_dict = {}  # receivers

for j in range(n):
    Pi_i_dict[int(Pi[j])] = j + 1

for i in range(1, n + 1):
    print(Pi_i_dict[i], end=' ')
