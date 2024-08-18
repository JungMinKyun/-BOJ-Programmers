# 백준 5800 성적통계

import sys
input = sys.stdin.readline

for order in range(int(input())):
    nums = list(map(int, input().split()))
    n = nums[0]
    array = nums[1:]

    array.sort()
    maxim, minim = array[-1], array[0]

    gap = 0
    for i in range(n-1):
        gap = max(gap, array[i+1]-array[i])

    print('Class {0}'.format(order+1))
    print('Max {0}, Min {1}, Largest gap {2}'.format(maxim, minim, gap))