# 백준 9661 돌 게임 7

import sys
input = sys.stdin.readline

k = int(input()) % 5

if k == 0 or k == 2: print('CY')
else: print('SK')