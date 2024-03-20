# 백준 2004 조합 0의 개수

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def two_or_five(n):
    two, five = 0, 0
    two_n, five_n = n, n
    while two_n != 0:
        two_n = two_n // 2
        two += two_n

    while five_n != 0:
        five_n = five_n // 5
        five += five_n
    return two, five

two_n, five_n = two_or_five(n)
two_m, five_m = two_or_five(m)
two_nm, five_nm = two_or_five(n-m)

print(min(two_n - two_m - two_nm, five_n - five_m - five_nm))