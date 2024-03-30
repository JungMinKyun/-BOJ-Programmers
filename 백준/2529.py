# 백준 2529 부등호

import sys
input = sys.stdin.readline

n = int(input())
operators = list(input().split())

res = []
chk = [False] * 10
ans = []
def BT():
    if len(res) == n+1:
        trigger = True
        for i in range(n):
            if operators[i] == '<':
                if res[i] >= res[i+1]:
                    trigger = False
                    break
            elif operators[i] == '>':
                if res[i] <= res[i+1]:
                    trigger = False
                    break
        if trigger:
            temp = ''
            for i in range(n+1):
                temp += str(res[i])
            ans.append(temp)
        return

    for i in range(10):
        if chk[i]:
            continue
        res.append(i)
        chk[i] = True
        BT()
        res.pop()
        chk[i] = False

BT()
print(max(ans))
print(min(ans))