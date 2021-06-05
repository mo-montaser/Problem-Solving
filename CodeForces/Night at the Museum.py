# https://codeforces.com/problemset/problem/731/A

name = input()
wheel = "abcdefghijklmnopqrstuvwxyz"
counter = 0
pointer = 0

for i in range(len(name)):
    clockwise = abs(pointer - wheel.index(name[i]))
    counterclockwise = abs(26 - clockwise)
    counter += min(clockwise, counterclockwise)
    pointer = wheel.index(name[i])

print(counter)
