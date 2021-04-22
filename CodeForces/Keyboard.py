# https://codeforces.com/problemset/problem/474/A

shift = input()
message = input()
keyboard = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']
orignal_message = ''

for i in message:
    if(shift == 'R'):
        orignal_message += keyboard[keyboard.index(i) - 1]
    else:
        orignal_message += keyboard[keyboard.index(i) + 1]

print(orignal_message)
