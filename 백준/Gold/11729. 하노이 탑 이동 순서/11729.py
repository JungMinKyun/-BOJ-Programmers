# 백준 11729 하노이 탑 이동 순서

n = int(input())

def move_tower(start, end, k):
    temp = []
    if k == 1:
        temp.append([start, end])
        return temp
    else:
        temp.extend(move_tower(start, 6-start-end, k-1))
        temp.append([start, end])
        temp.extend(move_tower(6-start-end, end, k-1))
        return temp

ans = move_tower(1, 3, n)
print(len(ans))
for i in ans:
    print(*i)