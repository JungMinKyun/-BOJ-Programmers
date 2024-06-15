# 백준 11729 하노이 탑 이동 순서

n = int(input())

def move_tower(start, middle, end, k):
    temp = []
    if k == 2:
        temp = [[start, middle], [start, end], [middle, end]]
        return temp
    else:
        temp.extend(move_tower(start, end, middle, k-1))
        temp.append([start, end])
        temp.extend(move_tower(middle, start, end, k-1))
        return temp

if n == 1:
    ans = [[1, 3]]
else:
    ans = move_tower(1, 2, 3, n)

print(len(ans))
for i in ans:
    print(*i)