# 백준 1302 베스트셀러

result = {}
n = int(input())
for _ in range(n):
    book = str(input())
    if book not in result:
        result[book] = 1
    else:
        result[book] += 1

cnt = 0
for key, value in result.items():
    if value > cnt:
        ans = [key]
        cnt = value
    elif value == cnt:
        ans.append(key)

ans.sort()
print(ans[0])