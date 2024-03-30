# 백준 10819 차이를 최대로

n = int(input())
array = list(map(int, input().split()))

res = []
chk = [False] * n
ans = []
def BT():
    if len(res) == n:
        temp = 0
        for i in range(n-1):
            temp += abs(res[i]-res[i+1])
        ans.append(temp)
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
print(max(ans))