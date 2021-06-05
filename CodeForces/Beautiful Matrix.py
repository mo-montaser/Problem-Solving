# https://codeforces.com/problemset/problem/263/A

matrix = []
for i in range(5):
    matrix.append(input().split())
    if "1" in matrix[i]:
        index_1 = [i, matrix[i].index("1")]

row_moves = 2 - index_1[0]
col_moves = 2 - index_1[1]

if row_moves < 0:
    row_moves = - row_moves
if col_moves < 0:
    col_moves = - col_moves

print(row_moves + col_moves)
