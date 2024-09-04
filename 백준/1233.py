# 백준 1233 주사위

a, b, c = map(int, input().split())

ans = [0] * 81
for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            val = i + j + k
            ans[val] += 1

print(ans.index(max(ans)))