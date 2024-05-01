# 백준 2457 공주님의 정원

import sys
input = sys.stdin.readline

n = int(input())
flowers = []
for i in range(n):
    sm, sd, em, ed = map(int, input().split())
    flowers.append((sm*100+sd, em*100+ed))
flowers.sort()

cnt = 0
start_date = 301
end_date = 0

while flowers:
    if (start_date >= 1201) or (start_date < flowers[0][0]):
        break

    for _ in range(len(flowers)):
        if flowers[0][0] <= start_date:
            if flowers[0][1] >= end_date:
                end_date = flowers[0][1]
            flowers.pop(0)
        else:
            break
    start_date = end_date
    cnt += 1

if start_date <= 1130:
    print(0)
else:
    print(cnt)