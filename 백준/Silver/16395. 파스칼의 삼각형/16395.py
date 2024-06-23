# 백준  16395 파스칼의 삼각형

n, k = map(int ,input().split())
factos = [1, 1]
for i in range(30):
    factos.append(factos[-1] * len(factos))

print(int(factos[n-1]/(factos[k-1] * factos[n-k])))