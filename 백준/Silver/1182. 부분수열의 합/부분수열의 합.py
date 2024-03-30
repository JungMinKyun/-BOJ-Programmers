# 백준 1182 부분수열의 합

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

cnt = 0
res = []
chk = [False] * n

def BT(now):
    global cnt
    if res and sum(res) == s:
        cnt += 1

    if len(res) == n:
        return
    
    for i in range(now, n):
        elt = array[i]
        if chk[i]:
            continue
        chk[i] = True
        res.append(elt)
        BT(i+1)
        res.pop()
        chk[i] = False
        
BT(0)
print(cnt)    