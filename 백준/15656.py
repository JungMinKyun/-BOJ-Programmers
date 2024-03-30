# 백준 15656 N과 M (7)

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
        res.append(elt)
        BT()
        res.pop()

BT()