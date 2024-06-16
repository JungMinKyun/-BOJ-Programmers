# 백준 1024 수열의 합

n, k = map(int, input().split())

trigger = True
while k <= 100:
    diff = k*(k-1)//2
    if diff > n:
        trigger = False
        break
    elif (n - diff) % k == 0:
        break
    k += 1

if not trigger or k > 100:
    print(-1)
else:
    ans = [i for i in range((n-diff)//k, (n-diff)//k+k)]
    print(*ans)