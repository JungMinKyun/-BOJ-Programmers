# 백준 1789 수들의 합

n = int(input())

ans = 0
for i in range(1, n+1):
    n -= i
    ans += 1
    if n <= i:
        break
print(ans)