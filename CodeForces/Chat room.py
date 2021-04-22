# https://codeforces.com/problemset/problem/85/A

s = input()
hello = "hello"
word = ""
j = 0

for i in range(len(s)):

    if(s[i] == hello[j]):
        word += s[i]
        j += 1
        if(j == 5):
            break

if(word == hello):
    print("YES")
else:
    print("NO")
