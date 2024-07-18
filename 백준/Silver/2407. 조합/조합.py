# 백준 2407 조합

factos = [1]
for i in range(99):
    factos.append(factos[-1] * (i+2))

n, m = map(int, input().split())
print(factos[n-1] // (factos[m-1] * factos[n-m-1]))