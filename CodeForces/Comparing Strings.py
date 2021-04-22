# https://codeforces.com/problemset/problem/186/A

# import time
# start = time.time()

first = input()
second = input()
flag = 0
counter = 0
if(len(first) == len(second) and len(first) == 2):
    if(first[1] + first[0] == second):
        print("YES")
    else:
        print("NO")
elif(first != second and len(first) == len(second) and len(first) > 2):

    for i in range(len(first)):
        if(first[i] != second[i]):
            counter += 1

            if(counter == 1):
                index_1 = flag
            elif(counter == 2):
                index_2 = flag
                first_swap = first[0:index_1] + first[index_2] + first[index_1 + 1:index_2] + first[index_1] + first[index_2 + 1:]
                if(first_swap == second):
                    print("YES")
                    break
                else:
                    print("NO")
                    break
        flag += 1

    if(counter == 1):
        print("NO")

else:
    print("NO")

# end = time.time()
# print(end - start)
