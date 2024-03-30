# 백준 9093 단어 뒤집기

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    string = list(input().strip().split())
    result = []
    for word in string:
        result.append(word[::-1])
    
    print(*result)
