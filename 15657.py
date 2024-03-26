# 백준 15657 N과 M (8)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

res = []
def BT():
    if len(res) == m:
        print(*res)
        return
    for i in range(n):
        elt = array[i]
        if res and elt < res[-1]:
            continue
        res.append(elt)
        BT()
        res.pop()

BT()