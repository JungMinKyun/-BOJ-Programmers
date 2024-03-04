# 백준 1541번 잃어버린 괄호

equation = input().split('-')
plus = []

for i in equation:
    plus.append(sum(map(int, i.split('+'))))

print(plus[0] - sum(plus[1:]))