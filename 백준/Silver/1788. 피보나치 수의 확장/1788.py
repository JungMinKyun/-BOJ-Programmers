# 백준 1788 피보나치 수의 확장

n = int(input())
mod = 1000000000

dp = [0, 1] + [0] * (abs(n)-1)
for i in range(2, abs(n)+1):
    dp[i] = (dp[i-1] + dp[i-2]) % mod
    
if n < 0 and abs(n) % 2 == 0:
    print(-1)
    print(dp[abs(n)])
elif n == 0:
    print(0)
    print(dp[n])
else:
    print(1)
    print(dp[abs(n)])