# 백준 2139 나는 너가 살아온 날을 알고 있다

import sys
input = sys.stdin.readline

while True:
    day_cnt = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d, m, y = map(int, input().split())
    if d == 0 and m == 0 and y == 0:
        break
    
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        day_cnt[1] = 29

    print(sum(day_cnt[:m-1]) + d)