# 백준 1292 쉽게 푸는 문제

a, b = map(int, input().split())

arr = []
for i in range(1, 46):
    arr += [i]*i

print(sum(arr[a-1:b]))
