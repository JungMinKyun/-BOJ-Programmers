# 백준 9527 1의 개수 세기

import sys
import math
input = sys.stdin.readline

def count_one(n):
    if n <= 0:
        return 0
    log_num = int(math.log2(n))
    power = 2**log_num

    if n == power:
        return log_num * n // 2 + 1
    
    diff = n - power
    return count_one(power) + diff + count_one(diff)
    
a, b = map(int, input().split())
print(count_one(b) - count_one(a-1))