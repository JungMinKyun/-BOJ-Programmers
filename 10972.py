# 백준 10972 다음 순열

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

if array==sorted(array, reverse=True):
    print(-1)
else:
    for i in range(n-1, 0, -1):
        if array[i-1] < array[i]:
            for j in range(n-1, 0, -1):
                if array[i-1] < array[j]:
                    array[i-1], array[j] = array[j], array[i-1]
                    array = array[:i] + sorted(array[i:])
                    print(*array)
                    sys.exit()