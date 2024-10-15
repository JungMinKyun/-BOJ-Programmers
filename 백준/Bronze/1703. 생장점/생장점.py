# 백준 1703 생장점

import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if not arr[0]:
        break
    result = 1

    for i in range(arr[0]):
        result *= arr[2*i+1]
        result -= arr[2*i+2]
        
    print(result)