# https://codeforces.com/problemset/problem/734/A

n = int(input())
s = input()
A = s.count("A")
D = s.count("D")

if(A > D):
    print("Anton")
elif(D > A):
    print("Danik")
else:
    print("Friendship")
