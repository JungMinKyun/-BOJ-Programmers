# 백준 10824 네 수

A, B, C, D = map(int, input().split())

first = int(str(A) + str(B))
last = int(str(C) + str(D))

print(first + last)