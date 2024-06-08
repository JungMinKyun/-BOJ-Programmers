# 백준 1188 음식 평론가

def euclidean(a, b):
    if b == 0:
        return a
    return euclidean(b, a % b)

n, m = map(int, input().split())
print(m - euclidean(n, m)) 