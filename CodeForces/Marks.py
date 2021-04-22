# https://codeforces.com/problemset/problem/152/A

n, m = input().split(" ")
gradebook = []
best = 0
successful_students = []

for i in range(int(n)):
    gradebook.append(input())

for i in range(int(m)):
    grades = []  # grades comparison

    for j in range(int(n)):
        grades.append(gradebook[j][i])

    best = max(grades)

    for j in range(int(n)):
        if(grades[j] == best):
            if j not in successful_students:
                successful_students.append(j)

print(len(successful_students))
