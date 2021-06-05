# https://codeforces.com/problemset/problem/381/A

n = int(input())
cards = list(map(int, input().split()))
Sereja = 0
Dima = 0
i = 0
j = n - 1

while True:

    if(i == j):
        Sereja += cards[i]
        break

    if(cards[i] > cards[j]):
        Sereja += cards[i]
        i += 1
    else:
        Sereja += cards[j]
        j -= 1

    if(i == j):
        Dima += cards[i]
        break

    if(cards[i] > cards[j]):
        Dima += cards[i]
        i += 1
    else:
        Dima += cards[j]
        j -= 1


print(Sereja, Dima)
