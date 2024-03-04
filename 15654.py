# 백준 15654번 N과 M (5)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

result = []

def BT():
    if len(result)==M:
        print(*result)
        return
    for num in array:
        if num in result:
            continue
        result.append(num)
        BT()
        result.pop()

BT()