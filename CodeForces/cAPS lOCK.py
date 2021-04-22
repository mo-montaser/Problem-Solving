# https://codeforces.com/problemset/problem/131/A

caps_word = input()

if(len(caps_word) == 1):
    if(caps_word.isupper()):
        word = caps_word.lower()
    else:
        word = caps_word.upper()
elif(caps_word[1:].isupper()):
    if(caps_word[0].islower()):
        word = caps_word[0].upper() + caps_word[1:].lower()
    else:
        word = caps_word.lower()
else:
    word = caps_word

print(word)
