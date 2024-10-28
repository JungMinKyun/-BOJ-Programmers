# 백준 2506 점수계산

n = int(input())
score = list(map(int, input().split()))

for i in range(n):
    if i > 0 and score[i] == 1:
        score[i] = score[i-1] + 1

print(sum(score))