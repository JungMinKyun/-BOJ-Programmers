# 백준 10974 모든 순열

n = int(input())
array = [i+1 for i in range(n)]

res = []
chk = [False] * n
def BT():
    if len(res) == n:
        print(*res)
        return
    for i in range(n):
        elt = array[i]
        if chk[i]:
            continue
        res.append(elt)
        chk[i] = True
        BT()
        res.pop()
        chk[i] = False

BT()