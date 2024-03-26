# 백준 15655 N과 M (6)

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
array = list(map(int, input().split()))
array.sort()
chk = [False] * n

res = []
def BT():
    if len(res) == m:
        print(*res)
        return
    for i in range(n):
        elt = array[i]
        if len(res) > 0 and elt < res[-1]:
            continue
        if chk[i]:
            continue
        chk[i] = True
        res.append(elt)
        BT()
        chk[i] = False
        res.pop()

BT()