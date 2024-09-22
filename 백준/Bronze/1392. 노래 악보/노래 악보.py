# 백준 1392 노래악보

arr = []

n, q = map(int, input().split())
for i in range(n):
    time = int(input())
    for _ in range(time):
        arr.append(i+1)

for _ in range(q):
    query = int(input())
    print(arr[query])