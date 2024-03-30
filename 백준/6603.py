# 백준 6603 로또

import sys
input = sys.stdin.readline

while True:
    array = list(map(int, input().split()))
    if array[0] == 0:
        break
    n = array[0]
    array = array[1:]

    res = []
    chk = [False] * n

    def BT():
        if len(res) == 6:
            print(*res)
            return
        for i in range(n):
            elt = array[i]
            if chk[i]:
                continue
            if res and res[-1] >= elt:
                continue
            res.append(elt)
            chk[i] = True
            BT()
            res.pop()
            chk[i] = False
    
    BT()
    print()