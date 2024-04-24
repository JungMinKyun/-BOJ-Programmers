# 백준 2138 전구와 스위치

import sys
input = sys.stdin.readline

n = int(input())
init = list(input())
goal = list(input())

for i in range(n):
    init[i] = int(init[i])
    goal[i] = int(goal[i])

temp_init = init[:]

res = 0
for j in range(2):
    init[0] = (init[0]+j)%2
    init[1] = (init[1]+j)%2

    for i in range(1, n):
        if init[i-1] != goal[i-1]:
            res += 1
            init[i-1] = (init[i-1]+1)%2
            init[i] = (init[i]+1)%2
            if i != n-1:
                init[i+1] = (init[i+1]+1)%2

    for i in range(n):
        if init[i] != goal[i]:
            init = temp_init[:]
            res = 1
            break
    else:
        print(res)
        sys.exit()

print(-1)