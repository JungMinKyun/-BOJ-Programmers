# 백준 1350 진짜 공간

n = int(input())
files = map(int, input().split())
cluster = int(input())

ans = 0
for file in files:
    if file % cluster == 0:
        ans += file // cluster
    else:
        ans += file // cluster + 1

print(ans * cluster)