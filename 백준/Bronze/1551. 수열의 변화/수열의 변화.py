# 백준 1551 수열의 변환

n, k = map(int, input().split())
num = list(map(int, input().split(',')))


for _ in range(k):
    ans = []
    for i in range(len(num)-1):
        ans.append(num[i+1]-num[i])
    num = ans

print(','.join(map(str, num)))