# 백준 2011 암호코드

import sys
input = sys.stdin.readline
string = input().strip()
n = len(string)

dp = [1] + [0] * n

for i in range(1, n+1):
    temp = string[:i]
    if int(temp[-2:]) <= 26:
        if int(temp[-2:]) == 0:
            dp[i] = 0
        elif int(temp[-1]) == 0:
            dp[i] = dp[i-2]
        elif i >=2 and int(temp[-2]) == 0:
            dp[i] = dp[i-1]
        else:
            dp[i] = (dp[i-2] + dp[i-1]) % 1000000
    else:
        if int(temp[-1]) == 0:
            dp[i] = 0
        else: 
            dp[i] += (dp[i-1])

print((dp[n]) % 1000000)