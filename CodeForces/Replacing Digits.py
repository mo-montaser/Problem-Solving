# https://codeforces.com/problemset/problem/169/B

# import time
# start = time.time()
a = input()
s = input()
s = "".join(sorted(s, reverse=True))
j = 0

for i in range(len(a)):
    if(a[i] < s[j]):
        a = a[0:i] + s[j] + a[i + 1:]
        j = j + 1

    if(j == len(s)):
        break
print(a)

# end = time.time()
# print(end - start)
