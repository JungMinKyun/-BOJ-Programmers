# 백준 19941 햄버거 분배

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
array = list(input())
person_visited = [0] * n
ham_visited =[0] * n

for i in range(n):
    if array[i] == 'P' and not person_visited[i]:
        min_idx = max(0, i-k)
        max_idx = min(n, i+k+1)
        for j in range(min_idx, max_idx):
            if array[j] == 'H' and not ham_visited[j]:
                person_visited[i] = 1
                ham_visited[j] = 1
                break

print(sum(ham_visited))
