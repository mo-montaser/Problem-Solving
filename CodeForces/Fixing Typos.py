# https://codeforces.com/problemset/problem/363/C


def fixing_typos(s):
    i = 0
    if(len(s) > 2):
        for i in range(len(s) - 2):
            if(s[i] == s[i + 1] == s[i + 2]):
                s[i] = ""

        s = list("".join(s))

    if(len(s) > 3):
        for i in range(len(s) - 3):
            if(s[i] == s[i + 1] and s[i + 2] == s[i + 3]):
                s[i + 2] = ""

    return "".join(s)


string = list(input())
print(fixing_typos(string))
