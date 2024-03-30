# 백준 2212 센서

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensors = list(map(int, input().split()))

sensors.sort()

result = []
for i in range(n-1):
    result.append(sensors[i+1] - sensors[i])

result.sort()
print(sum(result[:n-k]))