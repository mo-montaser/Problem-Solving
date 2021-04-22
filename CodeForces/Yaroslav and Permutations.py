# https://codeforces.com/problemset/problem/296/A

# import time

# start = time.time()
n = int(input())
array = input().split()
c = (n + 1) / 2
most_repeated = max(set(array), key=array.count)
counter = 0

for i in array:
    if(i == most_repeated):
        counter += 1
    else:
        continue

if(c <= counter and n % 2 == 0):
    print("NO")
elif(c < counter and n % 2 != 0):
    print("NO")
else:
    print("YES")

# end = time.time()

# print("most_repeated =", most_repeated)
# print("c =", c)
# print("counter =", counter)
# print(end - start)
