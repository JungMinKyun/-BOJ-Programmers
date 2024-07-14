# 백준 30802 웰컴 키트

n = int(input())
sizes = list(map(int, input().split()))
t, p = map(int, input().split())

ans = 0
for size in sizes:
    if size % t != 0:
        ans += (size//t) + 1
    else:
        ans += size//t
print(ans)
print(n//p, n%p)