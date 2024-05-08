# 백준 1027 고층 건물

n = int(input())
buildings = list(map(int, input().split()))

result = 0

for i in range(n):
    cnt = n - 1
    for j in range(i+1, n):
        for k in range(i+1, j):
            y_diff = buildings[j] - buildings[i]
            x_diff = j - i
            if (buildings[k] - buildings[i]) >= (y_diff / x_diff) * (k - i):
                cnt -= 1
                break
    for j in range(0, i):
        for k in range(j+1, i):
            y_diff = buildings[j] - buildings[i]
            x_diff = j - i
            if (buildings[k] - buildings[j]) >= (y_diff / x_diff) * (k - j):
                cnt -= 1
                break

    result = max(result, cnt)
print(result)