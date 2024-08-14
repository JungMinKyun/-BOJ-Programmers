# 백준 18110 solved.ac

import sys
input = sys.stdin.readline

def rounding(num):
  if num - int(num) >= 0.5:
    return int(num)+1
  else:
    return int(num)

n = int(input())

if n == 0:
    print(0)
else:
    nums = [int(input()) for _ in range(n)]
    nums.sort()

    cutline = rounding(n * 0.15)
    
    temp = nums[cutline : n-cutline]
    print(rounding(sum(temp)/len(temp)))