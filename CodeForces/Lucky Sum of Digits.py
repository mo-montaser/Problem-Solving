n = int(input())

for a in range(n):
    b = (n - 4 * a) / 7

    if(4 * a > n or n == 1):
        print(-1)
        break

    if (b.is_integer()):
        print("4" * a + "7" * int(b))
        break
