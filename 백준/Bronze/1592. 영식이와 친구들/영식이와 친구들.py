# 백준 1592 영식이와 친구들

n, m, l = map(int, input().split())
people = [0]*n

posit, maxim = 0, 0
while maxim < m:
    people[posit] += 1
    if people[posit] % 2 == 1:
        posit = (posit+l)%n
    else:
        posit = (posit-l)%n

    maxim = max(people)

print(sum(people)-1)