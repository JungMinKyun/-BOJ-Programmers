# 백준 1092 배

import sys
input = sys.stdin.readline

n = int(input())
cranes = list(map(int, input().split()))
cranes.sort(reverse=True)
m = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse=True)

if boxes[0] > cranes[0]:
    print(-1)
else:
    ans = 0
    while boxes:
        for crane in cranes:
            if boxes and crane >= boxes[-1]:
                for box in boxes:
                    if crane >= box:
                        boxes.remove(box)
                        break
        ans += 1
    print(ans)
