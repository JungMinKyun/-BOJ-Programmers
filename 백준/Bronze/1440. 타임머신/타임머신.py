# 백준 1440 타임머신

time = list(map(int, input().split(':')))
ans = 0

for i in range(3):
    for j in range(3):
        for k in range(3):
            if i!=j and j!=k and i!=k:
                if 1<=time[i]<=12 and 0<=time[j]<=59 and 0<=time[k]<=59:
                    ans += 1

print(ans)