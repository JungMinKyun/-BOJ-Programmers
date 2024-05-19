# 백준 1007 벡터 매칭

from itertools import combinations
import sys
input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())
    x_sum, y_sum = 0, 0
    vectors = []
    for i in range(n):
        x, y = map(int, input().split())
        x_sum += x
        y_sum += y
        vectors.append((x, y))

    vector_comb = list(combinations(vectors, n//2))
    ans = 1e9

    for c in vector_comb[:len(vector_comb)//2]:
        x1 = 0
        y1 = 0
        for x, y in c:
            x1 += x
            y1 += y
        x2 = x_sum - x1
        y2 = y_sum - y1

        ans = min(ans, ((x2-x1)**2 + (y2-y1)**2)**0.5)

    print(ans)
