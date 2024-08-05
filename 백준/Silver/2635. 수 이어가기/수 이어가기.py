# 백준 2635 수 이어가기

import sys
input = sys.stdin.readline

n = int(input())
max_list = []

for i in range(1, n+1):
    temp_list = [n]
    temp_list.append(i)

    idx = 1
    while True:
        next_num = temp_list[idx-1] - temp_list[idx]
        if next_num < 0:
            break
        temp_list.append(next_num)
        idx += 1

    if len(max_list) < len(temp_list):
        max_list = temp_list

print(len(max_list))
print(*max_list)
