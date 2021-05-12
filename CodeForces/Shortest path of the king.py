# https://codeforces.com/problemset/problem/3/A

s = input()
t = input()
row = ["a", "b", "c", "d", "e", "f", "g", "h"]
y0 = int(s[1])
y1 = int(t[1])

x0 = row.index(s[0])
x1 = row.index(t[0])
moves = []
while True:
    x, y = "", ""
    if(x1 == x0 and y1 == y0):
        break

    if(x1 > x0):
        x0 = x0 + 1
        x = "R"

    elif(x1 < x0):
        x0 = x0 - 1
        x = "L"

    if(y1 > y0):
        y0 = y0 + 1
        y = "U"
    elif(y1 < y0):
        y0 = y0 - 1
        y = "D"
    moves.append(x + y)


print(len(moves))
for move in moves:
    print(move)
