# 백준 15663번 N과 M (9)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

result = []
chk = [False]*N

def BT():
    if len(result)==M:
        print(*result)
        return
    value = -1
    for i in range(N):
        num = array[i]
        if value == num:
            continue
        if chk[i]:
            continue
        value = num
        result.append(num)
        chk[i] = True
        BT()
        result.pop()
        chk[i] = False

BT()
