# 백준 28279 덱 2

from collections import deque
import sys
input = sys.stdin.readline

Q = deque()
n = int(input())
for i in range(n):
    command = list(map(int, input().split()))
    length = len(Q)
    if command[0] == 1:
        Q.appendleft(command[1])
    elif command[0] == 2:
        Q.append(command[1])
    elif command[0] == 3:
        print(Q.popleft() if length else -1)
    elif command[0] == 4:
        print(Q.pop() if length else -1)
    elif command[0] == 5:
        print(length)
    elif command[0] == 6:
        print(0 if length else 1)
    elif command[0] == 7:
        print(Q[0] if length else -1)
    elif command[0] == 8:
        print(Q[-1] if length else -1)