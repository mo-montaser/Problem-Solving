# https://codeforces.com/problemset/problem/145/A

a = list(input())
b = list(input())

a_copy = a[:]
a_copy.sort()
b_copy = b[:]
b_copy.sort()

replace_counter = 0
swap_counter = 0

for i in range(len(a_copy)):
    if(a_copy[i] != b_copy[i]):
        replace_counter += 1

for i in range(len(a)):
    if (a[i] != b[i]):
        swap_counter += 1

swap_counter = (swap_counter - replace_counter) // 2
print(replace_counter + swap_counter)
