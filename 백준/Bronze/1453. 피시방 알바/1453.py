# 백준 1453 피시방 알바

n = int(input())
seats = list(map(int, input().split()))
seats = set(seats)

print(n - len(seats))