# 백준 1731 추론

import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

if arr[1]-arr[0] == arr[2]-arr[1]:
    print(arr[-1] + arr[-1] - arr[-2])

else:
    print(arr[-1] * (arr[1]//arr[0]))
