# 백준 18310 안테나

import sys  
input = sys.stdin.readline

n = int(input())
ants = sorted(list(map(int, input().split())))

print(ants[(n-1)//2])