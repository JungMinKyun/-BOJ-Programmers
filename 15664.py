# 백준 15664 N과 M (10)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

res = []
chk = [False] * n

def BT():
    if len(res) == m:
        print(*res)
        return
    val = -1
    for i in range(n):
        elt = array[i]
        if val == elt:
            continue
        if chk[i]:
            continue
        if res and res[-1] > elt:
            continue
        val = elt
        res.append(elt)
        chk[i] = True
        BT()
        res.pop()
        chk[i] = False

BT()