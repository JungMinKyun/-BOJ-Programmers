# 백준 1268 임시반장 정하기

import sys
input = sys.stdin.readline

students = []
n = int(input())
for _ in range(n):
    stud = list(map(int, input().split()))
    students.append(stud)

count = 0
ans = 0

for i in range(n):
    temp_cnt = 0
    for j in range(n):
        if i != j:
            for k in range(5):
                if students[i][k] == students[j][k]:
                    temp_cnt += 1
                    break
    if temp_cnt > count:
        count = temp_cnt
        ans = i + 1

if not ans: print(1)
else: print(ans)