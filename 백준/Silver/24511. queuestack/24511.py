# 백준 24511 queuestack

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split())) 
b = list(map(int, input().split())) 
m = int(input())                    
c = list(map(int, input().split())) 

Q = deque()

for i in range(n):
    if a[i] == 0:
        Q.appendleft(b[i])
        
for i in range(m):
    Q.append(c[i])
    print(Q.popleft(), end=' ')