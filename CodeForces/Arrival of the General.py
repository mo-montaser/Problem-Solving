# https://codeforces.com/problemset/problem/144/A

n = int(input())
a = input().split(' ')

for i in range(len(a)):
    a[i] = int(a[i])

counter = 0
max_index = a.index(max(a))

if(2 <= n <= 100):
    if (max(a) <= 100 and min(a) >= 1):

        # max
        for i in range(0, max_index + 1):
            if(max_index == 0):
                break
            a[max_index], a[max_index - 1] = a[max_index - 1], a[max_index]
            max_index -= 1
            counter += 1

        # min
        min_index = a.index(min(a))

        # if there is any duplicates:
        for i in range(len(a)):
            if(a[i] == a[min_index]):
                min_index = i

        for i in range(min_index, len(a)):
            if(min_index == len(a) - 1):
                break
            a[min_index], a[min_index + 1] = a[min_index + 1], a[min_index]
            min_index += 1
            counter += 1

print(counter)
