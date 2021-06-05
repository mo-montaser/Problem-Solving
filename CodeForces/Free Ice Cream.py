# https://codeforces.com/problemset/problem/686/A

n, ice_cream = map(int, input().split())
user_input = []
for i in range(n):
    user_input.append(input().split())
kids = 0

for i in range(n):
    if user_input[i][0] == "+":
        ice_cream += int(user_input[i][1])
    elif int(user_input[i][1]) <= ice_cream:
        ice_cream -= int(user_input[i][1])
    else:
        kids += 1

print(ice_cream, kids)
