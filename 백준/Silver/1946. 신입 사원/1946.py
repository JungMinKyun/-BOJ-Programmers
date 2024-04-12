# 백준 1946 신입 사원

import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    emp = []
    for _ in range(n):
        a, b = map(int, input().split())
        emp.append((a,b))

    emp.sort()
    ans = 0
    trigger = emp[0][1]
    for i in range(1, n):
        if emp[i][1] < trigger:
            ans += 1
            trigger = emp[i][1]

    print(ans + 1)