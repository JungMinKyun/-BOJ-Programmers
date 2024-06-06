# 백준 1229 육각수

import sys
input = sys.stdin.readline

n = int(input())
hexanums = [1]
hexalen = 1
while True:
    num = hexanums[-1] + 4*hexalen+1
    if num > min(1000000, n):
        break
    hexanums.append(num)
    hexalen += 1

dp = [0, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 2] + [1e9] * n

if n <= 12:
    print(dp[n])
else:
    for i in range(13, n+1):
        minimum = 1e9
        for hexanum in hexanums:
            if hexanum > i:
                break
            minimum = min(minimum, dp[i-hexanum])
        dp[i] = minimum + 1
    print(dp[n])