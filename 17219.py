# 백준 17219 비밀번호 찾기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
id_pw = {}
for _ in range(n):
    key, value = input().strip().split()
    id_pw[key] = value

for _ in range(m):
    key = input().rstrip()
    print(id_pw[key])