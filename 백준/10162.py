# 백준 10162번 전자레인지

N = int(input())

ans = []
ans.append(N//300)
N = N%300
ans.append(N//60)
N = N%60
ans.append(N//10)

if N%10 == 0:
    print(*ans)
else:
    print(-1)