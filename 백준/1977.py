# 백준 1977 완전제곱수

minma = int(input())
maxma = int(input())

start = int(minma ** 0.5)

ans = []
while start ** 2 <= maxma:
    if start ** 2 >= minma:
        ans.append(start ** 2)
    start += 1

if not ans:
    print(-1)
else:
    print(sum(ans))
    print(ans[0])