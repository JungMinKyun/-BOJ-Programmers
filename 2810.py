# 백준 2810번 컵홀더

n = int(input())
seats = input().strip()

couple = 0
for seat in seats:
    if seat == 'L':
        couple += 1

print(min(n, n+1 - couple//2))