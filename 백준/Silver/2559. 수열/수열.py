# 백준 2559 수열

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
array = list(map(int, input().split()))
sum_list = [array[0]]
for i in range(1, n):
    sum_list.append(array[i] + sum_list[-1])

if k == 1:
    ans = max(array)
else:
    ans = sum_list[k-1]
    for i in range(k, n):
        ans = max(ans, sum_list[i] - sum_list[i-k])
    
print(ans)