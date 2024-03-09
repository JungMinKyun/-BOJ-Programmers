# 백준 12904 A와B

import sys
input = sys.stdin.readline

s = list(input().strip())
t = list(input().strip())

flag = 0
while t:
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()
    if t == s:
        flag = 1
        break

if flag:
    print(1)
else:
    print(0)